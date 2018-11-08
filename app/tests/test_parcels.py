"""Unit tests for the parcel creation and getting the parcels"""

import unittest
import json
from app import create_app

class TestParcels(unittest.TestCase):
    """Class containing all tests for the parcel resource"""
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.parcel = {
            "sender_name":"Joseph",
            "descr":"tv",
            "sent_from":"Nairobi",
            "quantity":50,
            "price":50,
            "recipient_name":"Otile",
            "destination":"Nakuru",
            "status":"sent"
        }
        self.parcel_2 = {
            "sender_name":"Joseph",
            "descr":"tv",
            "sent_from":"Nairobi",
            "quantity":50,
            "price":50,
            "recipient_name":"Otile",
            "destination":"Nakuru",
            "status":"sent"
        }
        self.parcel_3 = {
            "sender_name":"Joseph",
            "descr":"reams",
            "sent_from":"Nairobi",
            "quantity":50,
            "price":50,
            "recipient_name":"Otile",
            "destination":"Nakuru",
            "status":"delivered"
        }
        self.parcel_4 = {
            "sender_name":"Joseph",
            "descr":"nails",
            "sent_from":"Nairobi",
            "quantity":-4,
            "price":-50,
            "recipient_name":"Otile",
            "destination":"Nakuru",
            "status":"delivered"
        }
        self.parcel_5 = {
            "sender_name":"",
            "descr":"",
            "sent_from":"",
            "quantity":"",
            "price":"",
            "recipient_name":"",
            "destination":"",
            "status":""
        }
        self.parcel_6 = {
            "sender_name":"Joseph",
            "descr":"nails",
            "sent_from":"Nairobi",
            "quantity":4,
            "price":50,
            "recipient_name":"Otile",
            "destination":"Nakuru",
            "status":"repeated"
        }

    def test_add_parcel_order(self):
        """Tests for adding a new parcel delivery order"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Parcel delivery order successfully created", str(response.data))
    
    def test_if_parcel_exists(self):
        """Tests if a parcel delivery order already exists"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel_2), content_type='application/json')
        #self.assertEqual(response.status_code, 400)
        self.assertIn("Parcel order delivery already exists", str(response.data))
    
    def test_if_arguemnt_has_negative_values(self):
        """Tests if a negative value has been supplied"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel_4), content_type='application/json')
        #self.assertEqual(response.status_code, 401)
        self.assertIn("The minimum unit price must be above 0", str(response.data))

    def test_if_status_is_wrong(self):
        """Tests if status is not sent"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel_3), content_type='application/json')
        #self.assertEqual(response.status_code, 201)
        self.assertIn("status, can only be sent when creating an order", str(response.data))
    
    def test_to_get_all_parcels(self):
        """Test to get all parcel delivery orders"""
        response = self.client().get('/api/v1/parcels/')
        #self.assertEqual(response.status_code, 201)
    
    def test_for_fetching_a_specific_parcel_order(self):
        """Test to successfully fetch a specific parcel order"""
        response = self.client().get('/api/v1/parcels/1')
        #self.assertEqual(response.status_code, 200)
        self.assertIn("tv", str(response.data))
    
    def test_for_fetching_a_specific_parcel_details(self):
        """Test when a specific parcel does not exist"""
        response = self.client().get('/api/v1/parcels/1000')
        #self.assertEqual(response.status_code, 404)
        self.assertIn("Parcel not found", str(response.data))

    def test_for_posting_empty_fields(self):
        """tests if the user is trying to post with an empty field"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel_5), content_type='application/json')
        self.assertIn("Quantity must be a number", str(response.data))

    def test_change_an_order_parcel(self):
        """Test for changing a delivery order"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v1/parcels/1', data=json.dumps(self.parcel_3), content_type='application/json')
        result = self.client().get('/api/v1/parcels/1')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn('reams', str(result.data)) 

    def test_change_an_order_parcel_wrong_status(self):
        """Test for changing a delivery order with wrong status"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v1/parcels/1', data=json.dumps(self.parcel_6), content_type='application/json')
        result = self.client().get('/api/v1/parcels/1')
        #self.assertEqual(response.status_code, 200)
        #self.assertIn('reams', str(result.data)) 
        #self.assertIn("You can only change the status to canceled", str(response.data))

    def test_change_an_order_parcel_wrong_id(self):
        """Test for changing a delivery order with wrong id"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v1/parcels/1000', data=json.dumps(self.parcel_6), content_type='application/json')
        result = self.client().get('/api/v1/parcels/1')
        #self.assertIn("No parcel delivery order with that id.", str(response.data))
