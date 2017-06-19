from flask import Flask, flash, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "secretsecret543210"

session={}
session['random']=None

def randomNumber():
    session['random'] = random.randrange(0,101)

@app.route('/')
def index():
    if session['random']==None:
        randomNumber()
    else:
        pass
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def usersGuess():
    print session['random']
    guess=request.form['guess']
    if len(guess)<1:
        flash('Please Enter a Number')
    else:
        usersGuess = int(guess)
        if (usersGuess==session['random']):
            flash('1')
        elif (usersGuess<session['random']):
            flash('2')
        elif (usersGuess>session['random']):
            flash('3')
    return redirect('/')

@app.route('/new', methods=['GET', 'POST'])
def newGame():
    randomNumber()
    return redirect('/')



app.run(debug=True)
