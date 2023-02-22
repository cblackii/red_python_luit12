import boto3

sqs = boto3.resource('sqs', region_name = 'us-west-2')

queue = sqs.create_queue(
    QueueName='updated_luitw15_queue',
    Attributes={'DelaySeconds': '5', 'VisibilityTimeout': '60'})
    
print(queue.url)