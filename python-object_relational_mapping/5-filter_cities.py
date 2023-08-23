""" takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
import sys
import MySQLdb


def main():
    """
    take input form the argumemnt
    connecting with the data base
    execute statements to communicate with the database
    execute our query
    put the resule on a variable
    print our result
    """
    u = sys.argv[1]
    pw = sys.argv[2]
    d = sys.argv[3]
    s = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pw, db=d)
    curs = db.cursor()
    qurer = "SELECT name FROM cities\
        WHERE state_id=(SELECT id FROM states WHERE name=%s)\
        ORDER BY cities.id ASC"
    curs.execute(qurer, (s,))
    result = curs.fetchall()
    for city in result:
        if city != result[-1]:
            print("{}, ".format(city[0]), end="")
        else:
            print("{}".format(city[0]))
    curs.close()
    db.close()
if __name__ == "__main__":
    main()
