# # Copyright 2018 Google LLC
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# # [START gae_python38_render_template]
# # [START gae_python3_render_template]
# import datetime

# import boto3
# from flask import Flask, render_template, request, flash

# app = Flask(__name__)


# # @app.route('/')
# # def root():
# #     # For the sake of example, use static information to inflate the template.
# #     # This will be replaced with real information in later steps.
# #     dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
# #                    datetime.datetime(2018, 1, 2, 10, 30, 0),
# #                    datetime.datetime(2018, 1, 3, 11, 0, 0),
# #                    ]

# #     return render_template('index.html', times=dummy_times)
# @app.route('/')
# def root():
#     return render_template('index.html')





# @app.route('/login1.html', methods=['GET', 'POST'])
# def route():
#     if request.method == 'POST':
#         print(request.method)
#         verify = False
#         print(request.form)
#         email = request.form['username']
#         password = e_credentails(email)

#         if len(password) ==0:
#             return "Please check your email"


#         if request.form['password'] == password:
#             verify = True 
#         if verify :
#             return root()
#         else :
#             return "Incorrect Email or Password"
#     return render_template('login1.html')

# def e_credentails(email):

#     aws_access_key_id="ASIAR44X363URCNOMOMA"
#     aws_secret_access_key="rUYvoDaba99d5VWlhZ4VQgM4kJnjsG+0EU9564Ra"
#     aws_session_token="FwoGZXIvYXdzED0aDMfg4BiVTtTAa0tgMSLNAZGjVVKM/baWFNB2x1x6IkXniKjUHeCcOq+i8PO02tF/qx2yd7ITB0PSnDGpd4yHhhJZYyqEgloUShf/qMxnDIvlw3xMUHaSeUII6sQTMHjwBDVzso3+5DM+jnv5pEJVmCfDlitzCNqHqQUaNjdpQKEthGrdIUKh9W9Emspyn1nx68INnPGbHfnzzX0dnKPIh+IRCZz7ClJnol0gsuC7i1KkIjQvOG8oezBNaZx1As+ahMkS+QBILSev7ooj4KNVcBJ8VD4PFU5qtLidCLgo2/7EoAYyLYxy6jBunzYL1x4viUohTYL9ZqbJvgAm7/7DRonMRbnXWdHhGSl1ciDgGYQj2g=="
    
#     ddb = boto3.client( "dynamodb",
#                        aws_access_key_id = aws_access_key_id,
#                        aws_secret_access_key =  aws_secret_access_key,
#                        aws_session_token = aws_session_token                   
#     )

#     #Requesting from Dynamo Db
#     name_of_table = 'login'
#     key = {"email" : {'S':email}}

#     #now i am requesting from table 
#     response = ddb.get_item(
#         TableName = name_of_table,
#         key = key)
#     try:
#         return response["password"]["S"]
    
#     except:
#         # print(e)
#         return 0
#     #define table name


# if __name__ == '__main__':
#     # This is used when running locally only. When deploying to Google App
#     # Engine, a webserver process such as Gunicorn will serve the app. This
#     # can be configured by adding an `entrypoint` to app.yaml.
#     # Flask's development server will automatically serve static files in
#     # the "static" directory. See:
#     # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
#     # App Engine itself will serve those files as configured in app.yaml.
#     app.run(host='0.0.0.0', port=8080, debug=True)
# # [END gae_python3_render_template]
# # [END gae_python38_render_template]




from flask import Flask, render_template, request, redirect, session
import boto3

app = Flask(__name__)
app.secret_key = 'secret_key'

# AWS Credentials
access_key="ASIAR44X363UXQTLDRUQ"
secret_key="ZhH88bXvCI/dazBg3WNOGDdBdgoJXOB4AA/3g4O8"
aws_session_token = "FwoGZXIvYXdzELP//////////wEaDEoUAcGEQrre+QOJ2iLNAQuzlUxaVfe7at+MbzUqS1PLQRYQWmNLlTuNP+56np+ZzSfsOFc0Ula9OT/uGHouhSwWeNAjd74pYydz5QxouUeTQJNOCEVjQnJBRfROE03Pex+NuH9cIj6sAdbRu6/X8SC1Jx/iTcUNP0iR36FWUB8T8lnpO/2EnZvHRCZawcf/kOIYTLnAuVkF4btHaFN1at8ToSsxgpwoU5wfln9AuS/hUZXkoEj615vmA+vMdjDux5y+ZbkWGV15JQOogC1NoiKL9UHZcj/g5uXVQZco9vjeoAYyLU2hEItYBuVHBrOCsvZLYW6dYeY3iU/vq4SqO2NZp4gmldSwUdgQGmY3sQFiEQ=="
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

# Run app
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)

