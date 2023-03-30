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
    access_key="ASIAR44X363USCC7RX76"
    secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"   
    aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="    
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


    
