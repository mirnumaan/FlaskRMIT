import boto3

def add_music(title, tn):

    access_key="ASIAR44X363UW6OAES2O"
    secret_key="KYf2o2r3j321+gwqyG2HgWu/AdtEr6iQwuBJrLo/"   
    aws_session_token="FwoGZXIvYXdzEGMaDBKtq1gDMQHkXTUSHyLNAXjJD0OMzfVUJe/yngJkjahyk0MANEaRGaPW52wqZHhYaqMFwvoS1eZj3LJi0dlcdVwK83COHVqiAUPW6c1VAzQGn76DO9vADb8xHynU+/wYyWPsjzFqT/4mzzYLypcTTtjjt14Yhmza0ovpfrnsrZTUTKIup43Vwfx75qHKX5MOXQtwO4Rq+NyPbK1gKMagqPbLBLzIeZjb8O+IcmGj3uKF8/P8p29wgBbxip2dKcVcFz37iIZ7hz60dRPjJeetKai9etrWnC6vK3eOdQko6++9oQYyLb/fBb86xK5/uojOKddlSrh3zWAAZPtdEs5cV5c3OdFtYwdNKtpGAOCYYepqUA=="
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
    
