# list all elemnt from states table in python 
#import mysqldb 

import MySQLdb
def main():
#connecting with the data base
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa")
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
