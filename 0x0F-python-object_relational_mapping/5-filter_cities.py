#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all
cities of that state in the database `hbtn_0e_4_usa`
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # create a connection to the database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])

    # create a cursor object to execute SQL queries
    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    WHERE states.name = %s
    JOIN states ON cities.state_id = states.id
    """
    cur.execute(query, (argv[4]))
    cities = cur.fetchall()
    length = len(cities)
    for i in range(length):
        if (i == length - 1):
            print(cities[i])
        else:
            print(cities[i], end=", ")
    db.close()
