import boto3

def add_music(title, tn):

    access_key="ASIAR44X363UZGOLAV4Z"
    secret_key="Jh/leSoYUB/ZRiEdlC/1y9sschbua2ZUqzUr0/CQ"   
    aws_session_token="FwoGZXIvYXdzEMX//////////wEaDBQ2t6iUUIljnh7edCLNAUb6/mWKXBopKaeVn53/KrzV4b1xI7Msx3OHFJj++9vyfeDdPge7V+F5yiHW9Ecb0NISd/oqqX/AiKr4b+8c0r5AGviCSl2nmaTGGdJBDen4p+ysRaFSvWUvbK2EF5o94MuChvIUFE4LSMZwB3G3HsI0KkFIotE9CF4WPG5V9KnwK6WBiG6cXbfTWA6RZ3+FRnRragcMlu7H6IGRv6mxNat9KJMFdiNMKncp9lwoNKkhlQn0tNH3ATXnDbi3aic/a3dmKZPZaVGJ8JwLZqUowa3ToQYyLZl/MeDqYaTM/ryDIJG7DQ3choME4sg8+hMmamZPQSnbohk7aqHECy+njd8vrw=="
    region_name = 'us-east-1'
    table_name = 'music'
    # DynamoDB Client
    dynamodb = boto3.client('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)
    table_name="music"
    
    key = {'title':{'S':title}}
    print(key)
    resp = dynamodb.get_item(TableName=table_name,Key=key)
    table_name=tn
    print(key)
    print(resp)
    dynamodb.put_item(TableName= table_name, Item= resp['Item'])
    
