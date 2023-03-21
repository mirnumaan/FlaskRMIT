from table import Movies
from flask import Flask, render_template, request, redirect, session
import boto3
 

app = Flask(__name__)
app.secret_key = 'secret_key'

# AWS Credentials
access_key="ASIAR44X363U5N2K53VF"
secret_key="QTFe3YejAiB+3IKtASnsbCWW2LRJ6szMV1HPOOhC"
aws_session_token="FwoGZXIvYXdzEM///////////wEaDM+dqQAQc/h3MhlPHyLNAVz0nCbwldv+O7MuhzKMubVA470+ttrGLmfKhBPay2drmZH5bEijT0yGL/zslPKtLYV0ICgsQwVa5FtMxlKjlVZRyUS0V3y5ELJz3LsAvq8IpC+APSUFzXbYs7GPlaevBwhVb7Th1EN/DRjV5o7cvTED7/q64x6mkpWM2jSkBt1rZ++Qv5vB/R8ESl0/A5kPiFnHshyKx3P5npv9Tt/JnrSYj3V2Wt+4kUr9Sj11pImmQFnpNyl6zLrdVLWwhWcSrndL3YXKy8sWy2XNvp4okYzloAYyLRSQ6eawzuS6zqveuxBBC4ZIH8zvtojV7RSddcYTaj97jOyKFI6/RfN49JSlew=="
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
        print(response)
        # Check if user exists and password matches
        if 'Item' in response and response['Item']['password'] == password:
            session['email'] = email
            print ("hi")
            return redirect('/welcome')

        else:
            return redirect('/login')

    except Exception as e:
        print(e)
        return redirect('/welcome')

# Dashboard route
@app.route('/welcome')
def dashboard():
    print(session)
    
    return render_template('welcome.html')
    

# Logout route
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')


######### s3 bucket ################




############3 dynamo table #####################

# response = dynamodb.create_table(
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'student_id',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'student_name',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'course_id',
#             'AttributeType': 'S'
#         }
#     ],
#     TableName='Rmit',
#     KeySchema=[
#         {
#             'AttributeName': 'student_name',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'student_id',
#             'KeyType': 'RANGE'
#         },
#     ],
#     LocalSecondaryIndexes=[
#         {
#             'IndexName': 'course_id',
#             'KeySchema': [
#                 {
#                     'AttributeName': 'student_name',
#                     'KeyType': 'HASH'
#                 },
#                 {
#                     'AttributeName': 'course_id',
#                     'KeyType': 'RANGE'
#                 }
#             ],
#             'Projection': {
#                 'ProjectionType': 'ALL'
#             }
#         },
#     ],
#     BillingMode='PAY_PER_REQUEST',

# )
########################

# Run app
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    
    app.run(debug=True)

