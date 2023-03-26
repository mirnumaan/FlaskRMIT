import os
import boto3
import logging
import json
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363U5DXJZZHB"
secret_key="Cv7UQS8C0Dwx+OLUzGuQVEx2DLum+BOvK2G9WKdz"   
aws_session_token="FwoGZXIvYXdzEOr//////////wEaDDV8YKKmx42LsrHivSLNAU2Obkxwb5TYSwPhuhbUI/Ke/c3zrk2Kyaqxm4oLzlyHXcEZDweI/Avw5KqkOVjFyjKnu0IVPCsIHpY5EkqhYSocY3kIbVcNqB1atuQvlJenqNYpN+qZcswRi12KVYXhLVTcr9TC+W1jO2aF6kEBBLcRHxvp4x2j+2DkRWh6HOQt7om6BBcK9/5+4pLcYU/crf6PtwYXT7IMp8CdjJBT/X1DK4jjoyGdPJ/Y/dwQbJKkS0Ywusq90LSD9rL9wAQjP6U1iH+lM7jDQ39FjakojvzqoAYyLcqylorW/AfKc/kGiSmvEbo0IHomcWi0KUaMZtl40DsVPoktoWHL4+oEBuZfng=="
region = 'us-east-1'

s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region)
json_object = 'a1.json'
s3.put_object(
     Body=json.dumps(json_object),
     Bucket='halayolay006',
     Key= access_key
)