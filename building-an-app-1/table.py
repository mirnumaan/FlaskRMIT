# from flask import Flask,render_template, request, redirect, session
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
    access_key="ASIAR44X363U7GP2W6MF"
    secret_key="H//ASuVFAF7dCWneTWYTHqgLbQ+YkHWb8CgA/75c"   
    aws_session_token="FwoGZXIvYXdzEOD//////////wEaDACcm2AmwJfjDGNsCCLNAUftifEzGGZZCBOOXm153gojkQ8bV/wOpS32PwHv2H6/9mixmYSSjFZyqft1AhDav5nLsvgzT6MdmDPI9sWB4Z5VS3q9ztabbXgeH6XnGN/GbyWB7yaVwQjyBRGgyn0uNnP1me7Y7Rti89EX5ZvDLLROkIUuh1qocJVqn+r3mCGU7bgSX68xsbW6O6fB+ZyFgIF0RMnQbcn5a/JI3yMAcv4w9Z9KUNypSXS6NRwbEJpdk0yaKVPhuRyOlmw2RJKvVaOc5rA5xc185YGFzZsoguDooAYyLc+KRKs8NrVg6X5jo4i+VzvT0xNWH87+pQUxvqVluzxbSNTL9VJPSLN9fzcbLw=="
    region_name = 'us-east-1'
    

    # DynamoDB Client
    dynamodb = boto3.resource('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)
    
    mov = Movies(dyn_resource=dynamodb)
    mov.create_table('hello_world')
    
