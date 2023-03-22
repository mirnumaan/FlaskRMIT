from flask import Flask, render_template, request, redirect, session
import boto3
# import logging
# from table import Movies
from botocore.exceptions import ClientError 

app = Flask(__name__)
app.secret_key = 'secret_key'

# AWS Credentials
access_key="ASIAR44X363U7GP2W6MF"
secret_key="H//ASuVFAF7dCWneTWYTHqgLbQ+YkHWb8CgA/75c"   
aws_session_token="FwoGZXIvYXdzEOD//////////wEaDACcm2AmwJfjDGNsCCLNAUftifEzGGZZCBOOXm153gojkQ8bV/wOpS32PwHv2H6/9mixmYSSjFZyqft1AhDav5nLsvgzT6MdmDPI9sWB4Z5VS3q9ztabbXgeH6XnGN/GbyWB7yaVwQjyBRGgyn0uNnP1me7Y7Rti89EX5ZvDLLROkIUuh1qocJVqn+r3mCGU7bgSX68xsbW6O6fB+ZyFgIF0RMnQbcn5a/JI3yMAcv4w9Z9KUNypSXS6NRwbEJpdk0yaKVPhuRyOlmw2RJKvVaOc5rA5xc185YGFzZsoguDooAYyLc+KRKs8NrVg6X5jo4i+VzvT0xNWH87+pQUxvqVluzxbSNTL9VJPSLN9fzcbLw=="
region_name = 'us-east-1'
table_name = 'login'

# DynamoDB Client
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          aws_session_token = aws_session_token,
                          region_name=region_name)

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

    # DynamoDB Table
    table = dynamodb.Table(table_name)

    try:
        # Retrieve user data from DynamoDB
        response = table.get_item(Key={'email': email})
        if 'Item' in response: 
            if response['Item']['password '] == password:
                session['email'] = email
                print("Hi from if!!")
                return redirect('/welcome')

        else:
            print("Hi from else")
            return redirect('/login')

    except Exception as e:
        print("Exception: ", e)
        return redirect('/login')

# Dashboard route
@app.route('/welcome')
def dashboard():
    print(session)
    
    return render_template('welcome.html')
    

# Logout route
@app.route('/signup')
def logout():
    # session.pop('email', None)
    return render_template('/signup.html')




# Run app
if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port ='8080' , debug=True)
    
  
