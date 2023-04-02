from flask import Flask
from flask import render_template,url_for,request,session,redirect
from flask_mysqldb import MySQL
from datetime import datetime
import numpy as np
import pickle

app = Flask (__name__)
app.secret_key = "super secret key"
# Required

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "database"
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


#route so that you don't get 404 error when you browse the url
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html',username = session['username'])                               

   
@app.route('/login',methods = ['POST','GET'])
def login():
    msg = ''
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users where username = %s AND password = %s ',(username,password,))
        record = cur.fetchone()
        print(record)
        if record:
            session['loggedin'] = True
            session['username'] = record['username']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password. Try again!'
            return render_template('index.html',msg = msg)
    
@app.route('/logout',methods = ['POST','GET'])
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/predict', methods = ['POST',"GET"])
def predict():
    msg = ''
    if (request.method == 'POST'):
       
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['angina'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        blood_sugar =int(request.form['blood_sugar'])
        ecg = int(request.form['ecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        query = np.array([age,sex,cp,trestbps,chol,blood_sugar,ecg,thalach,exang,oldpeak,slope, ca,thal])
        with open(r"dtmodel.pkl","rb") as inputfile:
            model = pickle.load(inputfile)
        pred = model.predict(query.reshape(1,-1))
        if pred == 0:
            msg = 'Absence of Heart Disease'
        else:
            msg = 'Presence of Heart Disease'
        
        return render_template('home.html',msg = msg)
    
@app.route('/register',methods = ['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * from users WHERE username = %s',(username,))
        account = cur.fetchone()
        if account : 
            msg = 'This user already exists!'
        else:
            cur.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)',(username,password,email))
            mysql.connection.commit()
            msg = 'You have successfully registered.'
    return render_template('registration.html',msg = msg)
 



if __name__ == "__main__":
    app.run(debug = True)#errors show up on the webpage
