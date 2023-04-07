import boto3

def search_music(title, artist, year):

    access_key="ASIAR44X363UZ233ZJ4A"
    secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
    aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="
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