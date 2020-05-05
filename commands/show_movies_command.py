from gateway.show_movies_gateway import show_movies_sorted


def show_movies_command():
    sorted_movies = show_movies_sorted()
    print("Current movies are:")
    movie_id = 1
    for movie in sorted_movies:
        print(f'[{movie_id}] - {movie[1]} ({movie[2]})')
        movie_id += 1
