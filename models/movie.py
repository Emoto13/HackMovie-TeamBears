from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from models.base import Base


class Movie(Base):
    __tablename__ = "movies"
    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String)
    movie_rating = Column(Float)

    projections = relationship("Projection", backref="movie")
