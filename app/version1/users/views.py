"""creating bp routes for users"""
from flask import jsonify, Blueprint, request, make_response, session, redirect, url_for
import datetime
from app.version1.users.models import Users
from app.version1.users.validator import validate_data_signup, validate_data_login

userObject = Users()

version1users_blueprints = Blueprint('version1users', __name__, url_prefix='/api/v1/users')

@version1users_blueprints.route('/register', methods=['POST'])
def signup():
    """user can get registered into the app"""
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

@version1users_blueprints.route('/login', methods=['POST'])
def login():
    """ Method to login regular user """
    data = request.get_json()
    response = validate_data_login(data)
    if response == "valid":
        name = data['name']
        password = data['password']
        response = userObject.login(name, password)
    return jsonify({"message": response}), 401
    
   
@version1users_blueprints.route('/admin_login', methods=['POST'])
def admin_login():
    """ Method to login admin user """
    data = request.get_json()
    response = validate_data_login(data)
    if response == "valid":
        name = data['name']
        password = data['password']
        response = userObject.admin_login(name, password, password)
    return jsonify({"message": response}), 401

@version1users_blueprints.route('/register/<int:user_id>', methods=['PUT'])
def add_admin():
    """user can get registered into the app"""
    data = request.get_json()
    response = validate_data_signup(data)
    role = data['role']
    if response == "valid":
        response = userObject.edit_user_role(role, role)
    return jsonify({"message":response}), 201
   