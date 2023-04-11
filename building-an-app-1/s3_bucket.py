# from flask import Flask,render_template, request, redirect, session
import boto3
import logging
from botocore.exceptions import ClientError 

region_name = 'us-east-1'
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            access_key="ASIAR44X363UZVQQ7R5S"
            secret_key="GpV9Ob/gM/brvIEck+JpVA+p/6ICr5MzQrLg68It"   
            aws_session_token="FwoGZXIvYXdzEM3//////////wEaDD9jNcPWY2uje0seCyLNARg8f+tXfzbm/V8/AaNIVWACyLOww4RaS/gfqI8gwRmDSuK/uXdYT1jTNzQ61hmNzMfPQnAtg54KKiR5xq5ALV+89S36tWcF949ED8n4v0h8FbVL9lUP6SRFLk1WevGTS9bBV9gcZ+9Rv+96bV3v51pmI10LPaC2y9su2aW2bDFAl2PWJ7VVdyy3fIF2BwC67sNwlcHfEHsE9v/tKLnqrzmpvrZKQcCI3TO1dWTY7T1TOUhMqLJLtaB6/fzqE2Tx+abzOQLnXXMDZdr4RA0o64nVoQYyLVNmPiMZaV9JwLBFX7Bqz3NTmNHl80wK8mOLy7bR+8jn/v30++F1yT+GyTl0Fw=="

            s3_client = boto3.client('s3', 
                                     aws_access_key_id=access_key,
                                     aws_secret_access_key=secret_key,
                                     aws_session_token = aws_session_token,region_name=region)
            
            s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error("Error: ", e)
        return False
    return True

if __name__ == '__main__':
    # AWS Credentials
    create_bucket('halayolay006', region=region_name)
