from flask import Blueprint, render_template, request, redirect, url_for, flash
from util.extensions import db
from models.hostel import HostelApplication

hostel_bp = Blueprint("hostels", __name__, url_prefix="/hostels")


# -----------------------------------------------------------
# 1. HOSTEL INFORMATION PAGE (Static)
# -----------------------------------------------------------
@hostel_bp.route("/")
def hostel_info():
    return render_template("views/hostels/info.html")


# -----------------------------------------------------------
# 2. APPLY FOR HOSTEL
# -----------------------------------------------------------
@hostel_bp.route("/apply", methods=["GET", "POST"])
def apply_hostel():
    if request.method == "POST":
        app = HostelApplication(
            fullname=request.form.get("fullname"),
            rollno=request.form.get("rollno"),
            gender=request.form.get("gender"),
            phone=request.form.get("phone"),
            address=request.form.get("address"),
            reason=request.form.get("reason")
        )

        db.session.add(app)
        db.session.commit()

        flash("Hostel application submitted successfully!", "success")
        return redirect(url_for("hostels.hostel_info"))

    return render_template("views/hostels/apply.html")


# -----------------------------------------------------------
# 3. VIEW ALL APPLICATIONS (ADMIN)
# -----------------------------------------------------------
@hostel_bp.route("/applications")
def view_applications():
    apps = HostelApplication.query.all()
    return render_template("views/hostels/applications.html", apps=apps)


# -----------------------------------------------------------
# 4. DELETE APPLICATION
# -----------------------------------------------------------
@hostel_bp.route("/delete/<int:id>")
def delete_application(id):
    app = HostelApplication.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()

    flash("Application deleted!", "info")
    return redirect(url_for("hostels.view_applications"))


# APPROVE APPLICATION
@hostel_bp.route("/approve/<int:id>")
def approve_application(id):
    app = HostelApplication.query.get_or_404(id)
    app.status = "Approved"
    db.session.commit()
    flash("Application Approved!", "success")
    return redirect(url_for("hostels.view_applications"))

# REJECT APPLICATION
@hostel_bp.route("/reject/<int:id>")
def reject_application(id):
    app = HostelApplication.query.get_or_404(id)
    app.status = "Rejected"
    db.session.commit()
    flash("Application Rejected!", "info")
    return redirect(url_for("hostels.view_applications"))
