from models.base import Base
from utils.session_context_manager import engine


def bootstrap():
    Base.metadata.create_all(engine)
