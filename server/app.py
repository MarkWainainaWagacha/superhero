from flask import Flask
from .config import db
from .routes import register_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
register_routes(app)




