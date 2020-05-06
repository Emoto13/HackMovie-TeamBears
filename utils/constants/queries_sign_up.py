USER_NAME_UNIQUENESSS = 'SELECT username FROM Users WHERE username = ?'

ADD_USER_TO_DATABASE = 'INSERT INTO Users (username, password) VALUES (?, ?)'
