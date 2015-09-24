from app import db

class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(100), unique=False)
    longitude = db.Column(db.String(100), unique=False)
    notes = db.Column(db.Text, unique=False)

    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
        self.notes = notes

    def __repr__(self):
        return '<%r %r>' % self.latitude, self.longitude