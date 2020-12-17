#!/usr/bin/python3
"""
a script that list databases
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", passwd=argv[2], user=argv[1],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
