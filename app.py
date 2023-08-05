# app.py
from flask import Flask
from model import db, mongo, User, MongoDBUser
from config import SQLALCHEMY_DATABASE_URI, MONGODB_SETTINGS

app = Flask(__name__)

# configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configuração do MongoEngine
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS

db.init_app(app)
mongo.init_app(app)

@app.route("/")
def home():
    # Código para interagir com o banco de dados
    pass
