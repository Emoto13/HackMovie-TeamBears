USERS_WITH_THE_SAME_USER_NAME = 'SELECT username FROM Users WHERE username = ?'

ADD_USER_TO_DATABASE = 'INSERT INTO Users (username, password) VALUES (?, ?)'
