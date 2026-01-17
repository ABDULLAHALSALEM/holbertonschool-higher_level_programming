#!/usr/bin/python3
"""
0-select_states.py

Lists all states from the database hbtn_0e_0_usa.
Results are sorted by states.id ASC.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and list all states ordered by id."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
