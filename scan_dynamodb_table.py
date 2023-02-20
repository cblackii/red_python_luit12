import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')

table = dynamodb.Table('NBAs_All_Time_Leading_Scorers') 

response = table.scan()

items = response['Items']

for item in items:
    print(item)