output "lambda_function_name" {
  value = aws_lambda_function.water_reminder.function_name
}

output "sns_topic_arn" {
  value = aws_sns_topic.water_reminder.arn
}
