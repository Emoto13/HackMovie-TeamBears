from gateway.show_movies import show_movies_sorted
from views.templates.show_movies import display_movies


def show_movies_command():
    sorted_movies = show_movies_sorted()
    display_movies(sorted_movies)
