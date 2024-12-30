import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="project",
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def insert(self, student_id,email, password):

        # Check if the admission number exists in the students table
        query_check_adm_no = "SELECT student_id FROM students WHERE student_id = %s"
        self.cursor.execute(query_check_adm_no, (student_id,))
        result_check_adm_no= self.cursor.fetchone()

        
        if not result_check_adm_no:
            return f"<p style='color: red; font-size: 50px;'>Admission number '{student_id}' does not exist .</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"

        #checking if email exists in students table
        query_check_email = "SELECT email FROM students WHERE email = %s"
        self.cursor.execute(query_check_email, (email,))
        result_check_email = self.cursor.fetchone()

        
        if not result_check_email:
            return f"<p style='color: red; font-size: 50px;'>email '{email}' does not exist .</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"


        # Check if the admission number already exists in the users table
        query_check_user = "SELECT student_id FROM registered_students WHERE student_id = %s"
        self.cursor.execute(query_check_user, (student_id,))
        record = self.cursor.fetchone()


        
        if record:
            return f"User already exists for Admission Number: {student_id}."

        # Get the last user_id(id) from the users table
        query_last_user_id = "SELECT id FROM registered_students ORDER BY id DESC LIMIT 1"
        self.cursor.execute(query_last_user_id)
        last_record = self.cursor.fetchone()
        
        if last_record:
            last_user_id = last_record[0]
        else:
            last_user_id = "STL0000"  # Default if no records exist

        # Generate a new user_id (last user_id + 1)
        new_user_id = "ID" + str(int(last_user_id[3:]) + 1).zfill(4)

        # Insert the user details into the users table
        query_insert_user = """
        INSERT INTO registered_students (student_id, id, password)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query_insert_user, (student_id, new_user_id, password))
        self.connection.commit()

        return f"<p style='font-size:40px'>User registered successfully with  <p style='color:blue; font-size:50px'>User ID:{new_user_id}  <a  href='/'>click here</a> to go to login page </p>"

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def fetch(self, id, password):
        
        
        query_student = "SELECT password FROM registered_students WHERE id = %s"
        print('executing student query')
        self.cursor.execute(query_student, (id,))
        result_student = self.cursor.fetchone()
        print(result_student)
        

        # Check if the student exists and verify the password
        if result_student:
            stored_password = result_student[0]
            print(stored_password)
            
            if stored_password == password:
                # fetching name of student
                query_name="SELECT name FROM project.registered_students LEFT JOIN project.students ON project.registered_students.student_id = project.students.student_id where project.registered_students.id = %s"
                self.cursor.execute(query_name,(id,))
                name= self.cursor.fetchone()[0]

                print(True,"student",name)
                return True ,"student",name

        #checking if teacher exist
        query_teacher = "SELECT password FROM teachers WHERE id = %s"
        print('teacher login query')
        self.cursor.execute(query_teacher, (id,))
        result_teacher = self.cursor.fetchone()
        print(result_teacher)

        if result_teacher:
            stored_password = result_teacher[0]
            print(stored_password)
            print(password)
            
            if stored_password == password:
                query_name="SELECT name FROM project.teachers where id=%s"
                self.cursor.execute(query_name,(id,))
                name= self.cursor.fetchone()[0]
                print(True,"teacher",name)
                return True,"teacher",name
            
        return False,None,None


    def insert_question(self, exam_name,subject,exam_id, class_name, question_text, question_type, options=None, correct_answer=None, marks=0):
        try:
            query = """
            INSERT INTO questions (id,exam_name,subject,class_name, question_text, question_type, options, correct_answer, marks)
            VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)
            """
            # Execute the query
            self.cursor.execute(query, (exam_id,exam_name,subject,class_name, question_text, question_type, options, correct_answer, marks))
            self.connection.commit()
            
        except Exception as e:
            print(f"Error inserting question: {e}")
              # Rollback in case of an error

    def insert_exam_schedule(self,exam_id,exam_name, subject_name,class_name, scheduled_date, start_time, duration, teacher_id):
        

            
        query = """
        INSERT INTO exams
            (exam_id,exam_name, subject,class_name, scheduled_date, start_time, duration, teacher_id)
        VALUES (%s, %s, %s,%s, %s, %s, %s,%s)
        """
        print('crgrsgfrwfr')
        values = (exam_id,exam_name, subject_name,class_name, scheduled_date, start_time, duration, teacher_id)
        print(values)
        print('fgtgrgfr')
        self.cursor.execute(query, values)
        
        self.connection.commit()
        print('something')
        

        return "Exam scheduled successfully!"

    def fetch_exams(self):
        query = "SELECT distinct exam_name,id FROM questions"  # Replace with actual table/column names
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def fetch_subjects_by_class(self, exam_name,class_names):
        """
        Fetch subjects associated with a given exam.
        Args:
            exam_name (str): The name of the exam.
        Returns: List of subject names.
        """
        query = """
            SELECT distinct(subject)
            FROM questions
            WHERE exam_name = %s and class_name=%s
        """
        self.cursor.execute(query, (exam_name,class_names))
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_class_names_by_exam(self, exam_name):
        
        query = """
            SELECT DISTINCT class_name
            FROM questions
            WHERE exam_name = %s
        """
        self.cursor.execute(query, (exam_name,))
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_scheduled_exams(self):
        query="select * from exams"
        self.cursor.execute(query)
        return self.cursor.fetchall()



    

    def fetch_exams_by_class(self, class_name):
        """
        Fetch exams filtered by class name.
        """
        query = """
            SELECT exam_id, exam_name, subject, scheduled_date, start_time, duration,class_name
            FROM exams
            WHERE trim("th" from class_name) = %s
        """
        self.cursor.execute(query, class_name)
        return self.cursor.fetchall()
    
    def fetch_exam_id_by_subjects(self,subject,class_name,exam_name):
        query="""select distinct(id) from questions where exam_name=%s and subject=%s and class_name=%s"""
        self.cursor.execute(query,(exam_name,subject,class_name))   
        return self.cursor.fetchall()

    def fetch_class_by_student_id(self,student_id):
        query_class = """
        SELECT class_name FROM students
        RIGHT JOIN registered_students ON students.student_id = registered_students.student_id
        WHERE registered_students.id = %s
        """
        self.cursor.execute(query_class,(student_id,))
        return self.cursor.fetchone()

    def fetch_exam_questions_for_student(self,exam_id,subject,class_name):
        query=""" select question_text,question_type,options,correct_answer,marks from questions where id=%s and subject=%s and class_name=%s"""
        self.cursor.execute(query,(exam_id,subject,class_name))
        return self.cursor.fetchall()


    def store_student_responses(self, responses):
        query = """
        INSERT INTO student_responses (student_id, exam_id, question_text, response,correct_answer, marks_awarded,maximum_marks, is_checked,checkers,class_name,subject)
        VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
        """
        self.cursor.executemany(query, responses)  # Use executemany to insert multiple rows at once
        self.connection.commit()

    def save_exam_result(self, student_id, exam_id, subject, class_name, marks_obtained, total_marks):
        query = """
            INSERT INTO exam_results (student_id, exam_id, subject, class_name, marks_obtained,total_marks)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (student_id, exam_id, subject, class_name, marks_obtained, total_marks))
        self.connection.commit()
    
    def fetch_student_responses(self,class_name,subject):
        query="""select student_id,exam_id,question_id,question_text,response,marks_awarded,maximum_marks,is_checked,checkers from student_responses where class_name=%s and subject=%s"""
        self.cursor.execute(query,(class_name,subject))
        return self.cursor.fetchall()
    
    def fetch_exams_from_responses(self):
        query = "SELECT DISTINCT exam_id FROM student_responses"
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_subjects_from_responses(self):
        query = "SELECT DISTINCT subject FROM student_responses"
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_class_names_from_responses(self):
        query = "SELECT DISTINCT class_name FROM student_responses"
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]

    def fetch_students_by_exam(self, exam_id, subject, class_name):
        query = """
        SELECT DISTINCT rs.id, s.name
         FROM student_responses sr
        JOIN registered_students rs ON sr.student_id = rs.id
        JOIN students s ON rs.student_id = s.student_id
        WHERE sr.exam_id =%s AND sr.subject =%s AND sr.class_name = %s and sr.is_checked=0

        """
        self.cursor.execute(query, (exam_id, subject, class_name))
        return self.cursor.fetchall()

    def fetch_student_responses_by_exam(self, student_id, exam_id):
        query = """
        SELECT question_id, question_text, response, marks_awarded, maximum_marks, is_checked, checkers
        FROM student_responses
        WHERE student_id = %s AND exam_id = %s and is_checked=0
        """
        self.cursor.execute(query, (student_id, exam_id))
        return self.cursor.fetchall()

    def update_student_response_marks(self, student_id,teacher_id, exam_id, question_id, marks_awarded):
        print('updating marks')
        print(student_id,teacher_id, exam_id, question_id, marks_awarded)
        query = """
        UPDATE student_responses
        SET marks_awarded = %s,   is_checked = 1 , checkers=%s
        WHERE student_id = %s AND exam_id = %s AND question_id = %s
        """
        self.cursor.execute(query, (marks_awarded, teacher_id ,student_id, exam_id, question_id))
        self.connection.commit()
    
    def update_exam_result(self,student_id,exam_id,marks_obtained,total_non_mcq_marks):
        query = """
        UPDATE exam_results
        SET marks_obtained =marks_obtained+ %s,
        total_marks=total_marks+%s,
        is_complete=1
        WHERE student_id = %s AND exam_id = %s
        """
        self.cursor.execute(query, (marks_obtained,total_non_mcq_marks, student_id, exam_id))
        self.connection.commit()
    
    def fetch_exam_results_for_student(self, student_id):
        query = """
        SELECT  exams.exam_id, exams.subject,exams.exam_name,exams.class_name ,marks_obtained, total_marks,exam_results.result_date,is_complete,students.name,
        FROM exam_results 
        join exams  on exams.exam_id=exam_results.exam_id 
        JOIN registered_students  ON exam_results.student_id = registered_students.id
        JOIN students  ON registered_students.student_id = students.student_id
        where exam_results.student_id=%s
        """
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchall()

    def fetch_exam_results_for_teacher(self, class_name):
        query = """
        SELECT  exams.exam_id, exams.subject,exams.exam_name,exams.class_name ,marks_obtained, total_marks,exam_results.result_date,is_complete,students.name
        FROM exam_results 
        join exams  on exams.exam_id=exam_results.exam_id 
        JOIN registered_students  ON exam_results.student_id = registered_students.id
        JOIN students  ON registered_students.student_id = students.student_id
        WHERE exam_results.class_name=%s
        """
        self.cursor.execute(query, (class_name,))
        return self.cursor.fetchall()
    
    def fetch_class_names_for_results_for_teacher(self):
        query = """
        SELECT  class_name from exam_results """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_subjects_for_results_for_teacher(self):
        query = """
        SELECT  subject from exam_results """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_subject_wise_marks(self, student_id):
        query = """
        SELECT subject, marks_obtained, total_marks
        FROM exam_results
        WHERE student_id = %s
        """
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchall()
    
    def fetch_subject_wise_marks(self, student_id):
        query = """
        SELECT subject, marks_obtained, total_marks
        FROM exam_results
        WHERE student_id = %s
        """
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchall()

    def fetch_student_responses_by_exam_for_analysis(self, student_id, exam_id):
        query = """
        SELECT question_id, question_text, response, correct_answer, marks_awarded, maximum_marks
        FROM student_responses
        WHERE student_id = %s AND exam_id = %s
        """
        self.cursor.execute(query, (student_id, exam_id))
        return self.cursor.fetchall()

    def fetch_all_responses_by_exam_for_analysis(self, exam_id, subject, class_name):
        query = """
        SELECT student_id, question_id, response, marks_awarded
        FROM student_responses
        WHERE exam_id = %s AND subject = %s AND class_name = %s
        """
        self.cursor.execute(query, (exam_id, subject, class_name))
        return self.cursor.fetchall()