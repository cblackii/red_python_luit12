import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='NBAs All Time Leading Scorers',
    KeySchema=[
        {
            'AttributeName': 'Player',
            'KeyType': 'HASH' #Partition Key
        },
        {
            'AttributeName': 'Points',
            'KeyType': 'RANGE' #Sort Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Player',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Points',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)