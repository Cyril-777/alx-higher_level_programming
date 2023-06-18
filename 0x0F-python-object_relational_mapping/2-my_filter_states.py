#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
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

    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'"
             .format(state_name))
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
