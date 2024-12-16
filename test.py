from db import Database
db=Database()
data=db.fetch_scheduled_exams()

row_count=0
for rows in range(len(data)):
    row=data[row_count]
    print(row)
    row_count+=1
