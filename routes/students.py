from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from util.extensions import db

students_bp = Blueprint('students', __name__, url_prefix="/students")

# Department short code map
DEPT_CODES = {
    "Computer Science": "CS",
    "Botany": "BOT",
    "English": "ENG",
    "MBA": "MBA",
    "Others": "OTH"
}

from sqlalchemy import func

def generate_rollno(department, year):
    dept_code = DEPT_CODES.get(department, "GEN")

    last_roll = db.session.query(Student.rollno).filter_by(     #SQL alchemy
        department=department,
        admission_year=year
    ).order_by(Student.rollno.desc()).first()

    if last_roll:
        # Extract last number (e.g., CS-2028-0002 → 2)
        last_number = int(last_roll[0].split("-")[-1])
        new_number = last_number + 1
    else:
        new_number = 1

    return f"{dept_code}-{year}-{new_number:04d}"           # custom roll no


# ------------------------------------------------------
# 1. LIST ALL STUDENTS  
# ------------------------------------------------------
@students_bp.route('/')
def student_departments():
    departments = ["Computer Science", "Botany", "English", "MBA"]
    return render_template("views/students/students_departments.html",
                           departments=departments)


@students_bp.route('/<dept>')
def department_batches(dept):
    students = Student.query.filter_by(department=dept).all()

    # Extract years from admission_year
    years = sorted({s.admission_year for s in students})

    return render_template("views/students/students_years.html",
                           dept=dept,
                           years=years)


@students_bp.route('/<dept>/<year>')
def students_in_batch(dept, year):
    students = Student.query.filter_by(department=dept, admission_year=year).all()

    return render_template("views/students/students_list_batch.html",
                           dept=dept,
                           year=year,
                           students=students)


# ------------------------------------------------------
# 2. REGISTER STUDENT
# ------------------------------------------------------
@students_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        department = request.form.get('department')
        year = request.form.get('admission_year')

        rollno = generate_rollno(department, year)

        new_student = Student(
            fullname=request.form.get('fullname'),
            rollno=rollno,
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

        flash(f"Student registered!" , "success")
        flash(f"Roll No: {rollno}", "info")

        return redirect(url_for('students.student_departments'))


    return render_template('views/students/register.html')


# ------------------------------------------------------
# 3. STUDENT PROFILE
# ------------------------------------------------------
@students_bp.route('/profile/<int:id>')
def student_profile(id):
    student = Student.query.get_or_404(id)
    return render_template('views/students/profile.html', student=student)


# ------------------------------------------------------
# 4. EDIT STUDENT
# ------------------------------------------------------
@students_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == "POST":
        student.fullname = request.form['fullname']
        student.dob = request.form['dob']
        student.address = request.form['address']
        student.category = request.form['category']
        student.department = request.form['department']
        student.course = request.form['course']
        student.admission_year = request.form['admission_year']
        student.gender = request.form['gender']

        db.session.commit()
        flash("Student updated!", "success")
        return redirect(url_for('students.student_departments'))

    return render_template('views/students/edit.html', student=student)


# ------------------------------------------------------
# 5. DELETE STUDENT
# ------------------------------------------------------
@students_bp.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    
    db.session.delete(student)
    db.session.commit()
    
    flash("Student deleted!", "info")
    return redirect(url_for('students.student_departments'))


