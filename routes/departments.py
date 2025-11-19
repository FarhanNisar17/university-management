from flask import Blueprint, render_template, abort, request, url_for
from models.students import Student
from sqlalchemy import asc, desc

department_bp = Blueprint("department", __name__, url_prefix="/departments")

# Map URL slug -> dict with DB value and display label.
# We want the existing engineering card (slug `computer-science`) to show
# students whose `department` in DB is 'B.Tech' but the page should display
# 'Department of Engineering'. This keeps student rows under the Engineering
# department while storing 'B.Tech' in the DB.
DEPARTMENT_MAP = {
    # support both legacy 'B.Tech' and new 'Department of Engineering' values in DB
    "computer-science": {"db": ["B.Tech", "Department of Engineering"], "label": "Department of Engineering"},
    "botany": {"db": ["Botany"], "label": "Botany"},
    "english": {"db": ["English"], "label": "English"},
    "mba": {"db": ["MBA", "Department of Management Studies"], "label": "Department of Management Studies"}
}

@department_bp.route("/")
def list_departments():
    return render_template("views/departments/list.html")

@department_bp.route("/<slug>")
def department_detail(slug):

    if slug not in DEPARTMENT_MAP:
        abort(404)

    dept_info = DEPARTMENT_MAP[slug]
    dept_db = dept_info.get('db')
    dept_label = dept_info.get('label')
    # Sorting and filtering
    sort_by = request.args.get('sort_by', 'name')  # options: name, admission_year, gender, category
    order = request.args.get('order', 'asc')

    # Query using the DB stored department value(s)
    if isinstance(dept_db, (list, tuple)):
        query = Student.query.filter(Student.department.in_(dept_db))
    else:
        query = Student.query.filter_by(department=dept_db)

    # Apply ordering
    if sort_by == 'admission_year':
        ordering = Student.admission_year
    elif sort_by == 'gender':
        ordering = Student.gender
    elif sort_by == 'category':
        ordering = Student.category
    else:
        ordering = Student.name

    if order == 'desc':
        query = query.order_by(desc(ordering))
    else:
        query = query.order_by(asc(ordering))

    students = query.all()

    # Group by admission year for accordion display
    batches = {}
    for s in students:
        year = s.admission_year or 'Unknown'
        batches.setdefault(year, []).append(s)
    return render_template(
        "views/departments/detail.html",
        dept_name=dept_label,
        batches=batches,
        slug=slug,
        sort_by=sort_by,
        order=order
    )
