from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.orm_models.base import Base
from models.orm_models.projection import Projection
from models.orm_models.reservation import Reservation
from models.orm_models.user import User


class Movie(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String)
    movie_rating = Column(Float)

    projections = relationship("Projection", backref="movie")
