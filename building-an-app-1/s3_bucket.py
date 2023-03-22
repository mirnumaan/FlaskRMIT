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
            access_key="ASIAR44X363U7GP2W6MF"
            secret_key="H//ASuVFAF7dCWneTWYTHqgLbQ+YkHWb8CgA/75c"   
            aws_session_token="FwoGZXIvYXdzEOD//////////wEaDACcm2AmwJfjDGNsCCLNAUftifEzGGZZCBOOXm153gojkQ8bV/wOpS32PwHv2H6/9mixmYSSjFZyqft1AhDav5nLsvgzT6MdmDPI9sWB4Z5VS3q9ztabbXgeH6XnGN/GbyWB7yaVwQjyBRGgyn0uNnP1me7Y7Rti89EX5ZvDLLROkIUuh1qocJVqn+r3mCGU7bgSX68xsbW6O6fB+ZyFgIF0RMnQbcn5a/JI3yMAcv4w9Z9KUNypSXS6NRwbEJpdk0yaKVPhuRyOlmw2RJKvVaOc5rA5xc185YGFzZsoguDooAYyLc+KRKs8NrVg6X5jo4i+VzvT0xNWH87+pQUxvqVluzxbSNTL9VJPSLN9fzcbLw=="
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
