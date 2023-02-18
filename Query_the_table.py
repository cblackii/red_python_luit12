import boto3

from boto3.dynamodb.conditions import key

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('NBAs_All_Time_Leading_Scorers')


response = table.query(
    KeyConditionExpression=Key('Username').eq('Moses_Malone'))
items = response['Items']

print(response["Items"])

