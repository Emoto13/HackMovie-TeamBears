from utils.session_context_manager import session_scope
from models.orm_models.movie import Movie
from models.orm_models.projection import Projection
from models.orm_models.reservation import Reservation


def get_movies():
    with session_scope() as session:
        movies = session.query(Movie).all()
    return movies


def get_projections_by_movie_id(movie_id):
    with session_scope() as session:
        projections = session.query(Projection).filter(Projection.movie_id == movie_id).all()
    return projections


def get_taken_seats_rows_and_columns(projection_id):
    with session_scope() as session:
        rows_and_cols = session.query(Reservation).filter(Reservation.projection_id == projection_id) \
            .with_entities(Reservation.reservation_row, Reservation.reservation_col)
    return rows_and_cols


def get_projection_by_projection_id(projection_id):
    with session_scope() as session:
        projection = session.query(Projection).filter(Projection.projection_id == projection_id).one()
    return projection


def create_new_reservation_in_the_database(reservations):
    with session_scope() as session:
        for reservation in reservations:
            session.add(reservation)
