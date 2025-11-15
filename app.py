from flask import Flask, render_template, request, redirect, url_for
from extensions import db
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:urdream@localhost/university_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Import models AFTER db.init_app
from models import Student

with app.app_context():
    db.create_all()

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    return render_template('views/home.html')

# ------------------ STUDENT REGISTER ------------------
@app.route('/register', methods=['GET', 'POST'])
def students():

    if request.method == "POST":
        fullname = request.form.get('fullname')
        rollno = request.form.get('rollno')
        dob = request.form.get('dob')
        address = request.form.get('address')
        category = request.form.get('category')
        department = request.form.get('department')
        course = request.form.get('course')
        admission_year = request.form.get('admission_year')
        gender = request.form.get('gender')

        new_student = Student(
            fullname=fullname,
            rollno=rollno,
            dob=dob,
            address=address,
            category=category,
            department=department,
            course=course,
            admission_year=admission_year,
            gender=gender
        )

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('views/register.html')
# ------------------ SCHOLARSHIPS ------------------
@app.route('/scholarships')
def scholarships():
    return render_template('views/scholarships.html')

# ------------------ COURSES ------------------
@app.route('/courses')
def courses():
    return render_template('views/courses.html')

# ------------------ CONTACTS ------------------
@app.route('/contacts')
def contacts():
    return render_template('views/contacts.html')

# ------------------ HOSTELS ------------------
@app.route('/hostels')
def hostels():
    return render_template('views/hostels.html')


# ------------------ TRANSPORT ------------------
@app.route('/transport/submit', methods=['POST'])
def submit_transport_application():
    name = request.form.get('name')
    address = request.form.get('address')
    pickup = request.form.get('pickup')
    bus_id = request.form.get('bus_id')

    return render_template(
        'views/transport-success.html',
        name=name, address=address, pickup=pickup, bus_id=bus_id
    )


# ------------------ RUN APP ------------------
if __name__ == '__main__':
    app.run(debug=True)
