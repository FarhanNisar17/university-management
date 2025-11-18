from flask import Blueprint, render_template, request, redirect, url_for
from models.thirdsem import ThirdSemStudent
from util.extensions import db
import os

thirdsem_bp = Blueprint('thirdsem_bp', __name__, url_prefix='/third_sem')

UPLOAD_FOLDER = "static/uploads/third_sem"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Show all third sem students
@thirdsem_bp.route('/')
def list_thirdsem():
    students = ThirdSemStudent.query.all()
    return render_template('views/third_sem.html', students=students)


# Add third sem student (simple form)
@thirdsem_bp.route('/add', methods=['GET', 'POST'])
def add_thirdsem():
    if request.method == 'POST':
        name = request.form.get('name')
        roll = request.form.get('roll')
        department = request.form.get('department')
        address = request.form.get('address')
        pickup = request.form.get('pickup')

        student = ThirdSemStudent(name=name, roll=roll, department=department, address=address, pickup_location=pickup)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('thirdsem_bp.list_thirdsem'))

    return render_template('forms/add_thirdsem.html')
