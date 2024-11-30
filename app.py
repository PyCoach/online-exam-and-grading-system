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
    student_id=request.form.get('student_id')
    password=request.form.get('password')
    email=request.form.get('email')
    db=Database()
    message=db.insert(student_id,email,password)
    db.close_connection()
    return message
    

@app.route('/perform_login',methods=['post'])
def perform_login():
    id=request.form.get('id').strip()
    password=request.form.get('password').strip()
    db=Database()
    response,role,name=db.fetch(id,password)
    db.close_connection()
    if response:
        if role=="teacher":
            return render_template('teacher_interface.html',name=name)

        elif role=="student":
            return render_template('student_dashboard.html',name=name)
    else:
        #return error
        return "<p style='color: red; font-size: 50px;'>either user_id or password is incorrect.</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"

@app.route('/process_teacher_action',methods=['post'])
def process_teacher_action():
    action = request.form.get('action')
    if action == 'create_exam':
        return render_template('design_question_paper.html')
    if action== 'schedule_exam':
        return 'schedule exam'
    elif action == 'view_exams':
        return "Redirect to view exams page"
    elif action == 'view_scorecard':
        return "Redirect to view scorecard page"
    return "Invalid action"

@app.route('/create_question_paper',methods=['post'])
def create_question_paper():
    
    mcq_count = int(request.form.get('mcq_count', 0) or "0")
    mcq_marks = int(request.form.get('mcq_marks', 0) or "0")
    short_count = int(request.form.get('short_count', 0) or "0")
    short_marks = int(request.form.get('short_marks', 0) or "0")
    long_count = int(request.form.get('long_count', 0) or "0")
    long_marks = int(request.form.get('long_marks', 0) or "0")

    total_marks = (
        mcq_count * mcq_marks +
        short_count * short_marks +
        long_count * long_marks
    )

    return render_template('create_question_paper.html', mcq_count=mcq_count, short_count=short_count, long_count=long_count)

   
if __name__ == "__main__":
    app.run(debug=True)

