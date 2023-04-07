import os
import boto3
import logging
import json
import requests
from io import BytesIO
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363UW6OAES2O"
secret_key="KYf2o2r3j321+gwqyG2HgWu/AdtEr6iQwuBJrLo/"   
aws_session_token="FwoGZXIvYXdzEGMaDBKtq1gDMQHkXTUSHyLNAXjJD0OMzfVUJe/yngJkjahyk0MANEaRGaPW52wqZHhYaqMFwvoS1eZj3LJi0dlcdVwK83COHVqiAUPW6c1VAzQGn76DO9vADb8xHynU+/wYyWPsjzFqT/4mzzYLypcTTtjjt14Yhmza0ovpfrnsrZTUTKIup43Vwfx75qHKX5MOXQtwO4Rq+NyPbK1gKMagqPbLBLzIeZjb8O+IcmGj3uKF8/P8p29wgBbxip2dKcVcFz37iIZ7hz60dRPjJeetKai9etrWnC6vK3eOdQko6++9oQYyLb/fBb86xK5/uojOKddlSrh3zWAAZPtdEs5cV5c3OdFtYwdNKtpGAOCYYepqUA=="
region_name = 'us-east-1'

s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region_name)

# Open JSON file containing image URLs
with open('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json', 'r') as f:
    data = json.load(f)
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

