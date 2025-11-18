from util.database import create_app, setup_database
from routes.students import students_bp
from flask import render_template

app = create_app()
setup_database(app)

# Import models AFTER db.init_app
from models.students import Student



# Import blueprints
from routes.students import students_bp
from routes.departments import department_bp
from routes.scholarships import scholarship_bp


# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    return render_template('views/home.html')

# Register blueprints
app.register_blueprint(students_bp)
app.register_blueprint(department_bp)
app.register_blueprint(scholarship_bp)


# ------------------ RUN APP ------------------
if __name__ == '__main__':
    app.run(debug=True)
