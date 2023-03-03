import boto3

sqs = boto3.client('sqs')

response = sqs.send_message(
    QueueUrl='https://sqs.us-west-2.amazonaws.com/542986597955/luitw15-queue',
    MessageBody='Message sent from Python <3'
    
)

print("Message sent")