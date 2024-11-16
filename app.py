from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login_page.html')

@app.route("/register")
def register():
    return render_template('registration_page.html')

@app.route("/perform_registration",methods=['post'])
def perform_registration():
    name=request.form.get('name')
    dob=request.form.get('dob')
    email=request.form.get('email')
    adm_no=request.form.get('adm_no')
    user_id=request.form.get('user_id')
    password=request.form.get('password')
    return f"hello {name}"

@app.route('/perform_login',methods=['post'])
def perform_login():
    return 'testsgtrg'
   
app.run(debug=True)
