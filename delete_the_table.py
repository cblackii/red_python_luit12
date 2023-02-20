import boto3

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table("NBAs_All_Time_Leading_Scorers")
response=table.delete()

print(response)
