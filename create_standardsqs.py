#Create Standard SQS Queue using Python

import boto3

sqs = boto3.client('sqs')
response = sqs.create_queue(
    QueueName= 'luitw15-queue',
)

print(response)