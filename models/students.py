from util.extensions import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
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
=======
    rollno = db.Column(db.String(20), unique=True)
    fullname = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.String(20))
    address = db.Column(db.String(200))
    category = db.Column(db.String(20))
    department = db.Column(db.String(100))
    course = db.Column(db.String(100))
    admission_year = db.Column(db.String(20))
    gender = db.Column(db.String(20))
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11
