resource "aws_sns_topic" "water_reminder" {
  name = "water-reminder-topic"
}

resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.water_reminder.arn
  protocol  = "email"
  endpoint  = var.email
}
