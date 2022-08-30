#!/usr/bin/python3
"""Deletes all State objects from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    """Deletes all States"""
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
