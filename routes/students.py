from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from extensions import db

students_bp = Blueprint('students', __name__, url_prefix="/students")

# Department → short code
DEPT_CODES = {
    "Computer Science": "CS",
    "Botany": "BOT",
    "English": "ENG",
    "MBA": "MBA",
    "Others": "OTH"
}

def generate_rollno(department, year):
    dept_code = DEPT_CODES.get(department, "GEN")
    
    # Count students in same dept & year
    count = Student.query.filter_by(department=department, admission_year=year).count() + 1
    
    # Format → CS-2025-0001
    return f"{dept_code}-{year}-{count:04d}"

@students_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":

        department = request.form.get('department')
        year = request.form.get('admission_year')

        # AUTO-GENERATE ROLL NUMBER
        rollno = generate_rollno(department, year)

        new_student = Student(
            fullname=request.form.get('fullname'),
            rollno=rollno,  # auto assigned
            dob=request.form.get('dob'),
            address=request.form.get('address'),
            category=request.form.get('category'),
            department=department,
            course=request.form.get('course'),
            admission_year=year,
            gender=request.form.get('gender')
        )

        db.session.add(new_student)
        db.session.commit()

        flash(f"Student registered successfully! Roll No: {rollno}", "success")
        return redirect(url_for('home'))

    return render_template('views/register.html')
