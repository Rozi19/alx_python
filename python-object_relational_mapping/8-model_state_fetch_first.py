"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL username, password, and database
    uname = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        uname, passwd, database))

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and filter the state id is 1
    state = session.query(State).order_by(State.id).first()

    # Display the results
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
