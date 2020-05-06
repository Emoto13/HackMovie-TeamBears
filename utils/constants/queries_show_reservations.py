SHOW_RESERVATIONS = '''SELECT Reservations.id, name, date, time, type, row, col
                        FROM `Users`
                        JOIN `Reservations` ON Users.id = Reservations.user_id
                        JOIN `Projections` ON Reservations.projection_id = Projections.id
                        JOIN `Movies` ON Movies.id = Projections.movie_id
                        WHERE username = ?
                        GROUP BY Reservations.id'''
