import boto3

def add_music(title, tn):

    access_key="ASIAR44X363UZTA4ZM5O"
    secret_key="SRIwwegDfpm+ZWtXGWISyMHzLXxr1sj3CclfVFcE"   
    aws_session_token="FwoGZXIvYXdzEDIaDH1274xTvgiQC6v4KiLNAchX+sWnwsr5/RkSyrFk67RUqeIOOu/Mcjm64Hii4ypM5rasc5iZc1IHUacz9huoWKPEzSN0Iz5S3AHaumGbBgWiVPtzV2O1A7Lv3bjCxH+qEPcYzGFEFbcO1uoXb18/Dr5RMQfRqazjZdHTTThdUZPZodhp4BlpVg+sUEI3dlH7jgXv9BDXkgWOD52dW7F92AY46JLwz++ZkCREMAnrTqCbivfU8isw5uUTeEOnJ/QgDLsm2K/lmT6v5na8EezyRCUPnDD+p2/8yVXxeDgogP+yoQYyLfC2aHg8N07nNkZ9diJR4jvK36OZYrWfmPZUoraeYDb+/FK6N0kKS1cEEZzCeA=="    
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
    
