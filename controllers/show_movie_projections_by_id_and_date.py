from gateway.show_movie_projections_by_id_and_date import get_movies_by_id_or_date
from views.templates.show_movie_projections_by_id_and_date import display_projections
from verification.show_movie_projections_by_id_and_date import verify_projections


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections = get_movies_by_id_or_date(movie_id, date)
    verify_projections(projections)
    display_projections(projections, date)
