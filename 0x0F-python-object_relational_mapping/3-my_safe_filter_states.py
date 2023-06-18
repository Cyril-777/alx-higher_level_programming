#!/usr/bin/python3
"""a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    pd = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=pd, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
