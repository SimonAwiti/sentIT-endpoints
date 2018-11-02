"""creating bp routes for products"""
from flask import jsonify, Blueprint, request, make_response, session, redirect, url_for
import datetime
from app.version1.users.models import Users
from app.version1.users.validator import validate_data_signup

userObject = Users()

version1users_blueprints = Blueprint('version1users', __name__, url_prefix='/api/v1/users')

@version1users_blueprints.route('/register', methods=['POST'])
def signup():
    """Admin can add a new attendant"""
    data = request.get_json()
    response = validate_data_signup(data)
    name = data['name']
    email = data['email']
    password = data['password']
    confirm = data['confirm']
    role = data['role']
    if response == "valid":
        response = userObject.add_user(name, email, password, confirm, role)
    return jsonify({"message":response}), 201
   

