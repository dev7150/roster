import sqlite3
from sqlite3 import Error
import datetime

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_roster(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'C://Users//devashishpoudel//Desktop//Project//roster.sqlite'
    sql_create_roster_table = """CREATE TABLE IF NOT EXISTS roster(
                                    id integer PRIMARY KEY,
                                    Shift text,
                                    date text
                                    );"""
    
    roster_start_date = input("Enter the roster start date(yyyy-mm-dd): ")
    no_of_days = input("Enter the number of days: ")
    
    dates = []
    for i in range(int(no_of_days)):
        dates.append(datetime.datetime.strptime(roster_start_date, '%Y/%m/%d') + datetime.timedelta(i))
        
    print(dates)

if __name__ == '__main__':
    main()
    
    
    

