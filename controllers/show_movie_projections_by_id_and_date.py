from gateway.show_movie_projections_by_id_and_date import get_movies_by_id_or_date
from models.data_models.projection import Projection
from views.templates.show_movie_projections_by_id_and_date import display_projections
from verification.show_movie_projections_by_id_and_date import verify_projections


def show_movie_projections_by_id_and_date(movie_id, date=None):
    projections_raw_data = get_movies_by_id_or_date(movie_id, date)
    verify_projections(projections_raw_data)
    projections = map_projections(projections_raw_data)
    display_projections(projections, date)


def map_projections(projections_raw_data):
    return list(map(lambda props: Projection.create_model(props), projections_raw_data))
