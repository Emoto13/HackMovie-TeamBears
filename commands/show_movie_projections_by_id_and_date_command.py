from constants.queries_show_movie_by_id_and_date import QUERY_SHOW_MOVIE_BY_ID, QUERY_SHOW_MOVIE_BY_ID_AND_DATE
from gateway.gateway_show_movie_projections_by_id_and_date import gateway_show_movies_by_id_and_date


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections = gateway_wrapper(movie_id, date)
    if len(projections) == 0:
        raise ValueError('No projections for this movie')
    show_projections_wrapper(projections)


def gateway_wrapper(movie_id, date):
    if date is None:
        return gateway_show_movies_by_id_and_date(QUERY_SHOW_MOVIE_BY_ID, (movie_id,))
    return gateway_show_movies_by_id_and_date(QUERY_SHOW_MOVIE_BY_ID_AND_DATE, (movie_id, date))


def show_projections_wrapper(projections):
    first_projection = projections[0]

    if len(first_projection) == 4:
        print_movie_projections_for_specific_date(projections)
    print_movie_projections(projections)


# move to templates
def print_movie_projections_for_specific_date(projections):
    movie_name = projections[0][0]
    print(f"Projections for movie '{movie_name}': ")
    for projection in projections:
        print(f"[{projection[1]}] - {projection[2]} ({projection[3]})")


# move to templates
def print_movie_projections(projections):
    movie_name = projections[0][0]
    print(f"Projections for movie '{movie_name}': ")
    for projection in projections:
        print(f"[{projection[1]}] - {projection[2]} {projection[3]} ({projection[4]})")
