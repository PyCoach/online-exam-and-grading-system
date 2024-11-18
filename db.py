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

    def insert(self, adm_no,email, password):

        # Check if the admission number exists in the students table
        query_check_adm_no = "SELECT adm_no FROM students WHERE adm_no = %s"
        self.cursor.execute(query_check_adm_no, (adm_no,))
        result_check_adm_no= self.cursor.fetchone()

        
        if not result_check_adm_no:
            return f"<p style='color: red; font-size: 50px;'>Admission number '{adm_no}' does not exist .</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"

        #checking if email exists in students table
        query_check_email = "SELECT email FROM students WHERE email = %s"
        self.cursor.execute(query_check_email, (email,))
        result_check_email = self.cursor.fetchone()

        
        if not result_check_email:
            return f"<p style='color: red; font-size: 50px;'>email '{email}' does not exist .</p><p style='font-size: 50px;'><br> <a  href='/register'>click here</a> to register again </p>"


        # Check if the admission number already exists in the users table
        query_check_user = "SELECT adm_no FROM users WHERE adm_no = %s"
        self.cursor.execute(query_check_user, (adm_no,))
        record = self.cursor.fetchone()


        
        if record:
            return f"User already exists for Admission Number: {adm_no}."

        # Get the last user_id from the users table
        query_last_user_id = "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1"
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
        INSERT INTO users (adm_no, user_id, password)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query_insert_user, (adm_no, new_user_id, password))
        self.connection.commit()

        return f"<p style='font-size:40px'>User registered successfully with  <p style='color:blue; font-size:50px'>User ID:{new_user_id}  <a  href='/'>click here</a> to go to login page </p>"

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


    def fetch(self, user_id, password):
        
        
        query = "SELECT password FROM users WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        

        # Check if the user exists and verify the password
        if result:
            stored_password = result[0]
            
            if stored_password == password:
                return True
            elif stored_password!= password:
                return "pass not found"

        return False





