from flask import Blueprint, render_template

hostel_bp = Blueprint("hostels", __name__, url_prefix="/hostels")

@hostel_bp.route("/")
def show_hostel_info():
    return render_template("views/hostels.html")
