import pandas as pd
import numpy as np

class Database:
    def insert(self, name,email,dob,adm_no,user_id,password):
        stu_data=pd.read_csv('files/student_basic_info.csv',index_col=["addmission_no","email"])
        if adm_no not in stu_data.index.get_level_values('adm_no'):
            if email not in stu_data.index.get_level_values('email'):
                if adm_no not in stu_data.index.get_level_values('adm_no'):
                    new_data=pd.DataFrame([])
                else:
                    return "user with admission_no already existd"

            else:
                return "email already exists"
            
        else:
            return "user already exists"









