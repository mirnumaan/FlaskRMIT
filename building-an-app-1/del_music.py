import os 
import boto3

def delete_music(id_music,tn):

    access_key="ASIAR44X363UZ233ZJ4A"
    secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
    aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="

    region_name= 'us-east-1'

    dynamodb = boto3.client('dynamodb',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            aws_session_token = aws_session_token,
                            region_name=region_name)
    
    table_name=tn

    key = {"title":{"S": id_music}}

    print(dynamodb.delete_item(TableName=table_name, Key = key))
