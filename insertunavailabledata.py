import sqlite3
from sqlite3 import Error
import re

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_task(conn, task):
    sql = '''INSERT INTO unavailable (id, begin_date, end_date) VALUES (?,?,?)'''
    c = conn.cursor()
    c.execute(sql, task)

def main():
    database = "C://Users//devashishpoudel//Desktop//Project//roster.sqlite"
    conn = create_connection(database)
    c = conn.cursor()
    emp = input("Enter the name of associate: ")
    c.execute('Select * from employees where name like ?',(emp+'%',))
    x = ((c.fetchall()))
    match = re.search('\d+', str(x[0]))
    empid = match.group()
    print(empid)
            
    if len(x) == 1:
        leave_start = input("Enter the leave start date: ")
        leave_end = input("Enter the leave end date: ")
        with conn:
            task = (empid, leave_start, leave_end)
            create_task(conn, task)           
        
    else:
            print("Employee does not exist")
            

       

if __name__ == '__main__':
    main()
