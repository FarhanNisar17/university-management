from util.extensions import db

class ScholarshipApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scholarship_name = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    parentage = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    reason = db.Column(db.Text, nullable=False)
