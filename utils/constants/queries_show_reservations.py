GET_RESERVATIONS = '''SELECT date, time, row, col,
                      Reservations.id as reservation_id, 
                      name as movie_name,
                      type as projection_type
                      FROM `Users`
                      JOIN `Reservations` ON Users.id = Reservations.user_id
                      JOIN `Projections` ON Reservations.projection_id = Projections.id
                      JOIN `Movies` ON Movies.id = Projections.movie_id
                      WHERE username = ?
                      GROUP BY Reservations.id'''
