from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from teamsdb import User, Teams, Players, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import session as login_session


app = Flask(__name__)

engine = create_engine('sqlite:///teamSport.db')
Base.metadata.bind = engine
Db = sessionmaker(bind=engine)
session = Db()

@app.route('/welcome')
def welcome():
    return "welcome"


@app.route('/login')
def login():
    return "login screen"


@app.route('/teams')
def displayTeams():
    teams = session.query(Teams).all()
    return render_template('displayTeams.html', teams=teams)


@app.route('/teams/<team>')
def displayTeamInfo():
    return "or maybe not"


@app.route('/teams/<team>/players/')
def teamPlayers():
    return "and here are your players"


@app.route('/teams/<team>/players/<name>')
def playerInfo():
    return "enough info for you"


if __name__ == "__main__":
    app.secret_key = "not yet"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
