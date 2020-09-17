variable "region" {
    default = "eu-west-1"
}

variable "accessKey" {}
variable "secretKey" {}

variable "servers_per_az" {
  default = 1
}

variable "instance_type" {
  default = "t3.medium"
}

variable "aws_profile" {
  default = "default"
}

variable "ssh_pub_key" {
  default = "~/.ssh/terraform.pub"
}

variable "ssh_private_key" {
  default = "~/.ssh/terraform"
}