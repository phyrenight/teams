from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from teamsdb import User, Teams, Players, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask from session as session as login_session


app = Flask(__name__)

@app.route('welcome')
def welcome():
    return "welcome"


@app.route('/login')
def login()
    return "login screen"


@app.route('/teams')
def displayTeams():
    return "and here are the teams."

@app.route(/teams/)