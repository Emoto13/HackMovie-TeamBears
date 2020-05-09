def display_projections(projections, date):
    movie_name = projections[0].movie_name
    print(f"Projections for movie '{movie_name}' {'on date ' + date if date else ''}")
    for projection in projections:
        print(f"[{projection.projection_id}] - {date + ' ' if date else ''}{projection.time}"
              f" {projection.projection_type}")
