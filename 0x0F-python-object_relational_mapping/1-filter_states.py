#!/usr/bin/python3
"""
This is a script that lists all states with name starting
with 'N' from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'"
    cur.execute(query)
    n_states = cur.fetchall()
    for state in n_states:
        print(state)
    db.close()
