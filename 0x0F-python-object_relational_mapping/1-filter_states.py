#!/usr/bin/python3
"""Module to list all states starting with N from database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """Module to list states starting with N"""
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE\
                 name LIKE BINARY 'N%' ORDER BY id ASC"

    cursor.execute(sql)
    states = cursor.fetchall()

    for state in states:
        print(state)
