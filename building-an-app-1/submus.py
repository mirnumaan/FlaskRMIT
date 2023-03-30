import boto3

def add_music(title, tn):

    access_key="ASIAR44X363USCC7RX76"
    secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"   
    aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="    
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
    
