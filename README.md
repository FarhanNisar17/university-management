📘 University Management System (Flask)

A simple Flask web application for managing university data such as students, departments, hostels, scholarships, and more.
All data is stored in a MySQL database using SQLAlchemy.

🚀 Features
✔ Student Management

Register new students

View all students

Auto-generate roll numbers

Store details like name, DOB, department, course, gender, etc.

✔ Department Management

View departments

Show students batch-wise

Accordion-style display for admission years

✔ Hostel Applications

Students apply using last 2 digits of roll number

System automatically finds full roll number

View all hostel applications

✔ Scholarships & Transport

Students can apply for scholarships

Transport service page included

🛠 Technologies Used

Flask (Python)

MySQL + SQLAlchemy

Jinja2 Templates

HTML, CSS, JavaScript

Blueprint Structure

▶️ How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Set up database

Create a MySQL database named:

university_db

3. Create tables
   from app import create_app
   from util.extensions import db

app = create_app()
with app.app_context():
db.create_all()

4. Start the server
   python app.py

5. Visit in browser:
   http://localhost:5000/

📄 Project Structure
project/
│── app.py
│── routes/
│── models/
│── templates/
│── static/
│── config/
└── README.md

🤝 Contributing
