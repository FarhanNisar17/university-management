from flask import Flask, render_template

# Initialize Flask app & tells Flask where your HTML files live
app = Flask(__name__, template_folder='templates',static_folder='static')


# Define route for homepage
@app.route('/')
def home():
    return render_template('views/home.html')

# Students
@app.route('/register')
def students():
    return render_template('views/register.html')

#scholarships
@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')

#courses
@app.route('/courses')
def courses():
    return render_template('courses.html')

#contacts
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


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

