#!/usr/bin/python3
"""Module to list all states starting with N from database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """Module to list states starting with N"""
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
        host='localhost', port=3306)

    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states ORDER BY id ASC;')

    states = cursor.fetchall()
    for state in states:
        if state[1].startswith('N'):
            print(state)
