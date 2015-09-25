from app import app
from flask import request
import json

@app.route('/health', methods=['GET'])
def health():
    return 'App is healthy!', 200


@app.route('/coordinates', methods=['POST'])
def handle_coordinates():
    coordinates = request.json["coordinates"]
    for coordinate in coordinates:
        latitude = coordinate["latitude"]
        longitude = coordinate["longitude"]
        notes = coordinate["notes"]
        print latitude, longitude, notes
    return 'Yay!', 200

# Curl command to test /coordinates
# curl -H "Content-Type: application/json" -X POST -d '{"coordinates": [{ "latitude": 101.1, "longitude": 42.0, "notes": "yolo"},{ "latitude": 99.99, "longitude": 12.34, "notes": "$"}]}' http://localhost:5000/coordinates