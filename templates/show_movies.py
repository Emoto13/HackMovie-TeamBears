def display_movies(movies):
    print("Current movies are:")
    for movie in movies:
        print(f'[{movie[0]}] - {movie[1]} ({movie[2]})')
