from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True  

@app.route("/")
def display_signup_form():
    return render_template('home_form.html', title="Welcome to Alexbook | Sign Up Page")

@app.route("/", methods=['POST'])
def validate_signup():
  
  username = request.form['usr_name']

  return render_template('welcome_form.html', name=username)



app.run()