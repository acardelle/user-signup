from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True  

def is_blank(word):
  if word == '':
    return True
  else:
    return False

def invalid_char(word):
  if (len(word) < 3) or (len(word)> 20) or (' ' in word):
    return True
  else:
    return False

def invalid_emal(word):
  if (len(word) < 3) or (len(word)> 20) or (' ' in word) or ("@" not in word):
    return True
  else:
    return False

@app.route("/")
def display_signup_form():
    return render_template('home_form.html', title="Welcome to Alexbook | Sign Up Page")

@app.route("/", methods=['POST'])
def validate_signup():

  
  username = request.form['usr_name']
  password = request.form['pas_word']
  veriword = request.form['ver_word']
  email    = request.form['e_mail']
  
  user_error = ''
  pass_error = ''
  veri_error = ''
  emal_error = ''

#Username checks
  if invalid_char(username) == True:
    user_error = 'Invalid username'
  if is_blank(username) == True:
    user_error = 'No username input detected (Must be 3-20 characters with no whitespaces)'

#Password checks
  if invalid_char(password) == True:
    pass_error = 'Invalid password (Must be 3-20 characters with no whitespaces)'
  if is_blank(password) == True:
    pass_error = 'No password input detected'

#Verify checks
  if veriword != password:
    veri_error = 'Passwords do not match'

#Email checks
  if invalid_emal(email) == True:
    emal_error = 'Invalid email address (Must be include a valid domain)'

#Success condition
  if not user_error and not pass_error and not veri_error and not emal_error:
    return render_template('welcome_form.html', name=username)

#Error redirection
  else:
    return render_template('home_form.html',
     user_error=user_error,
     user_field = username,
     pass_error=pass_error,
     veri_error=veri_error,
     emal_error=emal_error,
     emal_field = email)

app.run()