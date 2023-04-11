import os
import boto3
import logging
import json
import requests
from io import BytesIO
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363UZGOLAV4Z"
secret_key="Jh/leSoYUB/ZRiEdlC/1y9sschbua2ZUqzUr0/CQ"   
aws_session_token="FwoGZXIvYXdzEMX//////////wEaDBQ2t6iUUIljnh7edCLNAUb6/mWKXBopKaeVn53/KrzV4b1xI7Msx3OHFJj++9vyfeDdPge7V+F5yiHW9Ecb0NISd/oqqX/AiKr4b+8c0r5AGviCSl2nmaTGGdJBDen4p+ysRaFSvWUvbK2EF5o94MuChvIUFE4LSMZwB3G3HsI0KkFIotE9CF4WPG5V9KnwK6WBiG6cXbfTWA6RZ3+FRnRragcMlu7H6IGRv6mxNat9KJMFdiNMKncp9lwoNKkhlQn0tNH3ATXnDbi3aic/a3dmKZPZaVGJ8JwLZqUowa3ToQYyLZl/MeDqYaTM/ryDIJG7DQ3choME4sg8+hMmamZPQSnbohk7aqHECy+njd8vrw=="
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

