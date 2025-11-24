from util.extensions import db

class HostelApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    rollno = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default="Pending")  # Pending / Approved / Rejected
