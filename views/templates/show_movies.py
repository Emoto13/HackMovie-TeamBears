def display_movies(movies):
    print("Current movies are:")
    for movie in movies:
        print(f"[{movie.movie_id}] - {movie.movie_name} ({movie.movie_rating})")
