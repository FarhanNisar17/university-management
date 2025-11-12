from flask import Flask, render_template

# Initialize Flask app & tells Flask where your HTML files live
app = Flask(__name__, template_folder='templates',static_folder='static')

# Sample transport services data
transports = [
    {
        'name': 'North Campus Express',
        'number': 'JK01AB 6862',
        'route': 'Nowgam ⇄ North Campus',
        'driver': 'Mr Showkat Pandit',
        'contact': '+91-9000000001',
        'fare': '₹3000'
    },
    {
        'name': 'North Campus Tortoise',
        'number': 'JK01BC 3874',
        'route': 'Ganderbal ⇄ North Campus',
        'driver': 'Mr Farooq Ahmed',
        'contact': '+91-9000000002',
        'fare': '₹3000'
    },
    {
        'name': 'North Campus Quicker',
        'number': 'JK01BC 3853',
        'route': 'Sopore ⇄ North Campus',
        'driver': 'Mr Hilal Lone',
        'contact': '+91-9000000003',
        'fare': ' ₹3000 '
    }
]

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
    return render_template('views/scholarships.html')

#courses
@app.route('/courses')
def courses():
    return render_template('views/courses.html')

#contacts
@app.route('/contacts')
def contacts():
    return render_template('views/contacts.html')


# hostels
@app.route('/hostels')
def hostels():
    return render_template('views/hostels.html')


# Transport services
@app.route('/transport')
def transport():
    # pass the transports data to the template
    return render_template('views/transport.html', transports=transports)

# Transport apply form
@app.route('/transport/apply/<int:bus_id>')
def transport_apply(bus_id):
    if 0 <= bus_id < len(transports):
        bus = transports[bus_id]
        return render_template('views/transport-apply.html', bus=bus, bus_id=bus_id)
    return "Bus not found", 404

# Handle transport form submission
@app.route('/transport/submit', methods=['POST'])
def submit_transport_application():
    from flask import request
    name = request.form.get('name')
    address = request.form.get('address')
    pickup = request.form.get('pickup')
    bus_id = request.form.get('bus_id')
    
    # Here you can save to database or send email
    # For now, just return a success message
    return render_template('views/transport-success.html', 
                         name=name, address=address, pickup=pickup, bus_id=bus_id)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

