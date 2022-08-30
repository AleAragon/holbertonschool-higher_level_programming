#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa"""


if __name__ == '__main__':
    """ Module to select states"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
