from main import db

class Fish(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10))
    origin = db.Column(db.String(20))
    age_in_eyers = db.Column(db.Integer)
    weight = db.Column(db.Float)
