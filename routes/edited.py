from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.scholarship import ScholarshipApplication
from util.extensions import db

scholarship_bp = Blueprint("scholarships", __name__, url_prefix="/scholarships")

# Static list of scholarships
scholarships = [
    {
        "id": 0,
        "name": "Merit-Based Scholarship",
        "desc": "Awarded to students with excellent academic performance.",
        "eligibility": "Minimum 80% in last exam.",
        "deadline": "March 15, 2025"
    },
    {
        "id": 1,
        "name": "Need-Based Scholarship",
        "desc": "For students needing financial assistance.",
        "eligibility": "Annual income < ₹2,50,000",
        "deadline": "April 10, 2025"
    }
]


@scholarship_bp.route("/")
def list_scholarships():
    return render_template(
        "views/scholarships/list.html",
        scholarships=scholarships
    )


@scholarship_bp.route("/apply/<int:id>", methods=["GET", "POST"])
def apply(id):

    if id >= len(scholarships):
        flash("Invalid scholarship", "error")
        return redirect(url_for("scholarships.list_scholarships"))

    scholarship = scholarships[id]

    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        reason = request.form["reason"]

        # Duplicate checking
        existing_email = ScholarshipApplication.query.filter_by(email=email).first()
        existing_phone = ScholarshipApplication.query.filter_by(phone=phone).first()

        if existing_email:
            flash("This email has already been used to apply!", "error")
            return redirect(request.url)

        if existing_phone:
            flash("This phone number has already been used to apply!", "error")
            return redirect(request.url)

        # Save new application
        app = ScholarshipApplication(
            scholarship_name=scholarship["name"],
            fullname=fullname,
            email=email,
            phone=phone,
            reason=reason
        )

        try:
            db.session.add(app)
            db.session.commit()
            flash("Application submitted successfully!", "success")
        except Exception:
            db.session.rollback()
            flash("Something went wrong while submitting!", "error")

        return redirect(url_for("scholarships.list_scholarships"))

    return render_template(
        "views/scholarships/apply.html",
        scholarship=scholarship
    )


@scholarship_bp.route("/submissions")
def submissions():
    apps = ScholarshipApplication.query.all()
    return render_template(
        "views/scholarships/submissions.html",
        applications=apps
    )


@scholarship_bp.route("/delete/<int:id>")
def delete_submission(id):
    app = ScholarshipApplication.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()

    flash("Submission deleted successfully!", "success")
    return redirect(url_for("scholarships.submissions"))
