from decimal import Decimal
import logging
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import json
import boto3

# configure DynamoDB client

logger = logging.getLogger(__name__)

class MusicDatabase:
    def __init__(self, table,tn):
        self.table = table
        self.tn = tn
    
    def add_music(self, title, artist, year, img_url, web_url):
        """
        Adds a movie to the table.
        :param title: The title of the movie.
        :param year: The release year of the movie.
        :param plot: The plot summary of the movie.
        :param rating: The quality rating of the movie.
        """
        try:
            self.table.put_item(
                Item={
            
                    'title':{'S': title},
                    'artist': {'S': artist},
                    'img_url':{'S': img_url},
                    'web_url':{'S': web_url},
                    'year':{'S': year}
                    
                    }, TableName= self.tn)
        except ClientError as err:
            logger.error(
                "Couldn't add movie %s to table %s. Here's why: %s: %s",
                title,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
            
    def add_music_from_json(self, filename):
        """
        Adds movies to the table from a JSON file.
        :param filename: The name of the JSON file.
        """
        with open(filename) as f:
            songs = json.load(f)
            print(songs)
            for music in songs['songs']:
                print(music)
                self.add_music(
                    title=music['title'],
                    year=music['year'],
                    artist=music['artist'],
                    img_url = music['img_url'],
                    web_url=music['web_url']
                )
                

if __name__ == '__main__':
    access_key="ASIAR44X363UZVQQ7R5S"
    secret_key="GpV9Ob/gM/brvIEck+JpVA+p/6ICr5MzQrLg68It"   
    aws_session_token="FwoGZXIvYXdzEM3//////////wEaDD9jNcPWY2uje0seCyLNARg8f+tXfzbm/V8/AaNIVWACyLOww4RaS/gfqI8gwRmDSuK/uXdYT1jTNzQ61hmNzMfPQnAtg54KKiR5xq5ALV+89S36tWcF949ED8n4v0h8FbVL9lUP6SRFLk1WevGTS9bBV9gcZ+9Rv+96bV3v51pmI10LPaC2y9su2aW2bDFAl2PWJ7VVdyy3fIF2BwC67sNwlcHfEHsE9v/tKLnqrzmpvrZKQcCI3TO1dWTY7T1TOUhMqLJLtaB6/fzqE2Tx+abzOQLnXXMDZdr4RA0o64nVoQYyLVNmPiMZaV9JwLBFX7Bqz3NTmNHl80wK8mOLy7bR+8jn/v30++F1yT+GyTl0Fw=="
    region_name = 'us-east-1'


    dynamodb = boto3.client('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)

    tns = ['numaan0', 'numaan1', 'numaan2', 'numaan3', 'numaan4', 'numaan5', 'numaan6', 'numaan7', 'numaan8', 'numaan9', 'music']
    for tn in tns:
        music_db = MusicDatabase(dynamodb,tn)
        music_db.add_music_from_json('a1.json')


  
