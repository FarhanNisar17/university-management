from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.students import Student
from util.extensions import db

transport_bp = Blueprint('transport', __name__, url_prefix="/transport")

@transport_bp.route('/')
def transport():
    # pass the transports data to the template
    return render_template('views/transport.html')