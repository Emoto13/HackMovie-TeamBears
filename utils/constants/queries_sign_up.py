USER_NAME_UNIQUENESS = 'SELECT username FROM Users WHERE username = ?'

ADD_USER_TO_DATABASE = 'INSERT INTO Users (username, password) VALUES (?, ?)'
