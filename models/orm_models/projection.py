from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.orm_models.base import Base


class Projection(Base):
    __tablename__ = "projections"
    projection_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'))
    projection_type = Column(String)
    projection_date = Column(String)
    projection_time = Column(String)

    reservations = relationship("Reservation", backref="projection")
