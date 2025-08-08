from app import db

class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.String(200))