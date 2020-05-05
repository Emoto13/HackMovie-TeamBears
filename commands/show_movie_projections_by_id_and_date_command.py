from constants.queries_show_movie_by_id_and_date import QUERY_SHOW_MOVIE_BY_ID, QUERY_SHOW_MOVIE_BY_ID_AND_DATE
from gateway.gateway_show_movie_projections_by_id_and_date import gateway_show_movies_by_id_and_date
from templates.templates_show_movie_projections_by_id_and_date import display_movie_projections_for_specific_date, \
    display_movie_projections


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections = gateway_wrapper(movie_id, date)
    if len(projections) == 0:
        raise ValueError('No projections for this movie')
    show_projections_wrapper(projections, date)


def gateway_wrapper(movie_id, date):
    if date is None:
        return gateway_show_movies_by_id_and_date(QUERY_SHOW_MOVIE_BY_ID, (movie_id,))
    return gateway_show_movies_by_id_and_date(QUERY_SHOW_MOVIE_BY_ID_AND_DATE, (movie_id, date))


def show_projections_wrapper(projections, date):
    if date is None:
        return display_movie_projections(projections)
    return display_movie_projections_for_specific_date(projections, date)
