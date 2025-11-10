from flask import Flask, render_template

# Initialize Flask app & tells Flask where your HTML files live
app = Flask(__name__, template_folder='Frontend')


# Define route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Students
@app.route('/students')
def students():
    return render_template('students.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
