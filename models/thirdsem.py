from util.extensions import db
from datetime import datetime


class ThirdSemStudent(db.Model):
    __tablename__ = 'third_sem'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    roll = db.Column(db.String(50), unique=True, nullable=False)
    department = db.Column(db.String(150))
    address = db.Column(db.String(255))
    pickup_location = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ThirdSemStudent {self.roll} - {self.name}>'
