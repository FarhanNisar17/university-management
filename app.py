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
    return render_template('views/scholarships.html')

#departments
@app.route('/departments')
def departments():
    return render_template('views/departments.html')

#hostels
@app.route('/hostels')
def hostels():
    return render_template('views/hostels.html')

#transport
@app.route('/transport')
def transport():
    return render_template('views/transport.html')

#courses
@app.route('/courses')
def courses():
    return render_template('views/courses.html')

#contact
@app.route('/contact')
def contact():
    return render_template('views/contact.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

