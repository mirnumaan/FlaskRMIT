import base64
import boto3 
import os

def img_extract():
    access_key="ASIAR44X363URR37THFF"
    secret_key="7GUCBueYGoPHAT4zm5+pcYLYAe1JIlWLBJZl8snC"   
    aws_session_token="FwoGZXIvYXdzEJL//////////wEaDNhian9QwAP+LLiG+iLNAfdcErPRtqoVcARPqkzgpXetDUaNgDi8rPMV9+KUoYLE+YM1fa3RLp6h16Kb978IWJLfQBiUjmgEoSrDnGs0IrdaRalrPZ00pjcYS39ovmRZb4fKKhDHrrHhvVajjFtvcvMMd985qrLGZsZShQ+A7LoD0OL40IIv0BzDs/i8l4+t5NBY0mFgRKvGiDOHG94gXOTYzZtsTxS9u9tmDND5/V0DwdDZVC98qXi77mVd5AF6XcRZdA4wG7q0aDi31Xg/tCboEuuriDG0E/DSiVUo5ZbIoQYyLRpSSfdzW5kMvO89BVjrNIZGvym0EZumxf/4L/WzFaX7Nq7/24X5eXnqvV0TTg=="
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