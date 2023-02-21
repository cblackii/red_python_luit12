import boto3

AWS_REGION = 'us-west-2'

sqs_client = boto3.client("sqs", region_name=AWS_REGION)

