#!/usr/bin/python3
"""
0. Get all states
mandatory
Write a script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name "
    query.join("FROM cities")
    query.join("JOIN states ON states.id = cities.state_id")
    query.join("ORDER BY cities.id ASC")

    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
