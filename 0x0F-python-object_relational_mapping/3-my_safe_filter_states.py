#!/usr/bin/python3
"""
This script takes an argument and displays all values in
the 'states' hbtn_0e_0_usa database table whose names matches the argument
The script should be safe from SQL Injections
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # create a connection to the database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])

    # create a curser object to execute SQL queries
    cur = db.cursor()

    """
    define an SQL query with a parameter placeholder
    a parameter placeholder is one of the measures used to prevent
    an SQL Injection
    """
    query = "SELECT * FROM states WHERE BINARY name = %s"

    # execute query
    cur.execute(query, (argv[4],))
    matched_states = cur.fetchall()
    for state in matched_states:
        print(state)
    db.close()
