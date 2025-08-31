resource "aws_lambda_function" "water_reminder" {
  function_name = "water-reminder-lambda"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "lambda_handler.lambda_handler"
  runtime       = "python3.10"
  filename      = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  environment {
    variables = merge(
      var.lambda_env_vars,
      { SNS_TOPIC_ARN = aws_sns_topic.water_reminder.arn }
    )
  }
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "../src"
  output_path = "../src/lambda.zip"
}
