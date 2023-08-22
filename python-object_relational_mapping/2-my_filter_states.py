"""   displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    stat = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pw, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name= '{}' COLLATE utf8mb4_bin"
                .format(stat))
    result = cur.fetchall()
    for statess in result:
        print(statess)
if __name__ == "__main__":
    main()
