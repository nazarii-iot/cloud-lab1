variable "aws_region" {
  description = "AWS region for the lab"
  type        = string
  default     = "eu-north-1"
}

variable "project_name" {
  description = "Prefix used for lab resources"
  type        = string
  default     = "cloud-lab1"
}

variable "db_username" {
  description = "Database username"
  type        = string
  default     = "clouduser"
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

variable "vpc_cidr" {
  description = "CIDR range for the lab VPC"
  type        = string
  default     = "10.20.0.0/16"
}

variable "image_tag" {
  description = "Immutable Docker image tag in ECR"
  type        = string
  default     = "bootstrap"
}