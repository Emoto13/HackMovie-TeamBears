SHOW_PROJECTIONS_BY_MOVIE_ID_AND_DATE = '''SELECT name, Projections.id, time, type
                                     FROM Movies
                                     JOIN Projections ON Projections.movie_id = Movies.id
                                     WHERE movie_id = ?
                                     AND date = ?
                                     ORDER BY time;
                                     '''

HOW_PROJECTIONS_BY_MOVIE_ID = '''SELECT name, Projections.id, time, date, type
                                 FROM Movies
                                 JOIN Projections ON Projections.movie_id = Movies.id
                                 WHERE movie_id = ?
                                 ORDER BY date;
                                 '''
