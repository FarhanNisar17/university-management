from flask import Blueprint, render_template, abort
from models.students import Student

department_bp = Blueprint("department", __name__, url_prefix="/departments")

# Map URL slug → exact department string stored in DB
DEPARTMENT_MAP = {
    "computer-science": "Computer Science",
    "botany": "Botany",
    "english": "English",
    "mba": "MBA"
}

@department_bp.route("/")
def list_departments():
    return render_template("views/departments/list.html")

@department_bp.route("/<slug>")
def department_detail(slug):

    if slug not in DEPARTMENT_MAP:
        abort(404)

    dept_name = DEPARTMENT_MAP[slug]

    students = Student.query.filter_by(department=dept_name).all()

    batches = {}
    for s in students:
        batches.setdefault(s.admission_year, []).append(s)

    return render_template(
        "views/departments/detail.html",
        dept_name=dept_name,
        batches=batches
    )
