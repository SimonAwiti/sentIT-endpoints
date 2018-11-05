"""Unit tests for the users resources"""

import unittest
import json
from app import create_app

class TestUsers(unittest.TestCase):
    """Class containing all tests for the users resource"""
    def setUp(self):
        """initializing the tests"""
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.user = {
            "name":"Simon",
            "email":"simonawiti@gmail.com",
            "password":"pass123",
            "confirm":"pass123",
            "role":"reg user"
        }
        self.user1 = {
            "name":"Ken",
            "email":"kenjoseph@gmail.com",
            "password":"pass123",
            "confirm":"pass124",
            "role":"reg user"
        }
        self.user2 = {
            "name":"Ken",
            "email":"seph@gmail.com",
            "password":"pass",
            "confirm":"pass",
            "role":"reg user"
        }
        self.user3 = {
            "name":"Ken",
            "email":"seph@gmail.com",
            "password":"pass",
            "confirm":"pass",
            "role":"admin"
        }
        
        self.login = {
            "name":"simon",
            "password":"pass123"
        }
        self.login1 = {
            "name":"ken",
            "password":"pass123"
        }
        self.login2 = {
            "name":"",
            "password":""
        }
    
    def tearDown(self):
        users = []

    def test_add_user(self):
        """Tests for adding a new user"""
        response = self.client().post('/api/v1/users/register', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Succesfully Registered, Log in to SendIT", str(response.data))

    def test_add_user_wrong_role(self):
        """Tests for adding an admin new user"""
        response = self.client().post('/api/v1/users/register', data=json.dumps(self.user3), content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        self.assertIn("you can only register as a regular user", str(response.data))
    
    def test_add_user_wrong_passwords(self):
        """Tests for checking if password match"""
        response = self.client().post('/api/v1/users/register', data=json.dumps(self.user1), content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        self.assertIn("Passwords do not match", str(response.data))
    
    def test_password_length(self):
        """Tests for the length of the passwords"""
        response = self.client().post('/api/v1/users/register', data=json.dumps(self.user2), content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        self.assertIn("Password length should be between 6 and 12 characters long", str(response.data))

    def test_for_successful_login(self):
        """Tests if a user successfully logged in"""
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.login), content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(resource.content_type, 'application/json')
    
    def test_wrong_credentials_supplied(self):
        """Tests if the wrong credentials were passed in"""
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.login1), content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('Error logging in, ensure username or password are correct', str(response.data))

    def test_no_credentials_supplied(self):
        """Tests if the no credentials were passed in"""
        response = self.client().post('/api/v1/users/login', data=json.dumps(self.login1), content_type='application/json')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('Error logging in, ensure username or password are correct', str(response.data))
