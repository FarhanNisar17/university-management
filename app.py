from util.database import create_app, setup_database
from routes.students import students_bp
from flask import render_template
from util.extensions import db

app = create_app()          #flask instance 
setup_database(app)

# Import models AFTER db.init_app
from models.students import Student



# Import blueprints
from routes.students import students_bp
from routes.departments import department_bp
from routes.transport import transport_bp
from routes.contact import contact_bp
from routes.scholarships import scholarship_bp
from routes.hostel import hostel_bp

# ------------------ HOME PAGE ------------------
 
@app.route('/')
def home():

    total_students = Student.query.count()

    # you can count unique departments directly from Student table:
    total_departments = db.session.query(Student.department).distinct().count()         # takes only department column

    # Static sample data (modify later if needed)
    from models.hostel import HostelApplication
    total_hostel_residents = HostelApplication.query.filter_by(status="Approved").count()
    total_buses = 6

    return render_template(
        'views/home.html',
        total_students=total_students,
        total_departments=total_departments,
        total_hostel_residents=total_hostel_residents,
        total_buses=total_buses
    )

# Register blueprints
app.register_blueprint(students_bp)
app.register_blueprint(department_bp)
app.register_blueprint(transport_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(scholarship_bp)
app.register_blueprint(hostel_bp)

# -------- RUN APP ------ -
if __name__ == '__main__':      #run if this file gets executed 
    app.run(debug=True)
