GET_MOVIES = '''SELECT id as movie_id, name as movie_name, rating as movie_rating
                                     FROM Movies
                                     '''

GET_PROJECTIONS_BY_ID = \
    '''SELECT date, time,
       Projections.id as projection_id, name as movie_name,  type as projection_type,
       (100 - COUNT(Reservations.projection_id)) as seats_left
       FROM Movies 
       LEFT JOIN Projections ON Movies.id = Projections.movie_id 
       LEFT JOIN Reservations ON Projections.id = Reservations.projection_id
       WHERE movie_id = ? 
       GROUP BY Projections.id;'''

GET_PROJECTION_INFO = '''SELECT name as movie_name, rating as movie_rating,  type as projection_type, date, time
                         FROM Projections
                         JOIN Movies On Projections.movie_id = Movies.id
                         WHERE Projections.id = ?'''

GET_TAKEN_SEATS_BY_ROWS_AND_COLUMNS = '''SELECT row, col
                                               FROM Projections
                                               JOIN Reservations ON Projections.id = Reservations.projection_id
                                               WHERE projection_id = ?
                                               ORDER BY row;'''

GET_USER_ID_BY_USERNAME = '''SELECT id
                                    FROM Users 
                                    WHERE username = ?'''

INSERT_INTO_RESERVATIONS = '''INSERT INTO Reservations (user_id, projection_id, row, col)
                                    VALUES (?, ?, ?, ?)'''