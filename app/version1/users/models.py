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
        
        if role != "reg user":
            return {"msg":"you can only register as a regular user"}
        
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
            return {'msg':'Error logging in, ensure username or password are incorrect'}, 401
        return {'msg':'Log in succesful'}, 200
            