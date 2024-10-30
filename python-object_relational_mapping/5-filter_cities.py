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

    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s"
                "ORDER BY cities.id ASC", (argv[4], ))
    query_rows = cur.fetchall()
    results = []
    for row in query_rows:
        if row[2] == argv[4]:
            results.append(row[1])
    print(", ".join(results))
    cur.close()
    conn.close()
