"""lists all states with a name starting with N (upper N) from the database
import mysqldb abd sys
"""

import MySQLdb
import sys


"""
    connecting with the data base
    #execute statements to communicate with the database
    #execute our query
    #put the resule on a variable
    print our result
"""
U = sys.argv[1]
pw = sys.argv[2]
d = sys.argv[3]
db = MySQLdb.connect(host="localhost", port=3306, user=U, passwd=pw, db=d)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_bin")
result = cur.fetchall()
for state in result:
    print(state)
cur.close()
db.close()
