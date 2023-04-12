import base64
import boto3 
import os

def img_extract():
    access_key="ASIAR44X363U7ORN4XHS"
    secret_key="l2St4RhkiXqMDdA1TAjevEZyur4cTJtS8syj7zDD"   
    aws_session_token="FwoGZXIvYXdzENv//////////wEaDNZqBWjstBatxazjPSLNAbm9BL8be6H/3GWdCN7QJabcSzMdqRotB9dVf8EjWyjNCpTxaQEtQ1V8b9ZSL26ga6+azu/zEqMpr1jkeyPv8l+jQccsc4LR5VjIX86WDTIW1fVUroHRvXr2MBcr9+VdPCotN1XFUzZmFQ/ijJCk9xHcfsVTnZta+L8rV2usuAPHmnmLuyOFN2PdN1PdVJ0Eew4RXcvNYZTbnJHT/g6DIONuYvKVDsql5qHPcm4jOTPGbuw+wv4GqQO4oMw4W4iex+UTsRd+meAjh78ZH8ooo5jYoQYyLWjFhIBR5CuqfIy9ixk6Y5/libuC6Kha057CkDhmQE4NbV7Pz2HwX1DCFtPJ8g=="
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