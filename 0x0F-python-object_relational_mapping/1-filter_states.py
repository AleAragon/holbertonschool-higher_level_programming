#!/usr/bin/python3
"""Module to list all states starting with N from database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """Module to list states starting with N"""
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
