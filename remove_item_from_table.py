import boto3

dynamodb = boto3.resource("dynamodb")
table= dynamodb.Table("NBAs_All_Time_Leading_Scorers")
response=table.delete_item(
    Key={
        'Player': 'Moses_Malone', #item to be removed
        'Points': 27409
        
    }
)

print(response)