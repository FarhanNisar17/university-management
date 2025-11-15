from extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    rollno = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(20))
    address = db.Column(db.String(200))
    category = db.Column(db.String(20))
    department = db.Column(db.String(100))
    course = db.Column(db.String(100))
    admission_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
