terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
  required_version = ">= 1.0.0"
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to deploy resources."
  type        = string
  default     = "eu-west-2"
}

variable "lambda_env_vars" {
  description = "Environment variables for Lambda (API key, latitude, longitude)"
  type        = map(string)
}

variable "email" {
  description = "Email address to send SNS notifications to."
  type        = string
}