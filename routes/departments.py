from flask import Blueprint, render_template

department_bp = Blueprint("department", __name__, url_prefix="/departments")

@department_bp.route("/")
def list_departments():
    return render_template("views/departments/list.html")

@department_bp.route("/<dept>")
def department_detail(dept):
    return f"Department details for: {dept}"
