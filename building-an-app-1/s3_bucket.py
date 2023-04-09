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
            access_key="ASIAR44X363URR37THFF"
            secret_key="7GUCBueYGoPHAT4zm5+pcYLYAe1JIlWLBJZl8snC"   
            aws_session_token="FwoGZXIvYXdzEJL//////////wEaDNhian9QwAP+LLiG+iLNAfdcErPRtqoVcARPqkzgpXetDUaNgDi8rPMV9+KUoYLE+YM1fa3RLp6h16Kb978IWJLfQBiUjmgEoSrDnGs0IrdaRalrPZ00pjcYS39ovmRZb4fKKhDHrrHhvVajjFtvcvMMd985qrLGZsZShQ+A7LoD0OL40IIv0BzDs/i8l4+t5NBY0mFgRKvGiDOHG94gXOTYzZtsTxS9u9tmDND5/V0DwdDZVC98qXi77mVd5AF6XcRZdA4wG7q0aDi31Xg/tCboEuuriDG0E/DSiVUo5ZbIoQYyLRpSSfdzW5kMvO89BVjrNIZGvym0EZumxf/4L/WzFaX7Nq7/24X5eXnqvV0TTg=="

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
