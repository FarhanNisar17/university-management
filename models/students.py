from util.extensions import db

class Student(db.Model):
    __tablename__ = 'student'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    parentage = db.Column(db.String(150))
    dob = db.Column(db.Date)
    category = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    department = db.Column(db.String(50), default='Department of Engineering')
    admission_year = db.Column(db.String(20), default='2024')
    email = db.Column(db.String(100), unique=True)
    contact = db.Column(db.String(20))
    course = db.Column(db.String(100))
