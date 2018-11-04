"""handles all operations for creating and fetching data relating to users"""

from flask import request

# List to hold all users
users = [
    {
        "id": 0,
        "name" : "admin",
        "email" : "admin@email",
        "password" : "admin123",
        "role" : "admin"
    }
]

def generate_admin():
    """creates my first admin"""
    users_dict = {
        "id": 0,
        "name" : "admin",
        "password" : "admin123",
        "role" : "admin"
    }
    users.append(users_dict)

def check_if_user_exists(item):
    """
    Function to check if a user exists
    Returns True if user already exists, else returns False
    """
    user = [user for user in users if user['name'] == item.rstrip()]
    if user:
        return True
    return False

def verify_credentials(name, password):
    """
    Function to check if passwords match
    Returns True if user already exists, else returns False
    """
    user = [user for user in users if user['name'] == name and user['password'] == password]
    if user:
        return True
    return False

def is_admin(role):
    """
    Function to check if the user is and administrator
    """
    user = [user for user in users if user['role'] == "admin"]
    if user:
        return True
    return False

class Users():
    """Class to handle users"""
    def add_user(self, name, email, password, confirm, role):
        """Registers a new user"""
        name = request.json.get('name', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        confirm = request.json.get('confirm', None)
        role = request.json.get('role', None)
        # Checks for empty inputs
        if name == '' or password == '' or confirm == '':
            return {'error': 'Fields cannot be empty'}, 401

        if password != confirm:
            return {'msg':"Passwords do not match"}, 401

        if len(password) < 6 or len(password) > 12:
            return {'msg': "Password length should be between 6 and 12 characters long"}, 401

        duplicate = check_if_user_exists(name)
        if duplicate:
            return {'msg':'User already exists'}, 401
        
        user_dict = {
            "id": len(users) + 1,
            "name" : name.rstrip(),
            "email" : email,
            "password" : password,
            "role" :  role
        }
        users.append(user_dict)
        return {'msg':"Succesfully Registered, Log in to SendIT"}

    def login(self, name, password):
        """Logs in a regular user"""
        name = request.json.get('name', None)
        password = request.json.get('password', None)
        
        # Check for enpty inputs
        if name == '' or password == '':
            return {'error': 'Fields cannot be empty'}, 401

        credentials = verify_credentials(name, password)
        if not credentials:
            return {'msg':'Error logging in, ensure username or password are correct'}, 401
        return {'msg':'Log in succesful'}, 200

    def admin_login(self, name, role, password):
        """Logs in administrator user"""
        name = request.json.get('name', None)
        password = request.json.get('password', None)
        
        # Check for enpty inputs
        if name == '' or password == '':
            return {'error': 'Fields cannot be empty'}, 401

        credentials = verify_credentials(name, password)
        if not credentials:
            return {'msg':'Error logging in, ensure username or password are correct'}, 401

        administrator = is_admin(role)
        if not administrator:
            return {'msg':'Administrator log in only'}, 401
        return {'msg':'Log in succesful'}, 200

    def edit_user_role(self, user_id, role):
        """Admin changes reguser role to admin"""
        if not users:
            return "No registered users"
        if isinstance(user_id, int) is False:
            return "User Id should be a number"
        administrator = is_admin(role)
        if not administrator:
            return {'msg':'Only the admin can edit the role'}, 401
        for user in range(len(users)):
            if user_id != users[user]["user_id"]:
                continue
            user["role"] = "admin"
            return "User was promoted to admin"
            