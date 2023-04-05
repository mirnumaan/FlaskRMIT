import boto3

def search_music(title, artist, year):

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
    if title !=  None and artist ==  None and year ==  None:
        # define the query parameters
        expression = 'title = :title'
        expression_values = {':title': {'S': title}}

        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,
            ExpressionAttributeValues=expression_values
        )
    elif title ==  None and artist !=  None and year ==  None:
        expression = 'artist = :artist'
        expression_values = {':artist': {'S': artist}}

        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,
            ExpressionAttributeValues=expression_values

        )
    elif title ==  None and artist ==  None and year !=  None:
        key = {':yyyy':{'S':year}}
        expression = '#yr = :yyyy'
        expression_values = key
        # yr = :yyyy
        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,
            ExpressionAttributeNames={'#yr': 'year'},
            ExpressionAttributeValues=expression_values

        )
    elif title !=  None and artist ==  None and year !=  None:
        key = {':title': {'S': title},':yyyy':{'S':year}}
        expression = 'title = :title and #yr = :yyyy'
        expression_values = key
        # yr = :yyyy
        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,
            ExpressionAttributeNames={'#yr': 'year'},
            ExpressionAttributeValues=expression_values

        )
    elif title ==  None and artist !=  None and year !=  None:
        key = {':artist': {'S': artist},':yyyy':{'S':year}}
        expression = 'artist = :artist and #yr = :yyyy'
        expression_values = key
        # yr = :yyyy
        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,
            ExpressionAttributeNames={'#yr': 'year'},
            ExpressionAttributeValues=expression_values

        )
    elif title !=  None and artist !=  None and year ==  None:
        key = {':title': {'S': title},
                ':artist': {'S': artist}}
        expression = 'title = :title and artist = :artist'
        expression_values = key
        # execute the query
        response = dynamodb.scan(
            TableName=table_name,

            FilterExpression=expression,

            ExpressionAttributeValues=expression_values
        )
    elif title !=  None and artist !=  None and year !=  None:
        key = {':title': {'S': title},
                ':artist': {'S': artist},
                ':yyyy':{'S':year}}
        expression = 'title = :title and artist = :artist and #yr = year'
        expression_values = key
        # execute the query
        response = dynamodb.scan(
            TableName=table_name,
            ExpressionAttributeNames={'#yr': 'year'},
            FilterExpression=expression,
            ExpressionAttributeValues=expression_values
        )
    else:
        return  None
    print(response["Items"])
    return response 