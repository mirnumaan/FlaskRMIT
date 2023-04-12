import boto3

def search_music(title, artist, year):

    access_key="ASIAR44X363U7ORN4XHS"
    secret_key="l2St4RhkiXqMDdA1TAjevEZyur4cTJtS8syj7zDD"   
    aws_session_token="FwoGZXIvYXdzENv//////////wEaDNZqBWjstBatxazjPSLNAbm9BL8be6H/3GWdCN7QJabcSzMdqRotB9dVf8EjWyjNCpTxaQEtQ1V8b9ZSL26ga6+azu/zEqMpr1jkeyPv8l+jQccsc4LR5VjIX86WDTIW1fVUroHRvXr2MBcr9+VdPCotN1XFUzZmFQ/ijJCk9xHcfsVTnZta+L8rV2usuAPHmnmLuyOFN2PdN1PdVJ0Eew4RXcvNYZTbnJHT/g6DIONuYvKVDsql5qHPcm4jOTPGbuw+wv4GqQO4oMw4W4iex+UTsRd+meAjh78ZH8ooo5jYoQYyLWjFhIBR5CuqfIy9ixk6Y5/libuC6Kha057CkDhmQE4NbV7Pz2HwX1DCFtPJ8g=="    
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