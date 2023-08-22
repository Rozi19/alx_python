"""   displays all values in the states table of hbtn_0e_0_usa
where name matches the argument with out SQL Injection
"""

import MySQLdb
import sys


def main():
    """
    take input form the argumemnt
    connecting with the data base
    #execute statements to communicate with the database
    #execute our query
    #put the resule on a variable
    print our result
    """
    u = sys.argv[1]
    pw = sys.argv[2]
    d = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pw, db=d)
    cur = db.cursor()
    qure = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(qure, (state,))
    result = cur.fetchall()
    for statess in result:
        print(statess)
if __name__ == "__main__":
    main()
