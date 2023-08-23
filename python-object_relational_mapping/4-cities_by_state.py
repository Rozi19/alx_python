""" lists all cities from the database
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
    db=MySQLdb.connect(host="localhost", port=3306, user=u, passwd=pw, db=d)
    curs = db.cursor()
    qurer = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON state_id=states.id ORDER BY cities.id ASC"
    curs.execute(qurer)
    result = curs.fetchall()
    for city in result:
        print(city)
    curs.close()
    db.close()
if __name__ == "__main__":
    main()