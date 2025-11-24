from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from util.extensions import db
<<<<<<< HEAD
from datetime import datetime
from sqlalchemy import asc, desc
=======
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11

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

    last_roll = db.session.query(Student.rollno).filter_by(
        department=department,
        admission_year=year
    ).order_by(Student.rollno.desc()).first()

    if last_roll:
        # Extract last number (e.g., CS-2028-0002 → 2)
        last_number = int(last_roll[0].split("-")[-1])
        new_number = last_number + 1
    else:
        new_number = 1

    return f"{dept_code}-{year}-{new_number:04d}"


# ------------------------------------------------------
# 1. LIST ALL STUDENTS  (THIS ROUTE WAS MISSING)
# ------------------------------------------------------
@students_bp.route('/')
<<<<<<< HEAD
def view_students():
    # filters
    department = request.args.get('department', type=str)
    q = request.args.get('q', type=str)

    # sorting
    sort_by = request.args.get('sort_by', 'name')  # options: name, department, year, gender, category, recent
    order = request.args.get('order', 'asc')

    query = Student.query
    if department:
        query = query.filter_by(department=department)
    if q:
        # simple search on name or course
        term = f"%{q}%"
        query = query.filter((Student.name.ilike(term)) | (Student.course.ilike(term)))

    # determine ordering column
    if sort_by == 'department':
        ordering = Student.department
    elif sort_by == 'year':
        ordering = Student.admission_year
    elif sort_by == 'gender':
        ordering = Student.gender
    elif sort_by == 'category':
        ordering = Student.category
    elif sort_by == 'recent':
        ordering = Student.id
    else:
        ordering = Student.name

    if order == 'desc':
        query = query.order_by(desc(ordering))
    else:
        query = query.order_by(asc(ordering))

    all_students = query.all()

    # departments for filter dropdown
    departments = [
        'Department of Engineering',
        'Botany',
        'English',
        'Department of Management Studies'
    ]

    # Stats (overall)
    total = Student.query.count()
    male = Student.query.filter_by(gender='M').count()
    female = Student.query.filter_by(gender='F').count()
    other = total - (male + female)
    male_pct = (male / total * 100) if total else 0
    female_pct = (female / total * 100) if total else 0
    other_pct = (other / total * 100) if total else 0

    return render_template(
        'views/students.html',
        all_students=all_students,
        selected_department=department,
        departments=departments,
        sort_by=sort_by,
        order=order,
        q=q,
        stats={
            'total': total,
            'male': male,
            'female': female,
            'other': other,
            'male_pct': round(male_pct, 1),
            'female_pct': round(female_pct, 1),
            'other_pct': round(other_pct, 1)
        }
    )
=======
def student_departments():
    departments = ["Computer Science", "Botany", "English", "MBA"]
    return render_template("views/students/students_departments.html",
                           departments=departments)
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11


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
<<<<<<< HEAD
def register_student():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            parentage = request.form.get('parentage')
            dob = request.form.get('dob')
            category = request.form.get('category')
            gender = request.form.get('gender')
            department = request.form.get('department', 'Department of Engineering')
            course = request.form.get('course')
            admission_year = request.form.get('admission_year', '2024')

            # Create new student (we no longer require email/contact during registration)
            new_student = Student(
                name=name,
                parentage=parentage,
                dob=datetime.strptime(dob, '%Y-%m-%d').date() if dob else None,
                category=category,
                gender=gender,
                department=department,
                course=course,
                admission_year=admission_year
            )
            
            db.session.add(new_student)
            db.session.commit()
            
            flash('Student registered successfully!', 'success')
            return redirect(url_for('students_bp.view_students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error registering student: {str(e)}', 'danger')
            return redirect(url_for('students_bp.register_student'))
    
    return render_template('views/register_student.html')
=======
def register():
    if request.method == "POST":
        department = request.form.get('department')
        year = request.form.get('admission_year')
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11

        rollno = generate_rollno(department, year)

<<<<<<< HEAD
@students_bp.route('/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    
    if request.method == 'POST':
        try:
            student.name = request.form.get('name')
            student.parentage = request.form.get('parentage')
            dob = request.form.get('dob')
            student.dob = datetime.strptime(dob, '%Y-%m-%d').date() if dob else None
            student.category = request.form.get('category')
            student.gender = request.form.get('gender')
            student.department = request.form.get('department')
            student.course = request.form.get('course')
            student.admission_year = request.form.get('admission_year')
            
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('students_bp.student_profile', student_id=student_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating student: {str(e)}', 'danger')
    
    return render_template('views/edit_student.html', student=student)
=======
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
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11

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


