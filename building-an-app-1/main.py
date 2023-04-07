from flask import Flask, render_template, request, redirect, session,url_for,flash
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError 
import images_extr
import del_music
import query_id
from table import Music
from upload_table import MusicDatabase
import submus
import json
import requests
import base64
import requests
import json

# from dashboard_acess import dat
# import dashboard_acess
app = Flask(__name__)
app.secret_key = 'secret_key'
# AWS Credentials
access_key="ASIAR44X363UZ233ZJ4A"
secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="

region_name = 'us-east-1'
table_name = 'login'
my_bucket = 'halayolay006'
# DynamoDB Client
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)
s3 = boto3.client('s3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token = aws_session_token,region_name=region_name)

@app.route('/')
def root():
    return render_template('index.html')

# Login route
@app.route('/login')
def login():
    return render_template('login.html', x='none')

# Authenticate route
@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    # DynamoDB Table is been checked here
    table = dynamodb.Table(table_name)
    print(email, password)  
    # Retrieving the data of the user data from DynamoDB
    endpoint_url = "https://6ftlhwtbt8.execute-api.us-east-1.amazonaws.com/LoginFunction"
    payload = {"email":email}
    response=requests.post(endpoint_url,json=payload)
    print(response)
    response = json.loads(response.text)
    username = response
    if response['password '] == password:
        session['email'] = email
        session['user_name'] = username['user_name']
        print(password)
        return redirect('/welcome')
    else:
        
        error = 'Invalid username or password'
        print('error')
        return render_template('login.html', x='block',error= error)
 

@app.route('/delete_music', methods=['POST'])
def delmu():
    val = request.form['mf']
    print(val)
    del_music.delete_music(val,session['user_name'])
    return redirect('/welcome') 

@app.route('/welcome')
def dashboard():

    if 'email' not in session:
        return redirect(url_for('login'))
        
        # Get the music data from DynamoDB
    tn = session['user_name']
    print(tn)
    payload = {
        "table_name": tn
        }
    end_url = "https://1l68j6tkoa.execute-api.us-east-1.amazonaws.com/develop/music"
    resp = requests.post(end_url, json=payload) 
    
    music_data = resp.text
    music_data = json.loads(music_data)
    
    img_data = images_extr.img_extract()

    return render_template('welcome.html', music_data=music_data,img_data=img_data)
    
# Logout route
@app.route('/signup', methods=['GET', 'POST'])
def register():
    access_key="ASIAR44X363UZ233ZJ4A"
    secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
    aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="


    region_name = 'us-east-1'
    dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)

    table =dynamodb.Table(table_name)
    
    if request.method == 'POST':
        email = request.form['email']
        user_name = request.form['user_name']
        password = request.form['password']
        
        
        # check if email already exists in DynamoDB table
        response = table.get_item(Key={'email': email})
        
        if 'Item' in response:
            return 'Email already exists'
        # add new user to DynamoDB table
    
        else:
            table.put_item(
            Item={
                'email': email,
                'user_name': user_name,
                'password ': password
            })
            access_key="ASIAR44X363UZ233ZJ4A"
            secret_key="96DJI/+3y/8ZgDop20CgyvgsjmImwTqoAb0jZcI2"   
            aws_session_token="FwoGZXIvYXdzEGgaDIk7ZUewXrSNSExVSiLNAas2wKFFG48xuo56IQSr3ckCQGCQj/DGvG2popCgdFnYq9QTvrLCRTfrCd9+2hgX2iotHmDQZuozkjpnS1fBlL+n2vvS8xCGF5PRb3MBaIw2lzhWLD1AIWIcjY0oJmgOlHFuPgntHirHGvaM2J4ZXNnSfmYxgdZnH8zDZifRs3bXhHeHn54PI1sB9pqbBfkaABtBhqnI3wfXtvKpT392h1lTJrmfukNmMkrAgIqm8+YALPgeORuk/+Lpj+Y5rTdYnOtzq96/ajwjycE28rcog+++oQYyLZVKtTRkW7m8tjWR4YJLFRK31EJ/iWYEFeWOQYrcKPll50Wm6nlQwmt7FEMICg=="

            region_name = 'us-east-1'

            # DynamoDB Client

            try :
                dynamodb = boto3.resource('dynamodb',
                                        aws_access_key_id=access_key,
                                        aws_secret_access_key=secret_key,
                                        aws_session_token = aws_session_token,
                                        region_name=region_name)
                m = Music(dyn_resource=dynamodb)
                
                m.create_table(user_name)
                
                
                dynamodb = boto3.client('dynamodb',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                aws_session_token = aws_session_token,
                                region_name=region_name)
                
                music_db = MusicDatabase(dynamodb,user_name)
                music_db.add_music_from_json('a1.json')

            except Exception as e:

                print('e')




        return redirect('/login')
    return render_template('signup.html')

#logout route 
@app.route("/logout")
def logout():
    return redirect(url_for('login'))

# query page route
@app.route("/search", methods=["POST"])
def query():
    title = request.form['title']
    artist = request.form['artist']
    year = request.form['year']
    if title == "":
        title = None
    if artist == "":
        artist = None
    if year == "":
        year = None
    music_data = query_id.search_music(title,artist,year)
    print("music_data: ", music_data)
    if music_data['Count']==0:
        error = 'No result is retrieved. Please query again'
        return render_template("query_page.html", error = error)
    if "Items" in music_data:
        music_data=music_data["Items"]
        images_data = images_extr.img_extract()
        
        return render_template('query_page.html', music_data=music_data, img_data=images_data, str=str)
    else:
        
        return render_template("query_page.html",error=error)

@app.route("/query")
def query_pg():
    return render_template("query_page.html")

@app.route("/subscribe_music", methods=['POST'])
def sub_mus():
    title = request.form['mf']
    submus.add_music(title,session['user_name'])
    return redirect('/welcome')


# Run app
if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port ='80' , debug=True)
    
  
