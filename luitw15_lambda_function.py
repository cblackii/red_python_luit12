import json
import boto3
import random

def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')

    response = sqs.send_message(
        QueueUrl='https://sqs.us-west-2.amazonaws.com/542986597955/luitw15-queue',
        MessageBody=str(random.randint(0,100000))
    )

    # TODO implement
    return {
            'statusCode': 200,
            'body': json.dumps("Hello from Lambda!')
        } 