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

    def test_add_parcel_order(self):
        """Tests for adding a new parcel delivery order"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("Parcel delivery order successfully created", str(response.data))
    
    def test_if_parcel_exists(self):
        """Tests if a parcel delivery order already exists"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel_2), content_type='application/json')
        #self.assertEqual(response.status_code, 401)
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
        #self.assertEqual(response.status_code, 200)
    
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
