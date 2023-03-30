from decimal import Decimal
import logging
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import json
import boto3

# configure DynamoDB client

logger = logging.getLogger(__name__)

class MovieDatabase:
    def __init__(self, table,tn):
        self.table = table
        self.tn = tn
    
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
                    'web_url':{'S': web_url},
                    'year':{'S': year}
                    
                    }, TableName= self.tn)
        except ClientError as err:
            logger.error(
                "Couldn't add movie %s to table %s. Here's why: %s: %s",
                title,
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
    access_key="ASIAR44X363USCC7RX76"
    secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"   
    aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="    
    region_name = 'us-east-1'


    dynamodb = boto3.client('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)

    tns = ['numaan0', 'numaan1', 'numaan2', 'numaan3', 'numaan4', 'numaan5', 'numaan6', 'numaan7', 'numaan8', 'numaan9', 'music']
    for tn in tns:
        movie_db = MovieDatabase(dynamodb,tn)
        movie_db.add_movies_from_json('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json')


  
