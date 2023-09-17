#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
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

    # Retrieve the State object with id 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the State object exists
    if state_to_update:
        # Update the name of the State to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
