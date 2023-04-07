import base64
import boto3 
import os

def img_extract():
    access_key="ASIAR44X363UW6OAES2O"
    secret_key="KYf2o2r3j321+gwqyG2HgWu/AdtEr6iQwuBJrLo/"   
    aws_session_token="FwoGZXIvYXdzEGMaDBKtq1gDMQHkXTUSHyLNAXjJD0OMzfVUJe/yngJkjahyk0MANEaRGaPW52wqZHhYaqMFwvoS1eZj3LJi0dlcdVwK83COHVqiAUPW6c1VAzQGn76DO9vADb8xHynU+/wYyWPsjzFqT/4mzzYLypcTTtjjt14Yhmza0ovpfrnsrZTUTKIup43Vwfx75qHKX5MOXQtwO4Rq+NyPbK1gKMagqPbLBLzIeZjb8O+IcmGj3uKF8/P8p29wgBbxip2dKcVcFz37iIZ7hz60dRPjJeetKai9etrWnC6vK3eOdQko6++9oQYyLb/fBb86xK5/uojOKddlSrh3zWAAZPtdEs5cV5c3OdFtYwdNKtpGAOCYYepqUA=="
    region_name= 'us-east-1'
    table_name = 'login'
    my_bucket = 'halayolay006'

    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)

    s3 = boto3.resource('s3',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key,
                        aws_session_token = aws_session_token,
                        region_name=region_name) 


    bucket = s3.Bucket(my_bucket)

    objs = bucket.objects.all()

    file={}

    for obj in objs:
        key =obj.key
        # print(key)
        if key.endswith(".jpg"):
            body = obj.get()['Body'].read()
            body = base64.b64encode(body).decode('UTF-8')
            file[key] = body
        
    return file