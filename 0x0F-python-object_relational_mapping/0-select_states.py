#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

db = MySQLdb.connect(host='127.0.0.1:3306', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
query = "SELECT * FROM hbtn_0e_0_usa ORDER BY state.id ASC"
cur.execute(query)
results = cur.fetchall()
for row in results:
    print(row)

db.close()
