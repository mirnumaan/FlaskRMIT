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
            access_key="ASIAR44X363UZGOLAV4Z"
            secret_key="Jh/leSoYUB/ZRiEdlC/1y9sschbua2ZUqzUr0/CQ"   
            aws_session_token="FwoGZXIvYXdzEMX//////////wEaDBQ2t6iUUIljnh7edCLNAUb6/mWKXBopKaeVn53/KrzV4b1xI7Msx3OHFJj++9vyfeDdPge7V+F5yiHW9Ecb0NISd/oqqX/AiKr4b+8c0r5AGviCSl2nmaTGGdJBDen4p+ysRaFSvWUvbK2EF5o94MuChvIUFE4LSMZwB3G3HsI0KkFIotE9CF4WPG5V9KnwK6WBiG6cXbfTWA6RZ3+FRnRragcMlu7H6IGRv6mxNat9KJMFdiNMKncp9lwoNKkhlQn0tNH3ATXnDbi3aic/a3dmKZPZaVGJ8JwLZqUowa3ToQYyLZl/MeDqYaTM/ryDIJG7DQ3choME4sg8+hMmamZPQSnbohk7aqHECy+njd8vrw=="

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
