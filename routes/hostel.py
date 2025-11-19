from flask import Blueprint, render_template

hostel_bp = Blueprint('hostel', __name__, url_prefix='/hostels')

@hostel_bp.route('/')
def hostel_home():
    return render_template('views/hostels.html')
