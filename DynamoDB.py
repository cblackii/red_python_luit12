#DynamoDB example

import boto3

#replace the keys below

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_keyid=''
    aws_secret_access_key='',
    )