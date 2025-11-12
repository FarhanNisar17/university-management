from flask import Flask, render_template

# Initialize Flask app & tells Flask where your HTML files live
app = Flask(__name__, template_folder='templates',static_folder='static')


# Define route for homepage
@app.route('/')
def home():
    return render_template('views/home.html')

# Students
@app.route('/register')
def register():
    return render_template('views/register.html')

#scholarships
@app.route('/scholarships')
def scholarships():
    # Sample scholarships data — replace or extend with real data or a DB query
    scholarships = [
        {
            'title': 'Merit Based Scholarship',
            'amount': 'Up to 50% tuition fee waiver',
            'deadline': '2026-01-15',
            'eligibility': 'Top 5% of incoming class or CGPA >= 8.5',
            'description': 'Awarded to outstanding students based on academic performance.',
            'apply_link': '#'
        },
        {
            'title': 'Need Based Grant',
            'amount': 'Varies (based on financial need)',
            'deadline': '2026-02-28',
            'eligibility': 'Students with demonstrated financial need',
            'description': 'Helps support tuition and living costs for eligible students.',
            'apply_link': '#'
        },
        {
            'title': 'Research Fellowship',
            'amount': 'Monthly stipend + project funds',
            'deadline': '2026-03-10',
            'eligibility': 'Postgraduate students engaged in approved research',
            'description': 'Supports research projects and thesis work for eligible candidates.',
            'apply_link': '#'
        }
    ]

    return render_template('views/scholarships.html', scholarships=scholarships)

#courses
@app.route('/courses')
def courses():
    return render_template('views/courses.html')

# departments
@app.route('/departments')
def departments():
    # Sample departments data — replace with DB or external source as needed
    departments = [
        {
            'name': 'Computer Science & Engineering',
            'head': 'Dr. Waseem Bakshi',
            'contact': '6006000001',
            'email': 'cse@uoknorth.edu.in',
            'description': 'Focuses on software engineering, AI, and data science programs.',
            'courses': ['B.Tech CSE', 'M.Tech CSE', 'PhD']
        },
        {
            'name': 'Business & Management Studies',
            'head': 'Prof. Rifat Ara',
            'contact': '6005000002',
            'email': 'bms@uoknorth.edu.in',
            'description': 'Provides programs in management, entrepreneurship, and applied economics.',
            'courses': ['BBA', 'MBA', 'PGDM']
        },
        {
            'name': 'English & Literature',
            'head': 'Dr. Bashir Bhat',
            'contact': '6005000003',
            'email': 'english@uoknorth.edu.in',
            'description': 'Covers classical and contemporary literature, critical theory, and creative writing.',
            'courses': ['BA English', 'MA English', 'PhD']
        }
    ]

    return render_template('views/departments.html', departments=departments)

#contact
@app.route('/contact')
def contact():
    return render_template('views/contact.html')


# hostels
@app.route('/hostels')
def hostels():
    return render_template('views/hostels.html')


# Transport services
@app.route('/transport')
def transport():
    # pass the transports data to the template
    return render_template('views/transport.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

