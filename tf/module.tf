terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}

resource "aws_key_pair" "observatory" {
  key_name   = "observatory"
  public_key = file("${var.ssh_pub_key}")
  tags = {
    Name = "${var.ssh_private_key}"
  }
}

data "http" "myip"{
    url = "https://ipv4.icanhazip.com"
}

resource "aws_security_group" "localip_ssh" {
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

resource "aws_instance" "observatory" {
  key_name      = aws_key_pair.observatory.key_name
  ami           = "ami-0e273c93f05f09a49"
  instance_type = var.instance_type
  count         = var.servers_per_az
  security_groups = [
        "${aws_security_group.localip_ssh.name}"
    ]  
}

resource "null_resource" "cluster" {
  provisioner "local-exec" {
    command = "./create_ansible_hosts.py"
  }

}