from urllib import response
from xml.dom import ValidationErr
from flask import jsonify, request
from main import app, db
from rest_api.models import *
from marshmallow.exceptions import ValidationError

fish_schema = FishSchema()
fishes_schema = FishSchema(many = True)

@app.route('/')
def index():
	return 'Hooray'

@app.route('/prize/<id>')
def get_fish(id):
    fish = Fish.query.get(id)
    
    if fish is None:
        return{ "errors": "No fish with gotten id"}, 404
    
    response = fish_schema.dump(Fish.query.get(id))
    return jsonify(response)


@app.route("/fish")
def find_fish():
	response = fishes_schema.dump(Fish.query.all())
	return jsonify(response) 

@app.route("/fish", methods=["POST"])
def create_fish():
    try:
        fish = Fish(**fish_schema.load(request.get_json()))
    except ValidationError as err:
        return {"errors": err.messages}, 422	
    
    db.session.add(fish)
    db.session.commit()
    response = fish_schema.dump(fish)
    return jsonify(response)
