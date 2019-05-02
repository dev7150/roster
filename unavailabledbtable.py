import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'C://Users//devashishpoudel//Desktop//Project//roster.sqlite'
    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS unavailable(
                                    id integer PRIMARY KEY,
                                    begin_date text,
                                    end_date text
                                    );"""
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print("Error cant create dB connection")

if __name__ == '__main__':
    main()
            
        
