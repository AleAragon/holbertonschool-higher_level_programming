#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3],
        host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
