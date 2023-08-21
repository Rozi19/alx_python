# list all elemnt from states table in python
#import mysqldb abd sys


import MySQLdb
import sys


def main():
    #connecting with the data base
    U = sys.argv[1]
    pw = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=U, passwd=pw, db=d)
    #execute statements to communicate with the database
    cur = db.cursor()
    #execute our query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    #put the resule on a variable
    result = cur.fetchall()
    #print our result
    for state in result:
        print(state)
if __name__ == "__main__":
    main()