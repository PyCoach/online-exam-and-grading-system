import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="project"
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


    def fetch(self, id, password):
        
        
        query_student = "SELECT password FROM registered_students WHERE id = %s"
        self.cursor.execute(query_student, (id,))
        result_student = self.cursor.fetchone()
        

        # Check if the student exists and verify the password
        if result_student:
            stored_password = result_student[0]
            
            if stored_password == password:
                # fetching name of student
                query_name="SELECT name FROM project.registered_students LEFT JOIN project.students ON project.registered_students.student_id = project.students.student_id where project.registered_students.id = %s"
                self.cursor.execute(query_name,(id,))
                name= self.cursor.fetchone()[0]

                return True ,"student",name


        #checking if teacher exist
        query_teacher = "SELECT password FROM teachers WHERE id = %s"
        self.cursor.execute(query_teacher, (id,))
        result_teacher = self.cursor.fetchone()
        

        if result_teacher:
            stored_password = result_teacher[0]
            
            if stored_password == password:
                query_name="SELECT name FROM project.teachers where id=%s"
                self.cursor.execute(query_name,(id,))
                name= self.cursor.fetchone()[0]
                return True,"teacher",name
            
        return False





