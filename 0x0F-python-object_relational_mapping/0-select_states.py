#!/usr/bin/python3
"""select states module"""
from sys import argv
import MySQLdb
t",
                         port=3306,
          

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhos               user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC;")
    [print(state) for state in cursor.fetchall()]
    db.close()
