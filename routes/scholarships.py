from flask import Blueprint, render_template

scholarship_bp = Blueprint("scholarship", __name__, url_prefix="/scholarships")


@scholarship_bp.route("/")
def list_scholarships():
    return render_template("views/scholarships.html")
