import base64
import boto3 
import os

def img_extract():
    access_key="ASIAR44X363UZTA4ZM5O"
    secret_key="SRIwwegDfpm+ZWtXGWISyMHzLXxr1sj3CclfVFcE"   
    aws_session_token="FwoGZXIvYXdzEDIaDH1274xTvgiQC6v4KiLNAchX+sWnwsr5/RkSyrFk67RUqeIOOu/Mcjm64Hii4ypM5rasc5iZc1IHUacz9huoWKPEzSN0Iz5S3AHaumGbBgWiVPtzV2O1A7Lv3bjCxH+qEPcYzGFEFbcO1uoXb18/Dr5RMQfRqazjZdHTTThdUZPZodhp4BlpVg+sUEI3dlH7jgXv9BDXkgWOD52dW7F92AY46JLwz++ZkCREMAnrTqCbivfU8isw5uUTeEOnJ/QgDLsm2K/lmT6v5na8EezyRCUPnDD+p2/8yVXxeDgogP+yoQYyLfC2aHg8N07nNkZ9diJR4jvK36OZYrWfmPZUoraeYDb+/FK6N0kKS1cEEZzCeA=="    
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