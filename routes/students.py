from flask import Blueprint, render_template, request, redirect, url_for,flash
from models.students import Student
from extensions import db

students_bp = Blueprint('students', __name__, url_prefix="/students")

@students_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        new_student = Student(
            fullname=request.form.get('fullname'),
            rollno=request.form.get('rollno'),
            dob=request.form.get('dob'),
            address=request.form.get('address'),
            category=request.form.get('category'),
            department=request.form.get('department'),
            course=request.form.get('course'),
            admission_year=request.form.get('admission_year'),
            gender=request.form.get('gender')
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student registered successfully!", "success")
        return redirect(url_for('home'))

    return render_template('views/register.html')
