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
            access_key="ASIAR44X363UW6OAES2O"
            secret_key="KYf2o2r3j321+gwqyG2HgWu/AdtEr6iQwuBJrLo/"   
            aws_session_token="FwoGZXIvYXdzEGMaDBKtq1gDMQHkXTUSHyLNAXjJD0OMzfVUJe/yngJkjahyk0MANEaRGaPW52wqZHhYaqMFwvoS1eZj3LJi0dlcdVwK83COHVqiAUPW6c1VAzQGn76DO9vADb8xHynU+/wYyWPsjzFqT/4mzzYLypcTTtjjt14Yhmza0ovpfrnsrZTUTKIup43Vwfx75qHKX5MOXQtwO4Rq+NyPbK1gKMagqPbLBLzIeZjb8O+IcmGj3uKF8/P8p29wgBbxip2dKcVcFz37iIZ7hz60dRPjJeetKai9etrWnC6vK3eOdQko6++9oQYyLb/fBb86xK5/uojOKddlSrh3zWAAZPtdEs5cV5c3OdFtYwdNKtpGAOCYYepqUA=="
            
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
