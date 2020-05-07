QUERY_MOVIES_WITH_AVAILABLE_SEATS = '''SELECT id, name, rating
                                       FROM Movies
                                       '''

QUERY_GET_PROJECTIONS_BY_ID = \
    '''SELECT Projections.id, Movies.name, date, time, type, (100 - COUNT(Reservations.projection_id)) as places_left
       FROM Movies 
       LEFT JOIN Projections ON Movies.id = Projections.movie_id 
       LEFT JOIN Reservations ON Projections.id = Reservations.projection_id
       WHERE movie_id = ? 
       GROUP BY Projections.id;'''

QUERY_GET_PROJECTION_INFO = '''SELECT name, rating, date, time, type 
                               FROM Projections
                               JOIN Movies On Projections.movie_id = Movies.id
                               WHERE Projections.id = ?'''

QUERY_GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS = '''SELECT row, col
                                            FROM Projections
                                            JOIN Reservations ON Projections.id = Reservations.projection_id
                                            WHERE projection_id = ?
                                            ORDER BY row;'''

QUERY_GET_USER_ID_BY_USERNAME = '''SELECT id
                                    FROM Users 
                                    WHERE username = ?'''

QUERY_INSERT_INTO_RESERVATIONS = '''INSERT INTO Reservations (user_id, projection_id, row, col)
                                    VALUES (?, ?, ?, ?)'''