#!/usr/bin/python3
"""
2-my_filter_states.py

Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument exactly (case-sensitive).
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and display matching states."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC;"
    ).format(state_name)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
