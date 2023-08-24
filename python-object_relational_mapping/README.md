<h1>Python - Object-relational mapping</h1>
<h2>0. Get all states</h2>
<br>
Write a script that lists all states from the database hbtn_0e_0_usa:
<br>
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
<br>You must use the module MySQLdb (import MySQLdb)
<br>Your script should connect to a MySQL server running on localhost at port 3306
<br>Results must be sorted in ascending order by states.id
<br>Results must be displayed as they are in the example below
<br>Your code should not be executed when imported
<br>
<h2>1. Filter states</h2>
<br>
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
<br>
Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
<br>You must use the module MySQLdb (import MySQLdb)
<br>Your script should connect to a MySQL server running on localhost at port 3306
<br>Results must be sorted in ascending order by states.id
<br>Results must be displayed as they are in the example below
<br>Your code should not be executed when imported
<br>
<h2>2. Filter states by user input</h2>
<br>
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
<br>
Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)<br>
You must use the module MySQLdb (import MySQLdb)<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
You must use format to create the SQL query with the user input<br>
Results must be sorted in ascending order by states.id<br>
Results must be displayed as they are in the example below<br>
Your code should not be executed when imported<br>
<h2>3. SQL Injection...</h2>
<br>
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
<br>
What? Empty?
<br>
Yes, it’s an SQL injection to delete all records of a table…
<br>
Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
<br>
Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)<br>
You must use the module MySQLdb (import MySQLdb)<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
Results must be sorted in ascending order by states.id<br>
Results must be displayed as they are in the example below<br>
Your code should not be executed when imported<br>
<h2>4. Cities by states</h2>
<br>
Write a script that lists all cities from the database hbtn_0e_4_usa
<br>
Your script should take 3 arguments: mysql username, mysql password and database name<br>
You must use the module MySQLdb (import MySQLdb)<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
Results must be sorted in ascending order by cities.id<br>
You can use only execute() once<br>
Results must be displayed as they are in the example below<br>
Your code should not be executed when imported<br>
<h2>5. All cities by state</h2>
<br>
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
<br>
Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)<br>
You must use the module MySQLdb (import MySQLdb)<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
Results must be sorted in ascending order by cities.id<br>
You can use only execute() once<br>
The results must be displayed as they are in the example below<br>
Your code should not be executed when imported<br>
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
<h2>6. First state model</h2>
State class:<br>
inherits from Base<br>
links to the MySQL table states<br>
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key<br>
class attribute name that represents a column of a string with maximum 128 characters and can’t be null<br>
You must use the module SQLAlchemy<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)<br>
<h2>7. All states via SQLAlchemy</h2>
<br>
Write a script that lists all State objects from the database hbtn_0e_6_usa
<br>
Your script should take 3 arguments: mysql username, mysql password and database name<br>
You must use the module SQLAlchemy<br>
You must import State and Base from model_state - from model_state import Base, State<br>
Your script should connect to a MySQL server running on localhost at port 3306<br>
Results must be sorted in ascending order by states.id<br>
The results must be displayed as they are in the example below<br>
Your code should not be executed when imported<br>