from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from teamsdb import User, Teams, Players, Base
from sqlalchemy import create_engine, asc
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
def displayTeamInfo(team):
    teamDetails = session.query(Teams).filter_by(name=team).one()
    return render_template("teamInfo.html", teamDetails = teamDetails)


@app.route('/teams/division/<division>/')
def teamDivision(division):
	teams = session.query(Teams).filter_by(division=division).all()
	return render_template("divisionList.html", teams=teams)

@app.route('/teams/<team>/players/')
def teamPlayers():
    return "and here are your players"


@app.route('/teams/<team>/players/<name>')
def playerInfo():
    return "enough info for you"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
