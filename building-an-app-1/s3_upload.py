import os
import boto3
import logging
import json
import requests
from io import BytesIO
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363U7ORN4XHS"
secret_key="l2St4RhkiXqMDdA1TAjevEZyur4cTJtS8syj7zDD"   
aws_session_token="FwoGZXIvYXdzENv//////////wEaDNZqBWjstBatxazjPSLNAbm9BL8be6H/3GWdCN7QJabcSzMdqRotB9dVf8EjWyjNCpTxaQEtQ1V8b9ZSL26ga6+azu/zEqMpr1jkeyPv8l+jQccsc4LR5VjIX86WDTIW1fVUroHRvXr2MBcr9+VdPCotN1XFUzZmFQ/ijJCk9xHcfsVTnZta+L8rV2usuAPHmnmLuyOFN2PdN1PdVJ0Eew4RXcvNYZTbnJHT/g6DIONuYvKVDsql5qHPcm4jOTPGbuw+wv4GqQO4oMw4W4iex+UTsRd+meAjh78ZH8ooo5jYoQYyLWjFhIBR5CuqfIy9ixk6Y5/libuC6Kha057CkDhmQE4NbV7Pz2HwX1DCFtPJ8g=="
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

