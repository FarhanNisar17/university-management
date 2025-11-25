from flask import Blueprint, render_template

contact_bp = Blueprint('contact', __name__, url_prefix='/contacts')

#/contacts/

@contact_bp.route('/')
def contact_home():
    return render_template('views/contacts.html')
