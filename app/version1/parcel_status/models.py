"""handles all operations for the admin in fetching data relating to parcels delivery orders"""
from flask import request, jsonify

#local import 
from app.version1.parcel_delivery_order.models import parcels
from app.version1.parcel_delivery_order.models import check_if_parcel_exists


def check_if_parcel_order_exist(item):
    """
    Helper function to check if a parcel order by the client exists
    Returns True if the parcel already exists, else returns False
    """
    parcels = check_if_parcel_exists(item) 
    if parcels is True:
        True
    return False

def updated_status(order_id, status):
    """ checks if a parcel delivery order is updated succesfully, returns true if yes """
    if  status == '':
        return {
        "message": "Field cannot be empty"
        }, 401

    if status != "delivered" and status != "on-transit":
        return {
        "message": "status, can only be edited to on-transit or delivered"
        }, 401

    for parcel in parcels:
        if parcel['order_id'] == order_id:
            parcel['status'] = status
            return True
        return False

class ParcelStatus():
    """handles all the operations by the admin in editing the status and getting the parcels orders"""
    def get_all_parcels(self):
        """Fetch all parcels delivery orders from the list"""
        # If parcel list is empty
        if len(parcels) == 0:
            return {'msg':'No parcel delivery order added yet'}, 401
        return {'parcel orders':parcels}, 200

    def get_parcel_by_user(self, sender_id):
        """ Fetch sales rec by a certain sender """
        for parcel in parcels:
            if parcel['sender_id'] == sender_id:
                return jsonify({
                    "message": "Successful.",
                    "sales record": parcel}), 200
        return jsonify({
                "message": "No parcel record by that sender."
                }), 404

    def update_parcel_order(
        self, order_id, status):
        """ update status of the parcel order """
        if  status == '':
            return {
            "message": "Field cannot be empty"
            }, 401

        if status != "delivered" and status != "on-transit":
            return {
            "message": "status, can only be edited to on-transit or delivered"
            }, 401

        for parcel in parcels:
            if parcel['status'] != "canceled":
                if parcel['order_id'] == order_id:
                    parcel['status'] = status
                    return jsonify({
                        "message": "Update Successful.",
                        "Parcel order": parcel}), 201
            return {
                   "message": "You cannot edit a canceled delivery order"
                    }, 401                           
        return {
            "message": "No parcel order with that id."
            }, 404
