import sqlite3
import re

sqlite_file = "C://Users//devashishpoudel//Desktop//Project//roster.sqlite"
table_name = "Unavailable"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def udates():
    emp = input("Enter the name of associate: ")
    c.execute('Select * from employees where name like ?',(emp+'%',))
    x = ((c.fetchall()))
    match = re.search('\d+', str(x[0]))
    empid = match.group()
      
    print(empid)
            
    if len(x) == 1:
        leave_start = input("Enter the leave start date: ")
        leave_end = input("Enter the leave end date: ")
        
    else:
        print("Employee does not exist")

    return None




udates()

conn.close()

    

