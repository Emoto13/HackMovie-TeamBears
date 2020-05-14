from gateway.show_movies import get_movies
from views.templates.show_movies import display_movies


def show_movies_command():
    movies = get_movies()
    display_movies(movies)
