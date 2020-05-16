from utils.session_context_manager import session_scope
from models.projection import Projection


def get_movies_by_id_or_date(movie_id, date):
    if date is None:
        return get_movie_projections_by_movie_id(movie_id)
    return get_movie_projections_by_movie_id_and_date(movie_id, date)


def get_movie_projections_by_movie_id(movie_id):
    with session_scope() as session:
        projections = session.query(Projection).filter(Projection.movie_id == movie_id).all()
    return projections


def get_movie_projections_by_movie_id_and_date(movie_id, date):
    with session_scope() as session:
        projections = session.query(Projection). \
            filter(Projection.movie_id == movie_id). \
            filter(Projection.projection_date == date).all()
    return projections
