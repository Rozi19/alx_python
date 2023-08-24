"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL username, password, and database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database))

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and sort in ascending order by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state1 in states:
        print("{}: {}".format(state1.id, state1.name))
