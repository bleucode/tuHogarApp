import sqlite3 

connection = sqlite3.connect('flask.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO user(
        username,
        password,
        favorite_color
        )VALUES(
            'Ironman',
            'Tony',
            'Gold'
    );"""
)


connection.commit()
cursor.close()
connection.close()