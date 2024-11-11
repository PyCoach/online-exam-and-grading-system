from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('login_page.html')

@app.route('/registration_page')
def register():
    return render_template('/registration_page.html')

@app.route('/perform_registration')
def perform_registration():
    return "Hi" 

@app.route('/perform_login')
def perform_login():
    return "Hi"
app.run(debug=True)
