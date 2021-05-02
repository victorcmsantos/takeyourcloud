from flask import Flask
from config import Config, basedir
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.api.v1 import routes
from app.dbmods import model


