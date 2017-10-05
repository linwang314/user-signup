from flask import Flask, request, redirect, render_template
import cgi 
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def signup():
    username = request.form["username"]
    username_error = ''

    if username == '':
        username_error = "That's not a valid username."
    elif ' ' in username:
        username_error = "That's not a valid username."
        username = ''        
    elif len(username)<3 or len(username)>20:
        username_error = "That's not a valid username."
        username = ''
        
    if not username_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template('signup.html', username_error=username_error)

@app.route("/welcome")
def welcome():
    name = request.args.get('username')
    return '<h1>Welcome, {0}</h1>'.format(name)

app.run()