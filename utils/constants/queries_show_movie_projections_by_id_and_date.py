GET_PROJECTIONS_BY_MOVIE_ID_AND_DATE = '''
                                        SELECT time, 
                                        name as movie_name, 
                                        Projections.id as projection_id, 
                                        type as projection_type
                                        FROM Movies
                                        JOIN Projections ON Projections.movie_id = Movies.id
                                        WHERE movie_id = ?
                                        AND date = ?
                                        ORDER BY time;
                                        '''

GET_PROJECTIONS_BY_MOVIE_ID = '''
                                 SELECT time, date,
                                 name as movie_name, 
                                 Projections.id as projection_id,
                                 type as projection_type
                                 FROM Movies
                                 JOIN Projections ON Projections.movie_id = Movies.id
                                 WHERE movie_id = ?
                                 ORDER BY date;
                                 '''
