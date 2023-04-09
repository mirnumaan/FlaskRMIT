# from flask import Flask,render_template, request, redirect, session
import boto3
import json
import logging
from botocore.exceptions import ClientError 

class Music:
    """Encapsulates an Amazon DynamoDB table of movie data."""
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        self.table = None

    def create_table(self, table_name):
        logger = logging.getLogger(__name__)
        """
        Creates an Amazon DynamoDB table that can be used to store movie data.
        The table uses the release year of the movie as the partition key and the
        title as the sort key.
        :param table_name: The name of the table to create.
        :return: The newly created table.
        """
        try:
            self.table = self.dyn_resource.create_table(
                TableName=table_name,
                KeySchema=[
                    {'AttributeName': 'title', 'KeyType': 'HASH'}  # Partition key
                 
                    
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'title', 'AttributeType': 'S'}
                    
                    
                ],
                ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10})
            self.table.wait_until_exists()
        except ClientError as err:
            logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
        else:
            return self.table
        


if __name__ == '__main__':
    # AWS Credentials
    access_key="ASIAR44X363URR37THFF"
    secret_key="7GUCBueYGoPHAT4zm5+pcYLYAe1JIlWLBJZl8snC"   
    aws_session_token="FwoGZXIvYXdzEJL//////////wEaDNhian9QwAP+LLiG+iLNAfdcErPRtqoVcARPqkzgpXetDUaNgDi8rPMV9+KUoYLE+YM1fa3RLp6h16Kb978IWJLfQBiUjmgEoSrDnGs0IrdaRalrPZ00pjcYS39ovmRZb4fKKhDHrrHhvVajjFtvcvMMd985qrLGZsZShQ+A7LoD0OL40IIv0BzDs/i8l4+t5NBY0mFgRKvGiDOHG94gXOTYzZtsTxS9u9tmDND5/V0DwdDZVC98qXi77mVd5AF6XcRZdA4wG7q0aDi31Xg/tCboEuuriDG0E/DSiVUo5ZbIoQYyLRpSSfdzW5kMvO89BVjrNIZGvym0EZumxf/4L/WzFaX7Nq7/24X5eXnqvV0TTg=="
    region_name = 'us-east-1'

    # DynamoDB Client
    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)

    
    m = Music(dyn_resource=dynamodb)
    tab = ['numaan0', 'numaan1', 'numaan2', 'numaan3', 'numaan4', 'numaan5', 'numaan6', 'numaan7', 'numaan8', 'numaan9', 'music']
    for x in tab:
        print(x)
        m.create_table(x)


    
