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
            access_key="ASIAR44X363UZTA4ZM5O"
            secret_key="SRIwwegDfpm+ZWtXGWISyMHzLXxr1sj3CclfVFcE"   
            aws_session_token="FwoGZXIvYXdzEDIaDH1274xTvgiQC6v4KiLNAchX+sWnwsr5/RkSyrFk67RUqeIOOu/Mcjm64Hii4ypM5rasc5iZc1IHUacz9huoWKPEzSN0Iz5S3AHaumGbBgWiVPtzV2O1A7Lv3bjCxH+qEPcYzGFEFbcO1uoXb18/Dr5RMQfRqazjZdHTTThdUZPZodhp4BlpVg+sUEI3dlH7jgXv9BDXkgWOD52dW7F92AY46JLwz++ZkCREMAnrTqCbivfU8isw5uUTeEOnJ/QgDLsm2K/lmT6v5na8EezyRCUPnDD+p2/8yVXxeDgogP+yoQYyLfC2aHg8N07nNkZ9diJR4jvK36OZYrWfmPZUoraeYDb+/FK6N0kKS1cEEZzCeA=="    
            # region_name = 'us-east-1'
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
