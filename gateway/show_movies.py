from utils.session_context_manager import session_scope
from models.orm_models.movie import Movie


def get_movies():
    with session_scope() as session:
        movies = session.query(Movie).all()
    return movies
