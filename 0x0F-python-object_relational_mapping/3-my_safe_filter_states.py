#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa"""


if __name__ == '__main__':
    """ Module to displays all values"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    st = sys.argv[4].split('\'')
    to = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(st[0])
    cur.execute(to)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
