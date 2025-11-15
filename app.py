from flask import Flask, render_template, request, redirect, url_for, flash
import os
import json

# Initialize Flask app & tells Flask where your HTML files live
app = Flask(__name__, template_folder='templates', static_folder='static')
# Required for flashing messages from server to templates (development key)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-secret')

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

#scholarships
@app.route('/scholarships', methods=['GET', 'POST'])
def scholarship():
    if request.method == 'POST':
        # get form data here
        name = request.form['fullname']
        # save into database
    return render_template('views/scholarships.html')


#courses
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
