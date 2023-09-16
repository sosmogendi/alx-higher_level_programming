#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a'
    filtered_result = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print the results
    for state in filtered_result:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
