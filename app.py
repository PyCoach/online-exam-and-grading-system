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
    
    elif action=='check_student_answers':
        return redirect('/check_student_answers')
    else:
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
    

@app.route('/add_questions', methods=['POST'])
def add_questions():
    db = Database()

    exam_name = request.form.get('exam_name')
    subject = request.form.get('subject')
    exam_id= request.form.get('exam_id')
    class_name= request.form.get('class_name')
    print(exam_id,exam_name,class_name)

    if not exam_name:
        return "<p style='color: red; font-size: 50px;'>Exam name is missing.</p>"

    
    # Fetch total counts (ensure these are passed in the form)
    mcq_count=session.get('mcq_count')
    short_count=session.get('short_count')
    long_count=session.get('long_count')
    print(f"mcq_count: {mcq_count}")

    


    # Insert MCQs
    for i in range(1, mcq_count + 1):
        question_text = request.form.get(f'mcq{i}')
        print(question_text)
        options = '|'.join([
            request.form.get(f'mcq{i}_option1'),
            request.form.get(f'mcq{i}_option2'),
            request.form.get(f'mcq{i}_option3'),
            request.form.get(f'mcq{i}_option4')
        ])
        print(options)
        correct_answer = request.form.get(f'mcq{i}_answer')
        print(correct_answer)
        marks = int(request.form.get(f'mcq{i}_marks', 1))  # Default to 1 mark if not provided
        print(marks)
        # Insert MCQ into the database
        if question_text and options and correct_answer:
            db.insert_question(
                exam_name=exam_name,
                subject=subject,
                class_name=class_name,
                exam_id=exam_id,
                question_text=question_text,
                question_type="mcq",
                options=options,
                correct_answer=correct_answer,
                marks=marks
                
            )


    # Loop through Short Answer Questions
    for i in range(1, short_count + 1):
        question_text = request.form.get(f'short{i}')
        marks = int(request.form.get(f'short{i}_marks', 1))  # Default marks to 1 if not provided

        # Insert Short Answer Question into the database
        if question_text:
            db.insert_question(
                exam_name=exam_name,
                subject=subject,
                exam_id=exam_id,
                class_name=class_name,
                question_text=question_text,
                question_type="short",
                marks=marks
            )


    # Loop through Long Answer Questions
    for i in range(1, long_count + 1):
        question_text = request.form.get(f'long{i}')
        marks = int(request.form.get(f'long{i}_marks', 1))  # Default to 1 mark if not provided

        if question_text:
            db.insert_question(
                exam_name=exam_name,
                subject=subject,
                exam_id=exam_id,
                class_name=class_name,
                question_text=question_text,
                question_type="long",
                marks=marks
            )
    db.close_connection()
    return "Questions added successfully!"


