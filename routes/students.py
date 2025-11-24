from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from util.extensions import db
from datetime import datetime
from sqlalchemy import asc, desc

students_bp = Blueprint('students_bp', __name__, url_prefix='/students')


# ------------------------------------------------------
# LIST STUDENTS (with search, filter, sort)
# ------------------------------------------------------
@students_bp.route('/')
def view_students():
    department = request.args.get('department', type=str)
    q = request.args.get('q', type=str)
    sort_by = request.args.get('sort_by', 'name')
    order = request.args.get('order', 'asc')

    query = Student.query
    if department:
        query = query.filter_by(department=department)
    if q:
        term = f"%{q}%"
        query = query.filter((Student.name.ilike(term)) | (Student.course.ilike(term)))

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

    departments = [
        'Department of Engineering',
        'Botany',
        'English',
        'Department of Management Studies'
    ]

    total = Student.query.count()
    male = Student.query.filter_by(gender='M').count()
    female = Student.query.filter_by(gender='F').count()
    other = total - (male + female)

    return render_template('views/students.html',
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
                               'male_pct': round((male/total*100) if total else 0, 1),
                               'female_pct': round((female/total*100) if total else 0, 1),
                               'other_pct': round((other/total*100) if total else 0, 1)
                           }
                           )


# ------------------------------------------------------
# REGISTER STUDENT
# ------------------------------------------------------
@students_bp.route('/register', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            parentage = request.form.get('parentage')
            dob = request.form.get('dob')
            category = request.form.get('category')
            gender = request.form.get('gender')
            department = request.form.get('department', 'Department of Engineering')
            course = request.form.get('course')
            admission_year = request.form.get('admission_year', '2024')

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


# ------------------------------------------------------
# STUDENT PROFILE
# ------------------------------------------------------
@students_bp.route('/profile/<int:student_id>')
def student_profile(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('views/student_profile.html', student=student)


# ------------------------------------------------------
# EDIT STUDENT
# ------------------------------------------------------
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


# ------------------------------------------------------
# DELETE STUDENT
# ------------------------------------------------------
@students_bp.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting student: {str(e)}', 'danger')
    return redirect(url_for('students_bp.view_students'))


