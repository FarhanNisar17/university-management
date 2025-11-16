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

def generate_rollno(department, year):
    dept_code = DEPT_CODES.get(department, "GEN")

    # Count students in same department + year
    count = Student.query.filter_by(
        department=department,
        admission_year=year
    ).count() + 1

    return f"{dept_code}-{year}-{count:04d}"


# ------------------------------------------------------
# 1. LIST ALL STUDENTS  (THIS ROUTE WAS MISSING)
# ------------------------------------------------------
@students_bp.route('/')
def list_students():
    search = request.args.get("search", "")
    department = request.args.get("dept", "")

    query = Student.query

    if search:
        query = query.filter(Student.fullname.ilike(f"%{search}%"))

    if department:
        query = query.filter_by(department=department)

    students = query.all()

    return render_template(
        'views/students/list.html',
        students=students,
        search=search,
        department_filter=department
    )


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

        flash(f"Student registered! Roll No: {rollno}", "success")
        return redirect(url_for('students.list_students'))
        

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
        return redirect(url_for('students.list_students'))

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
    return redirect(url_for('students.list_students'))
