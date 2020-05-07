from gateway.show_movie_projections_by_id_and_date import show_movies_by_id_or_date
from templates.show_movie_projections_by_id_and_date import display_projections
from verification.show_movie_projections_by_id_and_date import verify_projections


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections = show_movies_by_id_or_date(movie_id, date)
    verify_projections(projections)
    display_projections(projections, date)
