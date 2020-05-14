from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.orm_models.base import Base


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    engine = create_engine("sqlite:///cinema.db")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()
