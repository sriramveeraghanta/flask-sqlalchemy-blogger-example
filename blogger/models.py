from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from blogger import app

db = SQLAlchemy(app)

class User(db.Model):
	uid = db.Column(db.Integer,primary_key = True, autoincrement = True)
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	username = db.Column(db.String(50), unique=True, index=True)
	password = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True, index=True)
	dateofreg = db.Column(db.DateTime, default = datetime.datetime.now)

	def __init__(self, firstname, lastname, username, password, email):
		self.firstname = firstname
		self.lastname = lastname
		self.username = username
		self.password = password
		self.email = email

class Posts(db.Model):
	pid= db.Column(db.Integer, primary_key = True, autoincrement = True )
	title = db.Column(db.String(100))
	description = db.Column(db.String(1000))
	puid = db.Column(db.Integer, db.ForeignKey('user.uid'))

	def __init__(self, title, description, puid):
		self.title = title
		self.description = description
		self.puid = puid

db.create_all()
