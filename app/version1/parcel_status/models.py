"""handles all operations for the admin in fetching data relating to parcels delivery orders"""
from flask import request, jsonify

#local import 
from app.version1.parcel_delivery_order.models import parcels, check_if_parcel_exists

"""list of all the parcel delivery orders by clients"""
client_parcels = parcels

def check_if_parcel_order_exist(item):
    """
    Helper function to check if a parcel order by the client exists
    Returns True if the parcel already exists, else returns False
    """
    parcels = check_if_parcel_exists(item) 
    if parcels is True:
        True
    return False

class ParcelStatus():
    """handles all the operations by the admin in editing the status and getting the parcels orders"""
    def get_all_parcels(self):
        """Fetch all parcels delivery orders from the list"""
        # If parcel list is empty
        if len(parcels) == 0:
            return {'msg':'No parcel delivery order added yet'}, 401
        return {'parcel orders':parcels}, 200

    def get_parcel_by_user(self, sender_name):
        """ Fetch sales rec by a certain sender """
        for parcel in parcels:
            if parcel['sender_name'] == sender_name:
                return jsonify({
                    "message": "Successful.",
                    "sales record": parcel}), 200
        return jsonify({
                "message": "No parcel record by that sender."}), 404

    def update_parcel_order(
        self, order_id, status):
        """ update status of the parcel order """
        if  status == '':
            return jsonify({
            "message": "Field cannot be empty"}), 401

        if status != "delivered" and status != "on-transit":
            return jsonify({
            "message": "status, can only be edited to on-transit or delivered"}), 401

        for parcel in parcels:
            if parcel['order_id'] == order_id:
                parcel['status'] = status
                return jsonify({
                    "message": "Update Successful.",
                    "Parcel order": parcel}), 201
        return jsonify({
            "message": "No parcel order with that id."}), 404