from flask import jsonify, request
from main import app, db
from ..models import Fish

@app.route('/')
def index():
    return 'Hooray'

@app.route('/prize/<id>')
def get_fish(id):
    return "<h1>HANDS UP</h1><br>Give me your money!!!!<br>Yoy're now %s"%id


@app.route("/fish")
def find_fish():
    
    return "The fish had gotten lost<br><h2>CRYING!!!</h2>"

@app.route("/fish", methods=["POST"])
def create_fish():
    reqs = request.get_json()
    fish = Fish(name = reqs['name'], origin = reqs['origin'])
    db.session.add(fish)
    print(reqs)
    db.session.commit()

    print(Fish.query.all())
    return "fish created"