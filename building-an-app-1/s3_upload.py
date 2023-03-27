import os
import boto3
import logging
import json
# from botocore.exceptions import ClientError 
from botocore.exceptions import ClientError 
access_key="ASIAR44X363USX6IG3NO"
secret_key="FIWL5YzIc7xNFhlAD2BU6riP7Y7ltkuB22L92I23"   
aws_session_token="FwoGZXIvYXdzEFoaDEGM63jRMQ0NYyU3eiLNARPjDw6/T28TZrmZbl7Bwc4EUZMhmqEt+hiEkkO3TcbfBJUSmnkF6OLncix/l5lAe0+PyM50UwQXWAFWupCfVVOli4jn8Id+gZNOlXJpta3MC8mzSlCbxruSJ6uYALmmygJTPPwm5BbmWtIwS619jRNGRxWOslEiPWPc3zqanOEjO4mHdJDxYOP4z8Uj5vvgyQZgTH7Anshn/G447jFVVXxxVao0dkQmbW0wXSclGBx1wG0lx2p5M0iIo2s4XTTD3hDWkC3GfR8QJ+Y2QLgo58eDoQYyLVAr77ljbXzfRvQ/m3Vn8k7sTyyb9Z+1V7kfjijl2dOYreoFsH00XRDfpXdXeQ=="
region_name = 'us-east-1'

s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region_name)
# json_object = 'a1.json'
# s3.put_object(
#      Body=json.dumps(json_object),
#      Bucket='halayolay006',
#      Key= access_key
# )

# logger = logging.getLogger(__name__)
# def put_policy(self, policy):
#         """
#         Apply a security policy to the bucket. Policies control users' ability
#         to perform specific actions, such as listing the objects in the bucket.
#         :param policy: The policy to apply to the bucket.
#         """
#         try:
#             self.bucket.Policy().put(Policy=json.dumps(policy))
#             logger.info("Put policy %s for bucket '%s'.", policy, self.bucket.name)
#         except ClientError:
#             logger.exception("Couldn't apply policy to bucket '%s'.", self.bucket.name)
#             raise
        
# put_policy('a1.json')

import json
import boto3
import requests
from io import BytesIO

# # Initialize S3 client
# s3 = boto3.client('s3')

# Open JSON file containing image URLs
with open('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json', 'r') as f:
    data = json.load(f)
# img_url = "S"
# Loop through each item in the JSON file
for item in data['img_url']:
    # Get the image URL
    img_url = item['img_url']
    # Download the image data from the URL
    response = requests.get(img_url)
    # Open a BytesIO stream to store the image data
    img_data = BytesIO(response.content)
    # Get the artist name to use as the S3 object key
    artist = item['artist']
    # Upload the image to S3
    s3.upload_fileobj(img_data, 'halayolay006', f'{artist}.jpg')

