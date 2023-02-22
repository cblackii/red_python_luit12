import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    time_date = now.strftime("%H-%M-%S %m:%d:%y")
    
    sqs = boto3.client('sqs')
    response = sqs.send_message(
    QueueUrl= "https://sqs.us-west-2.amazonaws.com/542986597955/updated_luitw15_queue",
    MessageBody= 'date_time',
)
    return {
        'statusCode': 200,
        'body': json.dumps('time_date')
    }