movie_query_init = '''CREATE TABLE IF NOT EXISTS Movies
    (id integer primary key AUTOINCREMENT unique not NULL,
    name varchar(100) not NULL,
    raiting real not NULL);'''

movie_query_fill = '''INSERT INTO Movies (name, raiting)
                        VALUES
                        ("The Hunger Games: Catching Fire", 7.9),
                        ("Wreck-It Ralph", 7.8),
                        ("Her", 8.3);'''


projections_query_init = '''CREATE TABLE IF NOT EXISTS Projections
    (id integer primary key AUTOINCREMENT unique not NULL,
    movie_id integer not NULL,
    type varchar(5) not NULL,
    date varchar(15) not NULL,
    time varchar(10) not NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(id));'''

projections_query_fill = '''INSERT INTO Projections (movie_id, type, date, time)
                                VALUES
                                (1, "3D", "2020-04-01", "19:10"),
                                (1, "2D", "2020-04-01", "19:00"),
                                (1, "4DX", "2020-04-02", "21:00"),
                                (3, "2D", "2020-04-05", "20:20"),
                                (2, "3D", "2020-04-02", "22:00"),
                                (2, "2D", "2020-04-02", "19:30");'''

users_query_init = '''CREATE TABLE IF NOT EXISTS Users
    (id integer primary key AUTOINCREMENT unique not NULL,
    username varchar(30) not NULL,
    password varchar(50) not NULL);'''

users_query_fill = '''INSERT INTO Users (username, password)
                        VALUES
                        ("Martin Angelov", "****"),
                        ("Ivo Donchev", "****"),
                        ("Radoslav Georgiev", "****"),
                        ("Rositza Zlateva", "****");'''

reservations_query_init = '''CREATE TABLE IF NOT EXISTS Reservations
    (id integer primary key AUTOINCREMENT unique not NULL,
    user_id integer not NULL,
    projection_id integer not NULL,
    row integer not NULL,
    col integer not NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (projection_id) REFERENCES Projections(id));'''

reservations_query_fill = '''INSERT INTO Reservations (user_id, projection_id, row, col)
                        VALUES
                        (3, 1, 2, 1),
                        (3, 1, 3, 5),
                        (3, 1, 7, 8),
                        (2, 3, 1, 1),
                        (2, 3, 1, 2),
                        (5, 5, 2, 3),
                        (6, 5, 2, 4);'''
