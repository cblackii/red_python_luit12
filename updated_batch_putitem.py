import boto3

#replace the keys below

dynamodb = boto3.resource('dynamodb')

#Put Item # Batch Writing

table = dynamodb.Table('NBAs_All_Time_Leading_Scorers') #variable to hold table name

dynamodb = put_item(
        Item={
            'Player': 'Lebron_James',
            'Points': '38411',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Kareem_Abdual_Jabbar',
            'Points': '38337',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Karl_Malone',
            'Points': '36928',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Kobe_Bryant',
            'Points': '33643',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Michael_Jordan',
            'Points': '32292',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Dirk_Nowitzki',
            'Points': '31560',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Wilt_Chamberlain',
            'Points': '31419',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Shaquille_Oneal',
            'Points': '28596',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Carmelo_Anthony',
            'Points': '28289',
            }
    )
dynamodb.put_item(
        Item={
            'Player': 'Moses_Malone',
            'Points': '27409',
            }
    )
    