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
}

data "aws_ami" "default" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-2.0.2020*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  owners = ["amazon"]
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


resource "aws_key_pair" "observatory" {
  key_name   = "observatory"
  public_key = file("${var.ssh_pub_key}")
  tags = {
    Key = "${var.ssh_private_key}"
  }
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
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port        = -1
    to_port          = -1
    protocol         = "icmpv6"
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_instance" "server" {
  key_name               = aws_key_pair.observatory.key_name
  count                  = var.availability_zones * var.instances_per_az
  instance_type          = var.instance_type
  ami                    = data.aws_ami.default.id
  subnet_id              = element(aws_subnet.public.*.id, count.index)
  ipv6_address_count     = "1"
  vpc_security_group_ids = [aws_security_group.default.id, aws_vpc.main.default_security_group_id]

  credit_specification {
    cpu_credits = "standard"
  }

  tags = {
    Name = "observatory-server-${element(local.az_names, count.index)}-${count.index}"
  }
}
