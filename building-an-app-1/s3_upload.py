import os
import boto3
import logging
import json
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363USCC7RX76"
secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"   
aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="    
region_name = 'us-east-1'

s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region_name)

import json
import boto3
import requests
from io import BytesIO


# Open JSON file containing image URLs
with open('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json', 'r') as f:
    data = json.load(f)
# img_url = "S"
# Loop through each item in the JSON file
for item in data['songs']:
    # Get the image URL
    img_url = item['img_url']
    # Download the image data from the URL
    response = requests.get(img_url)
    # Open a BytesIO stream to store the image data
    img_data = BytesIO(response.content)
    # Get the artist name to use as the S3 object key
    artist = item['title']
    # Upload the image to S3
    s3.upload_fileobj(img_data, 'halayolay006', f'{artist}.jpg')

