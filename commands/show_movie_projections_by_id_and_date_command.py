from gateway.show_movie_projections_by_id_and_date import show_movies_by_id_or_date
from templates.movie_projections_by_id_and_date import display_movie_projections_for_specific_date, \
    display_movie_projections


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections = show_movies_by_id_or_date(movie_id, date)
    if len(projections) == 0:
        raise ValueError('No projections for this movie')
    show_projections_wrapper(projections, date)

def show_projections_wrapper(projections, date):
    if date is None:
        return display_movie_projections(projections)
    return display_movie_projections_for_specific_date(projections, date)
