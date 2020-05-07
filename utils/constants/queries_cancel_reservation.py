DELETE_FROM_TABLE = 'DELETE FROM Reservations WHERE id = ?'

GET_RESERVATION_BY_USER_NAME_AND_RESERVATION_ID = '''SELECT Reservations.id
                                                     FROM `Reservations` 
                                                     JOIN `Users` ON Users.id = Reservations.user_id
                                                     WHERE username = ?
                                                     AND Reservations.id = ?'''

GET_ALL_RESERVATIONS_BY_USER_NAME = '''SELECT Reservations.id
                                      FROM `Reservations` 
                                      JOIN `Users` ON Users.id = Reservations.user_id
                                      WHERE username = ?'''
