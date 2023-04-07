import base64
import boto3 
import os

def img_extract():
    access_key="ASIAR44X363UZ233ZJ4A"
    secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
    aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="
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