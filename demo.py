from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_mail import Mail, Message

import model
import sqlite3

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'jumpjacks'

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME']= 'azulvs15@gmail.com'
app.config['MAIL_PASSWORD']= 'sassureHqZ7776'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
username = ''
user = model.check_users()


@app.route('/', methods = ['GET', "POST"])
def home():
    if 'username' in session:
        g.user=session['username'] 
        return render_template('homepage.html')
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])

def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = request.form['username']
        pwd = model.check_pw(areyouuser)
        
        if request.form['password'] == pwd:
            username = request.form['username']
            connection = sqlite3.connect('flask.db', check_same_thread = False)
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM user WHERE username = '{username}';""".format(username = username))
            session['username'] = request.form['username']
            session['usuario'] = cursor.fetchall()
            print (session)
            return redirect(url_for('home'))
        else:
            return render_template('index-alert.html')
    return render_template('index.html')

  

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   
    if request.method == 'GET':
         message = 'Please sign up!'
         return render_template('signup.html', message = message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        favorite_color = request.form["favorite_color"]
        message = model.signup(username, password, favorite_color)
        msg = Message('TuHogarApp', sender='azulvs15@gmail.com', recipients=[username])
        msg.html = """ <body>  <div class="column">
         <div style="text-align: center; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); padding: 16px; background-color:#FFFF" class="card"><h1 style="color: #FFFF"><a href="https://imgbb.com/"><img src="https://i.ibb.co/Nj6M9ZS/img.png" alt="img" border="0"></a></h1></div>
            </div> <p style="text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: medium;">Gracias por confiar en nosotros. Por favor verifica tu cuenta para poder usar la app. <br><br> <a href="http://localhost:7000/email-verif" style="color: #CD7034;">Verificar mi cuenta</a> </p> </div> </body>
         """
        mail.send(msg)
        return render_template("email.html")


@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('usuario', None)
    return redirect(url_for('home'))

@app.route('/comofunciona')
def suma():
    return render_template("comofunciona.html")

@app.route('/quienes')
def quienes():
    return render_template("quienes.html")

@app.route('/albanil')
def servicio():
     if 'username' in session:
        g.user=session['username'] 
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM user WHERE detalles = "Albanil"')
        data = cursor.fetchall()
        return render_template('albanil.html', output_data = data)
        

     return render_template('ingresar.html')

@app.route('/electricista')
def servicio1():
     if 'username' in session:
        g.user=session['username'] 
        return render_template('electricista.html')

     return render_template('ingresar.html')

@app.route('/perfil')
def perfil():
     if 'username' in session:
        g.user=session['username'] 
        print (session['username'])
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()
        cursor.execute("SELECT favorite_color FROM user WHERE favorite_color='Profesional'")
        if cursor.fetchone():

                return render_template('perfil.html')
                connection.commit()
                cursor.close()
                connection.close()
               
        return render_template('nonprofesional.html')
        
                
     return render_template('nonprofesional.html')

 

@app.route('/navbar')
def navbar():
    return render_template("navbar.html")

@app.route('/email-verif')
def envio1():
    return render_template("email-verif.html")

@app.route('/my_form', methods=['POST'])
def my_form():
    if request.method == 'POST':
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()
        username = request.form["username"]
        password = request.form["password"]
        favorite_color = request.form["favorite_color"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        numContacto = request.form["numContacto"]
        dire = request.form["dire"]
        dirNum = request.form["dirNum"]
        postal = request.form["postal"]
        pais = request.form["pais"]
        ciudad = request.form["ciudad"]
        message = model.form(username, password, favorite_color, nombre, apellido, numContacto, dire, dirNum, postal, pais, ciudad)
        return render_template('perfil.html')
    
@app.route('/my_form1', methods=['POST'])
def my_form1():
    if request.method == 'POST':
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()

        username = session['username']
        experiencia = request.form["experiencia"]
        detalles = request.form["detalles"]
        
        message = model.form1(username, experiencia, detalles)
        return render_template('perfil.html')

@app.route('/my_pass', methods=['POST'])
def my_pass():
    if request.method == 'POST':
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']
        message = model.passw(username, password)

        return render_template('index-pass.html')



@app.route('/password2', methods=['GET','POST'])
def password2():   
    if request.method == 'POST':
        session.pop('username', None)
        username = request.form['username']
        connection = sqlite3.connect('flask.db', check_same_thread = False)
        cursor = connection.cursor()
        cursor.execute(""" SELECT username FROM user WHERE username = '{username}'; """ .format(username = username))
        exist = cursor.fetchone()
        print(exist)
        if exist:
            msg = Message('TuHogarApp', sender='azulvs15@gmail.com', recipients=[username])
            msg.html = """<body> 
            <div style="text-align: center; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); padding: 16px; background-color:#FFFF" class="card"><h1 style="color: #FFFF"><a href="https://imgbb.com/"><img src="https://i.ibb.co/Nj6M9ZS/img.png" alt="img" border="0"></a></a></h1></div>
            </div> <p style="text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: medium;" >Ingrese al link para recuperar tu cuenta en TuHogarApp. <br><br> <a href="http://localhost:7000/cambiarpassword" style="color: #CD7034;">Recuperar mi cuenta</a> </p> </div></body>
            """
            mail.send(msg)
            return redirect(url_for('password'))
        else:
            return render_template('nonprofesional.html')
    return render_template('password2.html')

@app.route('/password')
def password():
    return render_template("password.html")

@app.route('/cambiarpassword')
def cpassword():
    return render_template("cambiarpassword.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 7000, debug = True)
