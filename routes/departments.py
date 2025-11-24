from flask import Blueprint, render_template, abort
from models.students import Student

department_bp = Blueprint("department", __name__, url_prefix="/departments")

# Map URL slug → exact department string stored in DB
DEPARTMENT_MAP = {
<<<<<<< HEAD
    # support both legacy 'B.Tech' and new 'Department of Engineering' values in DB
    "computer-science": {"db": ["B.Tech", "Department of Engineering"], "label": "Department of Engineering"},
    "botany": {"db": ["Botany"], "label": "Botany"},
    "english": {"db": ["English"], "label": "English"},
    "mba": {"db": ["MBA", "Department of Management Studies"], "label": "Department of Management Studies"}
=======
    "computer-science": "Computer Science",
    "botany": "Botany",
    "english": "English",
    "mba": "MBA"
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11
}

@department_bp.route("/")
def list_departments():
    return render_template("views/departments/list.html")

@department_bp.route("/<slug>")
def department_detail(slug):

    if slug not in DEPARTMENT_MAP:
        abort(404)

    dept_name = DEPARTMENT_MAP[slug]

<<<<<<< HEAD
    # Query using the DB stored department value(s)
    if isinstance(dept_db, (list, tuple)):
        query = Student.query.filter(Student.department.in_(dept_db))
    else:
        query = Student.query.filter_by(department=dept_db)
=======
    students = Student.query.filter_by(department=dept_name).all()
>>>>>>> f88f5548372592c6bbdb81cedb662d6390289d11

    batches = {}
    for s in students:
        batches.setdefault(s.admission_year, []).append(s)

    return render_template(
        "views/departments/detail.html",
        dept_name=dept_name,
        batches=batches
    )
