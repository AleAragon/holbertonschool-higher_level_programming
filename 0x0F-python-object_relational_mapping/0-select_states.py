#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()


sql = "SELECT * FROM states ORDER BY id ASC"

cursor.execute(sql)
states = cursor.fetchall()

for state in states:
    print(state)
