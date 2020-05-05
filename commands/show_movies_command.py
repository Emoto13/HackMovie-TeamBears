from gateway.gateway_show_movies import show_movies_sorted


def show_movies_command():
    sorted_movies = show_movies_sorted()
    # move to templates later
    print("Current movies are:")
    for movie in sorted_movies:
        print(f'[{movie[0]}] - {movie[1]} ({movie[2]})')
