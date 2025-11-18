import os
from flask import Flask
from util.extensions import db
from util.config import Config

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("templates"),
        static_folder=os.path.abspath("static")
    )

    app.config.from_object(Config)
    db.init_app(app)

    return app



def setup_database(app):
    # Import models AFTER init_app
    from models.students import Student
    # Ensure third sem model is imported so its table is created
    from models.thirdsem import ThirdSemStudent

    with app.app_context():
        db.create_all()
