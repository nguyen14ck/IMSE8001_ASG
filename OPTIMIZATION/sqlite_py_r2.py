#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      admin
#
# Created:     07/10/2014
# Copyright:   (c) admin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sqlite3 as sql
import os
import random
import rpy2.robjects as ro
r = ro.r

#CREATE OR OPEN DATABASE
db = sql.connect('py_r_db')
db.row_factory = sql.Row #use to access column by name (otherwise, column must be accessed by index)

#CREATE TABLE
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE CSV(x1 REAL , x2 REAL, x3 REAL, x4 REAL)

''')
db.commit()



#INSERT VALUES TO COLUMNS: x1, x2
for i in range(1,30,1):
    x1 = random.random()
    x2 = random.randint(1,200)
    cursor.execute('''INSERT INTO CSV(x1,x2)
                  VALUES(?,?)''', (x1,x2))
db.commit()


#READ AGAIN VALUES x1, x2 FROM DATABASE => UPDATE TO X3, X4
cursor.execute('''SELECT rowid, x1, x2 FROM CSV''')
rows = map(lambda t: t, cursor.fetchall())
for row in rows:
    x1 = row['x1']
    x2 = row['x2']
    x3 = x1 + x2
    x4 = x2 - x1
    cursor.execute('''UPDATE CSV SET x3 = ?, x4 = ? WHERE rowid = ? ''', (x3, x4, row['rowid']))

db.commit()


#CALL R TO READ TABLE CSV FROM SQLITE
##pi = ro.r['pi']
rlib = ro.r['library']
rlib('RSQLite')

##rdv = ro.r['dbDriver']
##drirver = rdv('SQLite')
dbcon = ro.r['dbConnect']
con = dbcon(driver = "SQLite", dbname = "E:/temp/GitEye-1.8.0-windows.x86_64/GIT/IMSE8001_ASG/OPTIMIZATION/py_r_db")


