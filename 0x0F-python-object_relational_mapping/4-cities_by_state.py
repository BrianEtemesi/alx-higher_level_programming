#!/usr/bin/python3
"""
script to list all cities from the database `hbtn_0e_4_usa`
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # create connection to database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3])

    # create a cursor object to execute SQL queries
    cur = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.states.id = states.id
    """
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    db.close()
