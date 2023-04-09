import boto3

def search_music(title, artist, year):

    access_key="ASIAR44X363URR37THFF"
    secret_key="7GUCBueYGoPHAT4zm5+pcYLYAe1JIlWLBJZl8snC"   
    aws_session_token="FwoGZXIvYXdzEJL//////////wEaDNhian9QwAP+LLiG+iLNAfdcErPRtqoVcARPqkzgpXetDUaNgDi8rPMV9+KUoYLE+YM1fa3RLp6h16Kb978IWJLfQBiUjmgEoSrDnGs0IrdaRalrPZ00pjcYS39ovmRZb4fKKhDHrrHhvVajjFtvcvMMd985qrLGZsZShQ+A7LoD0OL40IIv0BzDs/i8l4+t5NBY0mFgRKvGiDOHG94gXOTYzZtsTxS9u9tmDND5/V0DwdDZVC98qXi77mVd5AF6XcRZdA4wG7q0aDi31Xg/tCboEuuriDG0E/DSiVUo5ZbIoQYyLRpSSfdzW5kMvO89BVjrNIZGvym0EZumxf/4L/WzFaX7Nq7/24X5eXnqvV0TTg=="
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