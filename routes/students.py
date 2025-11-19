from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from util.extensions import db
from datetime import datetime

students_bp = Blueprint('students_bp', __name__, url_prefix='/students')

@students_bp.route('/')
def view_students():
    all_students = Student.query.all()
    return render_template(
        'views/students.html',
        all_students=all_students
    )

@students_bp.route('/register', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            parentage = request.form.get('parentage')
            dob = request.form.get('dob')
            category = request.form.get('category')
            gender = request.form.get('gender')
            email = request.form.get('email')
            contact = request.form.get('contact')
            department = request.form.get('department', 'B.Tech')
            admission_year = request.form.get('admission_year', '2024')
            
            # Check if email already exists
            existing_student = Student.query.filter_by(email=email).first()
            if existing_student:
                flash('Email already registered!', 'danger')
                return redirect(url_for('students_bp.register_student'))
            
            # Create new student
            new_student = Student(
                name=name,
                parentage=parentage,
                dob=datetime.strptime(dob, '%Y-%m-%d').date() if dob else None,
                category=category,
                gender=gender,
                email=email,
                contact=contact,
                department=department,
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


# ------------------------------------------------------
# 3. STUDENT PROFILE
# ------------------------------------------------------
@students_bp.route('/profile/<int:id>')
def student_profile(id):
    student = Student.query.get_or_404(id)
    return render_template('views/students/profile.html', student=student)

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
            student.email = request.form.get('email')
            student.contact = request.form.get('contact')
            student.department = request.form.get('department')
            student.admission_year = request.form.get('admission_year')
            
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('students_bp.student_profile', student_id=student_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating student: {str(e)}', 'danger')
    
    return render_template('views/edit_student.html', student=student)


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

