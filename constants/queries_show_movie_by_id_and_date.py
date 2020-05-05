QUERY_SHOW_MOVIE_BY_ID_AND_DATE = '''SELECT name, Projections.id, time, type
                                     FROM Movies
                                     JOIN Projections ON Projections.movie_id = Movies.id
                                     WHERE movie_id = ?
                                     AND date = ?
                                     ORDER BY time;
                                     '''

QUERY_SHOW_MOVIE_BY_ID = '''SELECT name, Projections.id, time, date, type
                            FROM Movies
                            JOIN Projections ON Projections.movie_id = Movies.id
                            WHERE movie_id = ?
                            ORDER BY date;
                            '''
