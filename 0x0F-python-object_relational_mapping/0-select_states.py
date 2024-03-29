#!/usr/bin/python3
"""
implementation of a script that lists all states
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)

    db.close()
