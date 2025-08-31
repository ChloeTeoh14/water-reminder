# Lambda handler for AWS Lambda
# This wraps the main.py logic to be compatible with AWS Lambda
import os
import main
import json
import boto3

def lambda_handler(event, context):
    key = os.environ["API_KEY"]
    latitude = os.environ["LATITUDE"]
    longitude = os.environ["LONGITUDE"]
    
    # Run the main logic
    forecast = main.get_forecast(key, latitude, longitude)
    data  = forecast["features"][0]["properties"]["timeSeries"]
    three_day_weather = main.get_next_3_days_data(data)
    probability_rain_list = [main.get_rain_probabilities(day) for day in three_day_weather]
    highest_prob = main.determine_highest_probability(probability_rain_list)
    message = main.determine_rain_likelihood(highest_prob)

    # Publish to SNS
    sns = boto3.client('sns')
    topic_arn = os.environ["SNS_TOPIC_ARN"]
    sns.publish(TopicArn=topic_arn, Message=message)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
