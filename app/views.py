from app import app
from flask import request
from app import models
import json

@app.route('/test', methods = ['GET'])
def test_view():
	coordinate_list = models.Coordinate.query.all()
	print(coordinate_list)
	return 'test_view', 200

@app.route('/health', methods=['GET'])
def health():
    return 'App is healthy!', 200

@app.route('/coordinates', methods=['POST'])
def handle_coordinates():
    coordinates = request.json["coordinates"]
    for coord in coordinate_list:
    	coordinate = Coordinate(coord["latitude"], coord["longitude"], coord["notes"])
        print coordinate
        db.session.add(coordinate)
    db.session.commit()
    return 'Yay!', 200

# Curl command to test /coordinates
# curl -H "Content-Type: application/json" -X POST -d "{"coordinates": [{ "latitude": 101.1, "longtitude": 42.0, "notes": "yolo"},{ "latitude": 99.99, "longtitude": 12.34, "notes": "$"}]}" http://localhost:5000/coordinates