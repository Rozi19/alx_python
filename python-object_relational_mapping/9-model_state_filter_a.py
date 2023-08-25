from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":
    # Get MySQL username, password, and database
    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    # Create the database engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, passwd, database))
 
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and filter the state name contins a
    state = session.query(State).filter(States.name.like('%a%')).all()

    # Display the results
    for state1 in state:
        print("{}: {}".format(state1.id, state1.name))
