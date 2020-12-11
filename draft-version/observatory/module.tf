terraform {
  required_version = ">= 0.12"
}

provider "aws" {
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}


locals {
  az_names = slice(keys({ for az, details in data.aws_ec2_instance_type_offering.ec2_offerings : az => details.instance_type if details.instance_type == var.instance_type }), 0, var.availability_zones)
  es_domain = var.es_domain
}

resource "aws_vpc" "main" {
  cidr_block                       = "192.168.0.0/16"
  assign_generated_ipv6_cidr_block = "true"
  enable_dns_support               = "true"
  enable_dns_hostnames             = "true"

  tags = {
    Name = "observatory-${var.region}"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "observatory_igw" {
  vpc_id = aws_vpc.main.id
}

# Route table: attach Internet Gateway 
resource "aws_route_table" "public_rt" {
  vpc_id = "${aws_vpc.main.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.observatory_igw.id}"
  }
}

resource "aws_key_pair" "observatory" {
  key_name   = "observatory"
  public_key = file("${var.ssh_pub_key}")
  tags = {
    Key = "${var.ssh_private_key}"
  }
}

resource "aws_ecr_repository" "observatory_repo" {
  name = "p2p-observatory-repo"
}

resource "aws_subnet" "public" {
  count                           = length(local.az_names)
  vpc_id                          = aws_vpc.main.id
  cidr_block                      = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  ipv6_cidr_block                 = cidrsubnet(aws_vpc.main.ipv6_cidr_block, 8, count.index)
  map_public_ip_on_launch         = true
  assign_ipv6_address_on_creation = true
  availability_zone               = element(local.az_names, count.index)

  tags = {
    Name = "observatory-${element(local.az_names, count.index)}-public"
  }
}

resource "aws_security_group" "default" {
  vpc_id      = aws_vpc.main.id
  name        = "localip_ssh"
  description = "Allow ssh inbound traffic from my IP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${chomp(data.http.myip.body)}/32"]
  }

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}

# Route table associatiion with public subnets
resource "aws_route_table_association" "a" {
  count          = var.availability_zones * var.instances_per_az
  subnet_id      = "${element(aws_subnet.public.*.id,count.index)}"
  route_table_id = "${aws_route_table.public_rt.id}"
}

resource "aws_instance" "server" {
  key_name               = aws_key_pair.observatory.key_name
  count                  = var.availability_zones * var.instances_per_az
  instance_type          = var.instance_type
  ami                    = data.aws_ami.default.id
  subnet_id              = element(aws_subnet.public.*.id, count.index)
  ipv6_address_count     = "1"
  vpc_security_group_ids = [aws_security_group.default.id]

  credit_specification {
    cpu_credits = "standard"
  }

  tags = {
    Name = "observatory-server-${element(local.az_names, count.index)}-${count.index}"
  }
}

