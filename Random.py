import json
import boto3

from datetime import datetime, timezone

def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    local_time = datetime.now(timezone.utc)
    queue = sqs.Queue(url='string')
    
    queue.send_message(MessageBody=str(local_time))
    
    return {
        'statusCode': 200,
        'body': json.dumps(local_time, default = str)
    }