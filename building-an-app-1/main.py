from flask import Flask, render_template, request, redirect, session,url_for,flash
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError 

app = Flask(__name__)
app.secret_key = 'secret_key'
# AWS Credentials
access_key="ASIAR44X363U356AVKEJ"
secret_key="D2L7XgO9YvodVhjd8NewHD1eFC4Kqnw4/54VHq4H"   
aws_session_token="FwoGZXIvYXdzEEEaDIWEJyMGoZPaut7C0CLNAU/JP37Uo31YjmMARysmQ9rSdwllN9oV+HGJ0CXKUyZf8gjDatfxxQVACbHow6/uvU4kL5pDwwGe/F93gxsuBsLpouC2q5YvWo/ssgHASJZsBIi7uYeedUE13h98XgxBiB9F4t2tjlhVaQ7NlCzMTdEMcd4xVb9ApuLrHW7NnpUfRn/KfWBLlYpjrDDXzsy5OBJ3mfaKlsjEfz3VfDm4YxjFX5CVnXqwUxJw5uDplpsare2XmqwAbFP6GvLIDGYKDUu4PC2fMEVb8H+1TMMokYb+oAYyLRTXgIQ9ZAo6llVeGlZZLk3hmZDAKT7Z7HD+vZ1WODnhPe1gWIZJoG5yfcGvcA=="
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
    # DynamoDB Table is been checked here
    table = dynamodb.Table(table_name)

    try:
        # Retrieving the data of the user data from DynamoDB
        response = table.get_item(Key={'email': email})
        if 'Item' in response:
            username = response['Item'] 
            if response['Item']['password '] == password:
                session['email'] = email
                session['user_name'] = username['user_name']
                return redirect('/welcome')
            else:
                return redirect('/login')
        else:
            return redirect('/login')

    except Exception as e:
        return redirect('/login')

# Dashboard route
@app.route('/welcome')
def dashboard():
    return render_template('welcome.html', user_name=session['user_name'])
    
    

# Logout route
@app.route('/signup', methods=['GET', 'POST'])
def register():
    table = dynamodb.Table(table_name)
    if request.method == 'POST':
        email = request.form['email']
        user_name = request.form['user_name']
        password = request.form['password']
        

        # check if email already exists in DynamoDB table
        # response = table.get_item(Key={'email': email})
        # if 'Item' in response:
        #     return 'Email already exists'
        # add new user to DynamoDB table
        table.put_item(
            Item={
                'email': email,
                'user_name': user_name,
                'password ': password
            })
        return redirect('/login')
    return render_template('signup.html')

@app.route("/logout")
def logout():
    return redirect(url_for('login'))


# Run app
if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port ='80' , debug=True)
    
  
