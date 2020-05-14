from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.orm_models.base import Base


class Reservation(Base):
    __tablename__ = "reservations"
    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    projection_id = Column(Integer, ForeignKey('projections.projection_id'))
    reservation_row = Column(Integer)
    reservation_col = Column(Integer)

    users = relationship("User", backref="reservations")
