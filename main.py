from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:password@localhost:3306/stud'

db = SQLAlchemy(app)
ms = Marshmallow(app)

from rest_api.fish_shop.controller import *


db.create_all()

if __name__ == "__main__":
    app.run()
