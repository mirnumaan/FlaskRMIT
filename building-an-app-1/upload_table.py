from decimal import Decimal
import logging
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import json
import boto3

# configure DynamoDB client

logger = logging.getLogger(__name__)

class MovieDatabase:
    def __init__(self, table):
        self.table = table
    
    def add_movie(self, title, artist, year, img_url, web_url):
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
                    'web_url':{'S': web_url}
                    }, TableName="music223")
        except ClientError as err:
            logger.error(
                "Couldn't add movie %s to table %s. Here's why: %s: %s",
                title, self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise
            
    def add_movies_from_json(self, filename):
        """
        Adds movies to the table from a JSON file.
        :param filename: The name of the JSON file.
        """
        with open(filename) as f:
            songs = json.load(f)
            print(songs)
            for music in songs['songs']:
                print(music)
                self.add_movie(
                    title=music['title'],
                    year=music['year'],
                    artist=music['artist'],
                    img_url = music['img_url'],
                    web_url=music['web_url']
                )
                

if __name__ == '__main__':
    access_key="ASIAR44X363UVPZBBTGD"
    secret_key="o/B3mFs0RRc7nydos/XED7vBn0sE4VxLj6NrX2K/"   
    aws_session_token="FwoGZXIvYXdzEF8aDNHO3qF+F6//hxD5/yLNAeCiIawRpxf8B5eeaygSQd8VV7A5Cobo+9Cb/hWvJYT1uefDLlr41gKjPVInl3ULF0w7RvTgksJc2K9lxX/DSV6bXazpTy6Cbzp3W/89lLl22wJvvZpmZjRP6vhQmELDaQeKExrKHcg5lHy16tgepsALTAkL32bHQL86fN4gWaH4xC1jRcThCMpO6kFkrbefu1a/CD6V7dj4ADdOu/dtqus1dUHwC0uJT+QzNzMOt4lNalATEdAPjzcgEVdO49yw0hEmbJJP4ZLTcGT7gncoqeKEoQYyLcI9IuFMHtUrB91QoJ0tJ/P5ITG9UabjTgqcAsd84IUYHNqEPyUvWnBTlOjYrg=="

    region_name = 'us-east-1'

    dynamodb = boto3.client('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)


    movie_db = MovieDatabase(dynamodb)
    movie_db.add_movies_from_json('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json')

# table = dynamodb.Table('music22')

  
# with open('FlaskRMIT/building-an-app-1/a1.json') as f:
#     data = json.load(f)

# songs = []
# for item in data:
#     song = {
#         'PutRequest': {
#             'Item': {
#                 'title': {'N': item[0]},
#                 'artist': {'S': item[0]}
#             }
#         }
#     }
#     songs.append(song)

# # insert data into DynamoDB table
# with table.batch_writer() as batch:
#     for item in data:
#         batch.put_item(Item=song)