@app.route('/schedule_exam', methods=['POST', 'GET'])
def schedule_exam():
    db = Database()
    print('Inside schedule_exam')

    # Fetch all exam names and IDs from the database
    exam_tuple = db.fetch_exams()  # Ensure this fetches (exam_name, exam_id)
    exam_names = [exam[0] for exam in exam_tuple]  # Extract exam names
    exam_ids = {exam[0]: exam[1] for exam in exam_tuple}  # Map exam_name to exam_id

    # Initialize variables
    selected_exam = None
    selected_class = None
    selected_subject = None
    selected_exam_id = None
    filtered_exam_ids = []
    subjects = []
    class_names = []
    message = None
    success_message = None

    if request.method == 'POST':
        # Fetch selected exam from the form
        selected_exam = request.form.get('exam_name')

        if selected_exam:
            # Fetch class names for the selected exam
            class_names = db.fetch_class_names_by_exam(selected_exam)

            # Fetch the selected class from the form
            selected_class = request.form.get('class_name')

            if selected_class:
                # Fetch subjects for the selected class
                subjects = db.fetch_subjects_by_class(selected_exam, selected_class)

                # Fetch the selected subject from the form
                selected_subject = request.form.get('subject_name')

                if selected_subject:
                    # Fetch filtered exam IDs
                    filtered_exam_ids = db.fetch_exam_id_by_subjects(selected_subject, selected_class, selected_exam)
                    filtered_exam_ids=[i[0] for i in filtered_exam_ids]

                    # Fetch the selected exam ID from the form
                    selected_exam_id = request.form.get('exam_id')

                    # Handle final form submission for scheduling the exam
                    if 'submit_schedule' in request.form:
                        # Get the remaining fields
                        scheduled_date = request.form.get('scheduled_date')
                        start_time = request.form.get('start_time')
                        duration = request.form.get('duration')

                        # Validate all fields
                        if selected_exam_id and scheduled_date and start_time and duration:
                            # Insert the schedule into the database
                            
                            db.insert_exam_schedule(
                                selected_exam_id, selected_exam, selected_subject, selected_class,
                                scheduled_date, start_time, duration, session['teacher_id']
                            )

                            success_message = "Exam scheduled successfully!"
                            print(success_message)
                        else:
                            message = "Please fill all required fields."
                else:
                    message = "Please select a subject."
            else:
                message = "Please select a class."
        else:
            message = "Please select an exam."

    return render_template(
        'schedule_exam.html',
        exam_names=exam_names,
        selected_exam=selected_exam,
        class_names=class_names,
        selected_class=selected_class,
        subjects=subjects,
        selected_subject=selected_subject,
        filtered_exam_ids=filtered_exam_ids,
        selected_exam_id=selected_exam_id,
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


@app.route('/show_exams_by_class')
def show_exams_by_class():
    db=Database()
    student_id=session['student_id']
    class_name= db.fetch_class_by_student_id(student_id)
    exams=db.fetch_exams_by_class(class_name)
    return render_template('student_exams.html',exams=exams)

@app.route('/student/attempt_exam/<exam_id>', methods=['GET', 'POST'])
def attempt_exam(exam_id):
    db = Database()
    subject = request.args.get('subject')
    class_name = request.args.get('class_name')
    
    print("Subject:", subject, "Class Name:", class_name, "Exam ID:", exam_id)
    
    # Fetch questions from the database based on exam_id, subject, and class_name
    questions = db.fetch_exam_questions_for_student(exam_id, subject, class_name)
    print("Questions Fetched:", questions)

    if not questions:
        message = "No questions available for this exam."
        return render_template('attempt_exam.html', questions=[], message=message)
    
    return render_template('attempt_exam.html', questions=questions, exam_id=exam_id,subject=subject,class_name=class_name)



@app.route('/submit_exam/<exam_id>', methods=['POST'])
def submit_exam(exam_id):
    db = Database()

    # Retrieve subject and class_name from the form
    subject = request.args.get('subject')
    class_name = request.args.get('class_name')
    print("resquest.form", request.form)
    print("Subject:", subject, "Class Name:", class_name, "Exam ID:", exam_id)
    
    # Fetch all questions with correct answers
    questions = db.fetch_exam_questions_for_student(exam_id, subject, class_name)
    print("Questions Fetched:", questions)

    # Create a dictionary for correct answers
    correct_answers = {question[0]: question[3] for question in questions}  # {question_text: correct_option}
    print("Correct Answers:", correct_answers)
    
    # Fetch submitted answers from the form
    submitted_answers = {}
    for key, value in request.form.items():
        if key not in ["subject", "class_name"]:  # Ensure it matches the expected input name
            submitted_answers[key] = value  # Use question text as key

    print("Submitted Answers:", submitted_answers)
    print("Correct Answers:", correct_answers)

    # Evaluate the score
    score = 0
    total_marks = sum(q[4] for q in questions if q[1] == 'mcq')
    student_responses = []
    is_checked = False  # Set to True if the teacher checks the exam
    n=0
    for question_text, correct_answer in correct_answers.items():
        response = submitted_answers.get(question_text)
        marks_awarded = 0
          # Always mark the question as checked, even if left empty
        # Always mark the question as checked if it is an 'mcq' and attempted
        is_checked = True if questions[n][1] == 'mcq' else False
        maximum_marks=questions[n][4]
        question_type=questions[n][1]
        print("Is Checked:", is_checked)
        if response == correct_answer and question_type=='mcq':
            marks_awarded = next(q[4] for q in questions if q[0] == question_text)  # Get marks
            score += marks_awarded  # Increment score for correct answers

        # Get question ID or any other identifier from the `questions` list
        question_id = next(q[4] for q in questions if q[0] == question_text)
        checkers = ['automated' if is_checked else 'manual'][0]
        student_responses.append((session['student_id'], exam_id, question_id,question_text, response, marks_awarded,maximum_marks, is_checked, checkers))

        print("Response:", response, "Correct Answer:", correct_answer, "Marks Awarded:", marks_awarded)
        n+=1
    print(f"MCQ Score: {score}/{total_marks}")

    # Save the result in the database
    student_id = session['student_id']

    db.store_student_responses(student_responses)
    db.save_exam_result(student_id, exam_id, subject, class_name, score, total_marks)

    # Redirect to results page or confirmation
    return render_template(
        'exam_result.html',
        score=score,
        total_marks=total_marks,
        subject=subject,
        class_name=class_name
    )
@app.route('/check_student_answers')
def check_student_answers():
    db = Database()
    teacher_id=session['teacher_id']
    student_responses=db.fetch_student_responses(teacher_id)
    return render_template('check_student_answers.html',student_responses=student_responses)


app.run(debug=True)


