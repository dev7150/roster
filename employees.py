import sqlite3

sqlite_file = "C://Users//devashishpoudel//Desktop//Project//roster.sqlite"
table_name1 = 'employees'
id = 'employeeid'
new_column1 = 'name'  # name of the new column
new_column2 = 'skill'  # name of the new column
column_type = 'INTEGER' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
field_type = 'TEXT'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=id, ft=column_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=table_name1, cn=new_column1, ct = field_type))

# A) Adding a new column for skill
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=new_column2, ct=field_type))





conn.commit()
conn.close()




