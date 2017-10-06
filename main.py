from flask import Flask, request, redirect, render_template
import cgi 
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def valid(something):
    if something == '':
        return False
    elif ' ' in something:
        return False        
    elif len(something)<3 or len(something)>20:
        return False
    else:
        return True
        
def is_valid(email):
    if email == '':
        return True
    elif ' ' in email:
        return False
    elif email.count('@') != 1 or email.count('.') != 1:
        return False
    elif len(email)<3 or len(email)>20:
        return False
    else:
        return True


@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if not valid(username):
        username_error = "That's not a valid username."  
        username = ''
        password = ''
        verify_password = ''

    if not valid(password):
        password_error = "That's not a valid password."
        password = ''
        verify_password = ''
    
    if verify_password == '':
        verify_error = "Passwords don't match."
        password = ''
    
    if password != verify_password:
        verify_error = "Passwords don't match."
        password = ''
        verify_password = ''
    
    if not is_valid(email):
        email_error = "That's not a valid email."
        email = ''
        password = ''
        verify_password = ''


    if not username_error and not password_error and not verify_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template('signup.html', username_error=username_error,
            password_error=password_error, verify_error=verify_error,
            email_error=email_error, user_name=username, password=password,
            verify_password=verify_password, email=email)

@app.route("/welcome")
def welcome():
    name = request.args.get('username')
    return '<h1>Welcome, {0}</h1>'.format(name)

app.run()