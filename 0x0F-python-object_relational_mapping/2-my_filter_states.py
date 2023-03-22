#!/usr/bin/python3
"""
This script takes argument and displays all values in
a database table that matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # establish connection to the database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])
    # create cursor object execute SQL queries
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cur.execute(query, argv[4])
    matched_states = cur.fetchall()
    for state in matched_states:
        print(state)

    db.close()
