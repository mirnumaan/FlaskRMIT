import boto3

def add_music(title, tn):

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
    table_name="music"
    
    key = {'title':{'S':title}}
    print(key)
    resp = dynamodb.get_item(TableName=table_name,Key=key)
    table_name=tn
    print(key)
    print(resp)
    dynamodb.put_item(TableName= table_name, Item= resp['Item'])
    
