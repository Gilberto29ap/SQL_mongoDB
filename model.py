# model.py
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

db = SQLAlchemy()
mongo = MongoEngine()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

class MongoDBUser(mongo.Document):
    name = mongo.StringField(required=True)
    email = mongo.EmailField(required=True)
