from app import app
from flask import request, render_template
from app import models, db

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
    for coord in coordinates:
    	coordinate = models.Coordinate(coord["latitude"], coord["longitude"], coord["notes"])
        print coordinate
        db.session.add(coordinate)
    db.session.commit()
    return 'Yay!', 200

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', coordinate_list = models.Coordinate.query.all())

# Curl command to test /coordinates
# curl -H "Content-Type: application/json" -X POST -d '{"coordinates": [{ "latitude": 101.1, "longitude": 42.0, "notes": "yolo"},{ "latitude": 99.99, "longitude": 12.34, "notes": "$"}]}' http://localhost:5000/coordinates