import sqlite3
import csv
import re

sqlite_file = "C://Users//devashishpoudel//Desktop//Project//roster.sqlite"
table_name1 = 'employees'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

with open("C://Users//devashishpoudel//Downloads//SMARTEDGE Service Portal 23_04_2019 08-46-11 AM (1).csv") as f:
    for row in f:
        f_name = re.search(r'\w*,\w*', row)
        full_name = ''.join(f_name.group())
        #print(full_name)
        
        eid = re.search(r'\d+', row)
        emp_id = eid.group()
        #print(emp_id)
        sk = re.search(r'([A-Z]{3,})+(-([A-Z]{3,}))?(-([A-Z]{3,}))?' , row)
        skill = sk.group()
        #print(skill)
        sql = ('''INSERT OR IGNORE INTO employees (employeeid, name, skill) VALUES(?,?,?)''')
        c.execute(sql, (emp_id, full_name, skill))

conn.commit()
conn.close()
        
        
        
        
    
        
    
        



        

