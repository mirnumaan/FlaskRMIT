import os 
import boto3

def delete_music(id_music,tn):

    access_key="ASIAR44X363UZVQQ7R5S"
    secret_key="GpV9Ob/gM/brvIEck+JpVA+p/6ICr5MzQrLg68It"   
    aws_session_token="FwoGZXIvYXdzEM3//////////wEaDD9jNcPWY2uje0seCyLNARg8f+tXfzbm/V8/AaNIVWACyLOww4RaS/gfqI8gwRmDSuK/uXdYT1jTNzQ61hmNzMfPQnAtg54KKiR5xq5ALV+89S36tWcF949ED8n4v0h8FbVL9lUP6SRFLk1WevGTS9bBV9gcZ+9Rv+96bV3v51pmI10LPaC2y9su2aW2bDFAl2PWJ7VVdyy3fIF2BwC67sNwlcHfEHsE9v/tKLnqrzmpvrZKQcCI3TO1dWTY7T1TOUhMqLJLtaB6/fzqE2Tx+abzOQLnXXMDZdr4RA0o64nVoQYyLVNmPiMZaV9JwLBFX7Bqz3NTmNHl80wK8mOLy7bR+8jn/v30++F1yT+GyTl0Fw=="

    region_name= 'us-east-1'

    dynamodb = boto3.client('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)
    
    table_name=tn

    key = {"title":{"S": id_music}}

    print(dynamodb.delete_item(TableName=table_name, Key = key))
