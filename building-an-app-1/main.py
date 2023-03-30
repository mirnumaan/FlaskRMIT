from flask import Flask, render_template, request, redirect, session,url_for,flash
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError 
import images_extr
import del_music
import query_id
from table import Music
from upload_table import MovieDatabase
import submus
# from dashboard_acess import dat
# import dashboard_acess
app = Flask(__name__)
app.secret_key = 'secret_key'
# AWS Credentials
access_key="ASIAR44X363USCC7RX76"
secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"
aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="
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
    return render_template('login.html')

# Authenticate route
@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    # DynamoDB Table is been checked here
    table = dynamodb.Table(table_name)
    print(email, password)  

    try:
        # Retrieving the data of the user data from DynamoDB
        response = table.get_item(Key={'email': email})
        print(response)
        if 'Item' in response:
            username = response['Item'] 
            if response['Item']['password '] == password:
                session['email'] = email
                session['user_name'] = username['user_name']
                print(password)
                return redirect('/welcome')
            else:
                print("Error??")
                error = 'Invalid username or password'
                return redirect('/login', error = error)
        else:
            return redirect('/login')

    except Exception as e:
        print(e)
        return redirect('/login')

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
    music_table = dynamodb.Table(tn)
    music_data = music_table.scan()['Items']
    img_data = images_extr.img_extract()
    print(music_data[0]['title']+".jpg")
    print(img_data[music_data[0]['title']+".jpg"])
    return render_template('welcome.html', music_data=music_data,img_data=img_data)
    
# Logout route
@app.route('/signup', methods=['GET', 'POST'])
def register():
    table = dynamodb.Table(table_name)
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
            access_key="ASIAR44X363USCC7RX76"
            secret_key="PddRScFV5nlhFO6FWwYnc5xo9ysBcwymMhltpQ9O"   
            aws_session_token="FwoGZXIvYXdzEKP//////////wEaDB4MrriF19djoauXoiLNAf4zbreTjcZYyPyxrln3y4w0OT5lsN+dguZlTEAvXgN3go/3DOcUlwOpKlippEkl/JhWqV4gWnaRay+ke6sXgwGY7CzLKltxCpuO+n0OUEALsUYz1tOmdsxPsQQPXsVV9M1TRvFtAnCXHvCrEouyj+1dn0ReyCGjRHj3S9ebBJOp6ftFGZZ4+Ly9+bQrsAZFZwYKxNdd+yyYMHLUVnyfmWIdTAaWr16ncCbPqM3YXeTR4PqRA2fx+sDb8LcDn2DZgyIhKz0ijWvnVpc7rCIoudmToQYyLSQDs9M5HmUeKuDtZV69ln/OYqIYt8yTPyoyHqPtgKGXAXtZDcfua3uVeopsIg=="    
            region_name = 'us-east-1'

            # DynamoDB Client
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
            
            movie_db = MovieDatabase(dynamodb,user_name)
            movie_db.add_movies_from_json('/Users/numaanbashir/Documents/cybersecurity/cloud_computing/assign1/FlaskRMIT/building-an-app-1/a1.json')



        return redirect('/login')
    return render_template('signup.html')
    
@app.route("/logout")
def logout():
    return redirect(url_for('login'))

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
    if music_data==None:
        return redirect('/query')
    if "Items" in music_data:
        music_data=music_data["Items"]
        images_data = images_extr.img_extract()
        return render_template('query_page.html', music_data=music_data, img_data=images_data, str=str)
    else:
        return redirect('/query')

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
    
  
