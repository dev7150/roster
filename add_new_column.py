#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:36:46 2019

@author: x270
"""

import sqlite3

sqlite_file = '/home/x270/Desktop/Python/roster.sqlite'    # name of the sqlite database file
table_name = 'employees'   # name of the table to be created
id_column = 'employeeid' # name of the PRIMARY KEY column
new_column1 = 'skill'  # name of the new column
new_column2 = 'Available'  # name of the new column
date_col = 'date'
time_col = 'time'
date_time_col = 'date_time'
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'Yes' # a default value for the new column rows

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn = table_name, cn=id_column, ct=column_type))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

# B) Adding a new column with a date
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=date_col, ct=column_type, df=default_val))
# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=time_col, ct=column_type))
# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=date_time_col, ct=column_type))




# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
