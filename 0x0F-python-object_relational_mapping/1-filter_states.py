#!/usr/bin/python3
""" script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    pd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, passwd=pd, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
