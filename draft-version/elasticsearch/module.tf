terraform {
  required_version = ">= 0.12"
}

provider "aws" {
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}


locals {
  es_domain = var.es_domain
}

resource "aws_elasticsearch_domain" "elasticsearch" {
  domain_name = local.es_domain
  elasticsearch_version = "7.1"

  cluster_config {
    instance_type = "t3.small.elasticsearch"
    instance_count = 1
  }

  ebs_options {
    ebs_enabled = true
    volume_size = 10
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }
  
  node_to_node_encryption{
      enabled = true
  }
  
  encrypt_at_rest{
      enabled = true
  }
  
  domain_endpoint_options{
      enforce_https       = true
      tls_security_policy = "Policy-Min-TLS-1-2-2019-07"
  }
  
  advanced_security_options {
      enabled                        = true
      internal_user_database_enabled = true

      master_user_options {
        master_user_name     = var.es_username
        master_user_password = var.es_password
      }

  }
}

resource "aws_elasticsearch_domain_policy" "elasticsearch-policy" {
  domain_name     = aws_elasticsearch_domain.elasticsearch.domain_name
  access_policies = data.template_file.elasticsearch-access-policy.rendered
}