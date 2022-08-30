#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa"""


if __name__ == '__main__':
    """ Module to displays all values"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
