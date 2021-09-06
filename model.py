import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def show_color(username):
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT favorite_color FROM user WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    color = cursor.fetchone()[0] 

    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s favorite color is {color}.'.format(username=username, color=color)
    return message

def check_pw(username):
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT password FROM user WHERE username='{username}' ORDER BY pk DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password

def check_users():
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT username FROM user ORDER BY pk DESC; """)
    db_user = cursor.fetchall()
    user = []

    for i in range(len(db_user)):
        person = db_user[i][0]
        user.append(person) 

    connection.commit()
    cursor.close()
    connection.close()
    return user

def signup(username, password, favorite_color):
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM user WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute("""INSERT INTO user(username, password, favorite_color)VALUES('{username}', '{password}', '{favorite_color}');""".format(username =username, password = password, favorite_color = favorite_color))
        connection.commit()
        cursor.close()
        connection.close() 

    else:
        return ('User already existed!!')

    return 'You have succesfully signed up!!!'

def form(username, password, favorite_color, nombre, apellido, numContacto, dire, dirNum, postal, pais, ciudad):
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM user WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone()

    if exist:
        cursor.execute("""UPDATE user SET username = '{username}' , password = '{password}', favorite_color = '{favorite_color}',  nombre = '{nombre}', apellido = '{apellido}', numContacto= '{numContacto}' , dire= '{dire}' ,dirNum= '{dirNum}' ,postal = '{postal}' , pais= '{pais}' ,ciudad= '{ciudad}' WHERE username = '{username}';""".format(username =username, password = password, favorite_color = favorite_color, nombre =nombre, apellido = apellido, numContacto = numContacto, dire = dire , dirNum = dirNum, postal = postal,  pais = pais, ciudad = ciudad))
        connection.commit()
        cursor.close()
        connection.close() 

    else:
        return ('aaaaa')

    return 'Changes made!!!'

def form1(username, experiencia, detalles):
    connection = sqlite3.connect('flask.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM user WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone()

    if exist:
        cursor.execute("""UPDATE user SET experiencia= '{experiencia}', detalles= '{detalles}' WHERE username = '{username}';""".format(username= username, experiencia = experiencia, detalles = detalles))
        connection.commit()
        cursor.close()
        connection.close() 

    else:
        return ('aaaaa')

    return 'Changes made!!!'