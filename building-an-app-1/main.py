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
<<<<<<< HEAD
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
=======
    # app.run(host='0.0.0.0', port=8080, debug=True)
    app.run(debug=True)

>>>>>>> 530b7aba281f4d6ab5ae15dad0f0e32ccf7ac95f
