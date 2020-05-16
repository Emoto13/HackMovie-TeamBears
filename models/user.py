from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_password = Column(String)
