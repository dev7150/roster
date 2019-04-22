#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:39:51 2019

@author: x270
"""

import sqlite3

sqlite_file = '/home/x270/Desktop/Python/roster.sqlite'
table_name1 = 'employees'  # name of the table to be created  
table_name2 = 'shift'
new_field = 'id' # name of the column
field_type = 'INTEGER'  # column data type


conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

conn.commit()
conn.close()
