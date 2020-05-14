# from utils.database_communication import DataBaseCommunication
# from utils.constants.queries_show_movie_projections_by_id_and_date import GET_PROJECTIONS_BY_MOVIE_ID,\
#     GET_PROJECTIONS_BY_MOVIE_ID_AND_DATE
from utils.session_context_manager import session_scope
from models.orm_models.projection import Projection
from models.orm_models.movie import Movie


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
