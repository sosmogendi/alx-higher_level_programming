#!/usr/bin/python3
"""Deletes State objects with names containing 'a' from
the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, passwd, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query and delete State objects with names containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
