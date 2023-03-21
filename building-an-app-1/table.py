from flask import Flask, render_template, request, redirect, session
import boto3
import logging
from botocore.exceptions import ClientError 

class Movies:
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
                    {'AttributeName': 'year', 'KeyType': 'HASH'},  # Partition key
                    {'AttributeName': 'title', 'KeyType': 'RANGE'}  # Sort key
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'year', 'AttributeType': 'N'},
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
    
    mov = Movies(dyn_resource=dynamodb)
    mov.create_table('music_code')
