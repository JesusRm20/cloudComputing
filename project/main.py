from flask import Flask, jsonify, json, redirect, url_for, render_template, request, flash, session
import requests
import userClasses
import passwordHash
import task
import numpy as np

app = Flask(__name__)
app.secret_key = "Jesus"
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        usr = request.form
        resp = userClasses.addUser(usr)
        if resp:
            flash('The account has been created successfully' , 'info')
            return redirect(url_for('login'))
        return resp
    else:
        return render_template('signup.html')

@app.route('/load', methods=['GET','POST'])
def loadCrimes():
    if request.method == 'POST':
        date = request.form['date']
        res = task.selectCrimeByDate(date)
        if res > 0:
            flash('Crimes for this date already exist.' , 'info')
            return render_template('loadCrimes.html')
        else:
            crimeDetails = task.loadStreetLevelCrimes(date)
            flash('Crimes loaded successfully.' , 'info')
            return render_template('loadCrimes.html')
    else:
        if 'usr' in session:
            return render_template('loadCrimes.html') 
        else:
            return  redirect(url_for('login'))

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
                return render_template('login.html')  
        else:
            flash('User name or password incorrect' , 'error')
            return render_template('login.html')        
    else:
        if name:
            session.pop('usr')
            return render_template('login.html', name=name)
        else:
            if 'usr' in session:
                return  redirect(url_for('home'))
            else:
                return render_template('login.html', name=name)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form['searchDate']
        resp = task.getStreestLevelCrimes(date)
        dates = task.selectDates()
        return render_template('home.html', obj={'outcomes':resp,'dates':dates})
    else:
        if 'usr' in session:
            resp = task.getStreestLevelCrimes()
            dates = task.selectDates()
            return render_template('home.html', obj={'outcomes':resp,'dates':dates})
        else:
            return  redirect(url_for('login'))

@app.route('/put', methods=['PUT'])
def put():
    crime = request.form
    update = task.updateCrime(crime)
    return update
@app.route('/delete', methods=['DELETE'])
def delete():
    crime = request.form['id']
    update = task.deleteOutcome(crime)
    return '{}'.format(update)

@app.route('/edit/<id>', methods=['GET','POST'])
def editCrime(id):
    if request.method == 'POST':
        if request.form['_method']=='put':
            crime = {}
            crime['id'] = id
            crime['category'] = request.form['category']
            crime['location_type'] = request.form['location_type']
            crime['latitude'] = request.form['latitude']
            crime['longitude'] = request.form['longitude']
            crime['street_name'] = request.form['street_name']
            crime['month'] = request.form['month']
            response = requests.put('http://localhost:5000/put', data=crime)
            if response.content:
                crimeDetails = task.getStreestLevelCrimesId(id)
                persistent_id = crimeDetails[0].persistent_id
                crimeOutcomes = task.getCrimesOutcome(persistent_id)  
        else:
            if 'usr' in session:
                outcomeId = request.form['value']
                response = requests.delete('http://localhost:5000/delete', data={'id':outcomeId})
                crimeDetails = task.getStreestLevelCrimesId(int(response.content))
                persistent_id = crimeDetails[0].persistent_id
                count = task.countCrimesOutcome(persistent_id)
                if count > 0:
                    crimeOutcomes = task.getCrimesOutcome(persistent_id)
                else:
                    task.loadCrimesOutcome(persistent_id)
                    crimeOutcomes = task.getCrimesOutcome(persistent_id)                

            else:
                return  redirect(url_for('login'))
    else:
        if 'usr' in session:
            crimeDetails = task.getStreestLevelCrimesId(id)
            persistent_id = crimeDetails[0].persistent_id
            count = task.countCrimesOutcome(persistent_id)
            if count > 0:
                crimeOutcomes = task.getCrimesOutcome(persistent_id)
            else:
                task.loadCrimesOutcome(persistent_id)
                crimeOutcomes = task.getCrimesOutcome(persistent_id)
        else:
            return  redirect(url_for('login'))
    
    return render_template('editCrime.html', crime={'details':crimeDetails,'outcomes':crimeOutcomes}) 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)