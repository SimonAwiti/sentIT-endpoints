"""Unit tests for the parcel editing and getting the parcels orders"""

import unittest
import json
from app import create_app

class TestParcelsStatus(unittest.TestCase):
    """Class containing all tests for the parcel resource"""
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['Testing'] = True
        self.client = self.app.test_client
        self.parcel = {
            "order_id":1,
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
            "order_id":2,
            "status":"delivered"
        }
        self.parcel_3 = {
            "order_id":3,
            "status":"still on the road"
        }

    def test_change_an_order_parcel(self):
        """Test for changing a delivery order"""
        response = self.client().post('/api/v1/parcels/', data=json.dumps(self.parcel), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v1/admin_parcels/Joseph', data=json.dumps(self.parcel_2), content_type='application/json')
        result = self.client().get('/api/v1/admin_parcels/Joseph')
        #self.assertEqual(response.status_code, 200)
        self.assertIn('1', str(result.data)) 

    def test_to_get_all_parcels(self):
        """Test to get all parcel delivery orders"""
        response = self.client().get('/api/v1/admin_parcels/')
        self.assertEqual(response.status_code, 201)  

    def test_for_fetching_a_specific_parcel_order(self):
        """Test to successfully fetch a specific parcel order"""
        response = self.client().get('/api/v1/admin_parcels/Joseph')
        self.assertEqual(response.status_code, 200)
        self.assertIn("tv", str(response.data))

    def test_for_fetching_a_specific_parcel_order_with_no_user(self):
        """Test to successfully fetch a specific parcel order"""
        response = self.client().get('/api/v1/admin_parcels/Rotas')
        self.assertEqual(response.status_code, 404)
        self.assertIn("No parcel record by that sender.", str(response.data))

    def test_for_fetching_a_specific_parcel_order_with_no_id(self):
        """Test to successfully fetch a specific parcel order"""
        response = self.client().get('/api/v1/admin_parcels/300')
        self.assertEqual(response.status_code, 404)
        self.assertNotIn("No parcel order with that id", str(response.data))
    