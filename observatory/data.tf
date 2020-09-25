data "aws_availability_zones" "all" {}

data "aws_ec2_instance_type_offerings" "all" {}

data "aws_ec2_instance_type_offering" "ec2_offerings" {
  for_each = toset(data.aws_availability_zones.all.names)
  
  filter {
    name   = "instance-type"
    values = [var.instance_type, "t3.micro", "t2.micro"]
	// values = slice(tolist(data.aws_ec2_instance_type_offerings.all.instance_types), 0, min(length(data.aws_ec2_instance_type_offerings.all.instance_types), 199))
  }

  filter {
    name   = "location"
    values = [each.value]
  }

  location_type = "availability-zone"

  preferred_instance_types = [var.instance_type, "t3.micro", "t2.micro"]
  //"${concat([var.instance_type], slice(tolist(data.aws_ec2_instance_type_offerings.all.instance_types), 0, min(length(data.aws_ec2_instance_type_offerings.all.instance_types), 199)))}"
}

output "foo" {
  value = keys({ for az, details in data.aws_ec2_instance_type_offering.ec2_offerings : az => details.instance_type if details.instance_type == var.instance_type })
}
