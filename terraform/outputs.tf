output "api_url" {
  description = "Public URL of the REST API"
  value       = "http://${aws_lb.api.dns_name}"
}

output "ecr_repository_url" {
  description = "Private ECR repository URL"
  value       = aws_ecr_repository.api.repository_url
}

output "rds_endpoint" {
  description = "PostgreSQL endpoint"
  value       = aws_db_instance.main.address
}