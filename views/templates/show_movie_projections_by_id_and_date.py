def display_projections(projections, date):
    if date is None:
        return display_movie_projections(projections)
    return display_movie_projections_for_specific_date(projections, date)


def display_movie_projections_for_specific_date(projections, date):
    movie_name = projections[0][0]
    print(f"Projections for movie '{movie_name}' on date {date}: ")
    for projection in projections:
        print(f"[{projection[1]}] - {projection[2]} ({projection[3]})")


def display_movie_projections(projections):
    movie_name = projections[0][0]
    print(f"Projections for movie '{movie_name}': ")
    for projection in projections:
        print(f"[{projection[1]}] - {projection[2]} {projection[3]} ({projection[4]})")
