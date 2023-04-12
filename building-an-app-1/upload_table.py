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
    access_key="ASIAR44X363U7ORN4XHS"
    secret_key="l2St4RhkiXqMDdA1TAjevEZyur4cTJtS8syj7zDD"   
    aws_session_token="FwoGZXIvYXdzENv//////////wEaDNZqBWjstBatxazjPSLNAbm9BL8be6H/3GWdCN7QJabcSzMdqRotB9dVf8EjWyjNCpTxaQEtQ1V8b9ZSL26ga6+azu/zEqMpr1jkeyPv8l+jQccsc4LR5VjIX86WDTIW1fVUroHRvXr2MBcr9+VdPCotN1XFUzZmFQ/ijJCk9xHcfsVTnZta+L8rV2usuAPHmnmLuyOFN2PdN1PdVJ0Eew4RXcvNYZTbnJHT/g6DIONuYvKVDsql5qHPcm4jOTPGbuw+wv4GqQO4oMw4W4iex+UTsRd+meAjh78ZH8ooo5jYoQYyLWjFhIBR5CuqfIy9ixk6Y5/libuC6Kha057CkDhmQE4NbV7Pz2HwX1DCFtPJ8g=="
    region_name = 'us-east-1'


    dynamodb = boto3.client('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)

    tns = ['numaan0', 'numaan1', 'numaan2', 'numaan3', 'numaan4', 'numaan5', 'numaan6', 'numaan7', 'numaan8', 'numaan9', 'music']
    for tn in tns:
        music_db = MusicDatabase(dynamodb,tn)
        music_db.add_music_from_json('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json')


  
