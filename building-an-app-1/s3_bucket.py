from flask import Flask,render_template, request, redirect, session
import boto3
import logging
from botocore.exceptions import ClientError 



def create_bucket(bucket_name, region = 'us-east-1'):
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
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == '__main__':
    # AWS Credentials
    access_key="ASIAR44X363U5N2K53VF"
    secret_key="QTFe3YejAiB+3IKtASnsbCWW2LRJ6szMV1HPOOhC"
    aws_session_token="FwoGZXIvYXdzEM///////////wEaDM+dqQAQc/h3MhlPHyLNAVz0nCbwldv+O7MuhzKMubVA470+ttrGLmfKhBPay2drmZH5bEijT0yGL/zslPKtLYV0ICgsQwVa5FtMxlKjlVZRyUS0V3y5ELJz3LsAvq8IpC+APSUFzXbYs7GPlaevBwhVb7Th1EN/DRjV5o7cvTED7/q64x6mkpWM2jSkBt1rZ++Qv5vB/R8ESl0/A5kPiFnHshyKx3P5npv9Tt/JnrSYj3V2Wt+4kUr9Sj11pImmQFnpNyl6zLrdVLWwhWcSrndL3YXKy8sWy2XNvp4okYzloAYyLRSQ6eawzuS6zqveuxBBC4ZIH8zvtojV7RSddcYTaj97jOyKFI6/RfN49JSlew=="
    region_name = 'us-east-1'
    table_name = 'login'

    # DynamoDB Client
    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)
    
    create_bucket('hello_world')
