#!/usr/bin/python3
"""
1-filter_states.py

Lists all states with a name starting with 'N' (uppercase)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and list states starting with 'N'."""
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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
