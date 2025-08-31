# Water Reminder

This project provides an automated daily weather-based reminder system using AWS Lambda, SNS, and Terraform. It fetches weather forecasts and sends a daily email notification to remind you to water your plants (or not!) based on rain probability.

## Features
- Fetches weather forecast from the UK Met Office API
- Analyzes rain probability for the next 3 days
- Sends a daily email notification via AWS SNS
- Fully automated and scheduled using AWS CloudWatch Events
- Infrastructure as Code with Terraform

## Directory Structure

- `src/` — Python source code for Lambda (main logic and handler)
- `terraform/` — Terraform configuration for AWS resources

## Prerequisites
- AWS account with permissions to create Lambda, SNS, IAM, and CloudWatch resources
- Terraform >= 1.0.0
- Python 3.10
- A valid Met Office [Datahub API key](https://datahub.metoffice.gov.uk/)

## Setup & Deployment

1. **Clone the repository**

	```bash
	git clone <repo-url>
	cd water-reminder
	```

2. **Configure variables**

	Edit terraform/terraform.tfvars with your API key, coordinates, and email
	

3. **Install Lambda dependencies and package**

	```bash
	cd src
	pip install --target . requests boto3
	zip -r lambda.zip . -x "__pycache__/*"
	cd ..
	```

4. **Deploy with Terraform**

	```bash
	cd terraform
	terraform init
	terraform apply
	```
	Review and approve the plan.

5. **Confirm SNS Email Subscription**

	Check your email inbox for a confirmation email from AWS SNS and confirm the subscription to start receiving notifications.

## How it Works

- Every day at 8 AM UTC, AWS Lambda runs the weather analysis code.
- The Lambda function fetches the weather forecast, determines rain likelihood, and sends a message to your email via SNS.

## Customization
- Change the schedule in `terraform/schedule.tf` by editing the `cron` expression.
- Change the recipient email by updating the `email` variable in your `terraform.tfvars`.

## Cleanup
To remove all resources:

```bash
cd terraform
terraform destroy
```
