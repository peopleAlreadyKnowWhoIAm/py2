from main import db, ms

class Fish(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10))
    origin = db.Column(db.String(30))
    
class FishSchema(ms.Schema):
    class Meta:
        fields = ('id','name', 'origin')