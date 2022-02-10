from flask import Flask
from flask_sqlalchemy import SQLAlchemy #IGNORE

app = Flask(__name__)
db = SQLAlchemy(app)

from rest_api.fish_shop.controller import *
from rest_api.models import Fish

db.create_all()

if __name__ == "__main__":
    app.run()

