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
                  # Sort key
                    
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
    access_key="ASIAR44X363UVPZBBTGD"
    secret_key="o/B3mFs0RRc7nydos/XED7vBn0sE4VxLj6NrX2K/"   
    aws_session_token="FwoGZXIvYXdzEF8aDNHO3qF+F6//hxD5/yLNAeCiIawRpxf8B5eeaygSQd8VV7A5Cobo+9Cb/hWvJYT1uefDLlr41gKjPVInl3ULF0w7RvTgksJc2K9lxX/DSV6bXazpTy6Cbzp3W/89lLl22wJvvZpmZjRP6vhQmELDaQeKExrKHcg5lHy16tgepsALTAkL32bHQL86fN4gWaH4xC1jRcThCMpO6kFkrbefu1a/CD6V7dj4ADdOu/dtqus1dUHwC0uJT+QzNzMOt4lNalATEdAPjzcgEVdO49yw0hEmbJJP4ZLTcGT7gncoqeKEoQYyLcI9IuFMHtUrB91QoJ0tJ/P5ITG9UabjTgqcAsd84IUYHNqEPyUvWnBTlOjYrg=="
    region_name = 'us-east-1'

    # DynamoDB Client
    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)

    
    m = Music(dyn_resource=dynamodb)
    m.create_table('music223')


    
