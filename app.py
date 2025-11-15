from flask import Flask, render_template, request, redirect, url_for
from extensions import db
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:urdream@localhost/university_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = "kjh23kjh4k2j34h2kj34h2k34jh23kj4h23"



# Import models AFTER db.init_app
from models.students import Student

# Import blueprints
from routes.students import students_bp

with app.app_context():
    db.create_all()

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    return render_template('views/home.html')

# Register blueprints
app.register_blueprint(students_bp)


# ------------------ RUN APP ------------------
if __name__ == '__main__':
    app.run(debug=True)
