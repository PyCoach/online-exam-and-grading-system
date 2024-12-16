from db import Database
from flask import Flask, render_template, request,session,redirect
import time

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Replace with a secure secret key

@app.route("/")
def index():
    return render_template('login_page.html')

@app.route("/register")
def register():
    return render_template('registration_page.html')

@app.route("/perform_registration",methods=['post','get'])
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
    print(response,role,name)
    db.close_connection()
    if response:
        if role=="teacher":
            session['name']=name
            session['teacher_id']=id
            print(session['teacher_id'])
            return render_template('teacher_interface.html',name=name)
            
        elif role=="student":
            session['student_id']=id
            print(session['student_id'])
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
        return redirect('/schedule_exam')
    elif action == 'view_exams':
        return redirect('/show_all_exams')
    elif action == 'view_scorecard':
        return "Redirect to view scorecard page"
    return "Invalid action"

@app.route('/create_question_paper',methods=['post'])
def create_question_paper():
    
    print("Inside create_question_paper route")
    session['mcq_count']= int(request.form.get('mcq_count'))
    session['mcq_marks']  = int(request.form.get('mcq_marks',0) or "0")
    session['short_count']= int(request.form.get('short_count'))
    session['short_marks']= int(request.form.get('short_marks',0) or "0")
    session['long_count']  = int(request.form.get('long_count'))
    session['long_marks'] = int(request.form.get('long_marks',0) or "0")
    print("long_count",session.get('long_count'))
    
    # total_questions=mcq_count+short_count+long_count

    # total_marks = (
    #     mcq_count * mcq_marks +
    #     short_count * short_marks +
    #     long_count * long_marks
    # )


    return render_template('create_question_paper.html', mcq_count=session.get('mcq_count'), short_count=session.get('short_count'), long_count=session.get('long_count'))
    
   
@app.route('/schedule_exam', methods=['POST', 'GET'])
def schedule_exam():
    db = Database()
    print('inside schedule exams')

    # Fetch all exam names from the database
    exam_tuple = db.fetch_exams()
    exam_names = [exams[0] for exams in exam_tuple]
    exam_names = set(exam_names)  # Remove any duplicates

    selected_exam = None
    selected_class = None
    subjects = []
    class_names = []
    message = None  # Initialize message to avoid UnboundLocalError
    success_message = None

    if request.method == 'POST':
        selected_exam = request.form.get('exam_name')
        selected_class = request.form.get('class_name')

        if selected_exam:
            # Fetch class names if exam is selected
            class_names = db.fetch_class_names_by_exam(selected_exam)

        if selected_exam and selected_class:
            # Fetch subjects associated with the selected exam and class
            subjects = db.fetch_subjects_by_class(selected_exam, selected_class)

            # Get other details
            subject_name = request.form.get('subject_name')
            scheduled_date = request.form.get('scheduled_date')
            start_time = request.form.get('start_time')
            duration = request.form.get('duration')

            if subject_name and scheduled_date and start_time and duration:
                # Insert the exam schedule into the database
                db.insert_exam_schedule(selected_exam, subject_name, selected_class, scheduled_date, start_time, duration, session['teacher_id'])
                success_message = "Exam scheduled successfully!"

            else:
                message = "Please fill all required fields."

        else:
            # Show error message if exam or class is not selected
            message = "Please select both exam and class."

    return render_template(
        'schedule_exam.html',
        exam_names=exam_names,
        selected_exam=selected_exam,
        class_names=class_names,
        selected_class=selected_class,
        subjects=subjects,
        message=message,
        success_message=success_message
    )

@app.route('/go_to_teacher_interface', methods=['POST'])
def go_to_teacher_interface():
    # This is where the teacher interface will be rendered directly.
    return render_template('teacher_interface.html')

@app.route('/show_all_exams')
def show_all_exams():
    db = Database()
    # Replace 'your_table_name' with the actual table name you want to fetch
    all_exams = db.fetch_scheduled_exams()  # Modify query as needed
    for row in all_exams[0]:
        print(row)
    return render_template('scheduled_exams.html', exam_data=all_exams)









if __name__ == "__main__":
    app.run(debug=True)


