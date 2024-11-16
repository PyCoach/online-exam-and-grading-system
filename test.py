from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login_page.html')

@app.route("/register")
def register():
    return render_template('registration_page.html')

@app.route('/perform_registration')
def perform_registration():
    return "Registration successful"

@app.route('/logged_in' , methods=["post"])
def perform_login():
    return render_template('after_login.html')
   

if __name__ == "__main__":
    app.run(debug=True)
