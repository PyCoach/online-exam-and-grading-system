
import pandas as pd
import numpy as np
stu_data=pd.read_csv('files/student_basic_info.csv',index_col=["addmission_no","email"])


stu_data.index.get_level_values('name')


print(stu_data.index.get_level_values('email'))
#stu_data.to_csv("files/student_basic_info.csv")