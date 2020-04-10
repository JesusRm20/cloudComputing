from flask import Flask, jsonify, json, redirect, url_for, render_template, request, flash, session
import userClasses
import passwordHash
import task
import numpy as np

app = Flask(__name__)
app.secret_key = "Jesus"
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    name = ''
    if request.method == 'POST':
        usr = request.form
        resp = userClasses.addUser(usr)
        if resp:
            flash('The account has been created successfully' , 'info')
            return redirect(url_for('login', name=usr['firstName']))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<name>', methods=['GET', 'POST'])
def login(name=None):
    if request.method == 'POST':
        
        usr = request.form['userName']
        password = request.form['password']
        resp = userClasses.verUser(usr)
        if resp != '':
            ver = passwordHash.passwordCheck(password, resp) 
            if ver:
                session['usr'] = usr
                flash('You have been logged in successfully' , 'info')
                return  redirect(url_for('home'))
            else:
                flash('User name or password incorrect' , 'error')
                return render_template('login.html', name=name)  
        else:
            flash('User name or password incorrect' , 'error')
            return render_template('login.html', name=name)        
    else:
        if name:
            # session.pop('usr')
            return render_template('login.html', name=name)
        else:
            if 'usr' in session:
                return  redirect(url_for('home'))
            else:
                return render_template('login.html', name=name)

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'usr' in session:
        resp = task.getStreestLevelCrimes()
        return render_template('home.html', obj=resp)
    else:
        return  redirect(url_for('login'))

@app.route('/getcrimes', methods=['GET'])
def getCrimes():
    result = []
    resp = task.getStreestLevelCrimes()
    for i in resp:
        result.append(i.__dict__)
    result = np.array(result)
    return jsonify(result)
             

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)