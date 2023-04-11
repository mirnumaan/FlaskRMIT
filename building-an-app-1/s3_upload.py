import os
import boto3
import logging
import json
import requests
from io import BytesIO
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363UZVQQ7R5S"
secret_key="GpV9Ob/gM/brvIEck+JpVA+p/6ICr5MzQrLg68It"   
aws_session_token="FwoGZXIvYXdzEM3//////////wEaDD9jNcPWY2uje0seCyLNARg8f+tXfzbm/V8/AaNIVWACyLOww4RaS/gfqI8gwRmDSuK/uXdYT1jTNzQ61hmNzMfPQnAtg54KKiR5xq5ALV+89S36tWcF949ED8n4v0h8FbVL9lUP6SRFLk1WevGTS9bBV9gcZ+9Rv+96bV3v51pmI10LPaC2y9su2aW2bDFAl2PWJ7VVdyy3fIF2BwC67sNwlcHfEHsE9v/tKLnqrzmpvrZKQcCI3TO1dWTY7T1TOUhMqLJLtaB6/fzqE2Tx+abzOQLnXXMDZdr4RA0o64nVoQYyLVNmPiMZaV9JwLBFX7Bqz3NTmNHl80wK8mOLy7bR+8jn/v30++F1yT+GyTl0Fw=="
region_name = 'us-east-1'

s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region_name)

# Open JSON file containing image URLs
with open('a1.json', 'r') as f:
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

