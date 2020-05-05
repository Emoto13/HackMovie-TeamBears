from gateway.gateway_show_movies import show_movies_sorted
from templates.templates_show_movies import display_movies


def show_movies_command():
    sorted_movies = show_movies_sorted()
    display_movies(sorted_movies)
