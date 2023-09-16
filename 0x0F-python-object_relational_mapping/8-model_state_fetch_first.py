#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object
    f_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if the table is empty
    if f_state:
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
