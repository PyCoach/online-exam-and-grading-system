from db import Database
from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login_page.html')

@app.route("/register")
def register():
    return render_template('registration_page.html')

@app.route("/perform_registration",methods=['post'])
def perform_registration():
    adm_no=request.form.get('adm_no')
    password=request.form.get('password')
    email=request.form.get('email')
    db=Database()
    message=db.insert(adm_no,email,password)
    db.close_connection()
    return message
    

@app.route('/perform_login',methods=['post'])
def perform_login():
    user_id=request.form.get('user_id')
    password=request.form.get('password')
    db=Database()
    response=db.fetch(user_id,password)
    db.close_connection()
    if response==True:
        return render_template('after_login.html')

    else:
        return "<p style='color: red; font-size: 50px;'>either user_id or password is incorrect.</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"

   
if __name__ == "__main__":
    app.run(debug=True)

