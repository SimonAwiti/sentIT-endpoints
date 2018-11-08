"""handles all operations for creating and fetching data relating to parcels delivery orders"""

from flask import request, jsonify

parcels = []

def check_if_parcel_exists(item):
    """
    Helper function to check if a parcel delivery order exists
    Returns True if parcel already exists, else returns False
    """
    parcel = [parcel for parcel in parcels if parcel['descr'] == item.rstrip()]
    if parcel:
        return True
    return False

def check_if_numbers_are_negatives(quantity, price):
    """
    Helper function to check if any negative numbers were supplied in the JSON object
    Returns True if any number is less than 0, else returns False
    """
    if quantity < 0 or price < 0 :
        return True
    return False

class Parcels():
    """Class to handle  the creation of parcel orders"""
    def add_parcel_order(self, sender_name, descr, sent_from, \
                quantity, price, recipient_name, destination, status):
                    """Add an order to the parcel delivery order list"""
                    # Get the JSON object values
                    sender_name = request.json.get('sender_name', None)
                    descr = request.json.get('descr', None)
                    sent_from = request.json.get('sent_from', None)
                    quantity = request.json.get('quantity', None)
                    price = request.json.get('price', None)
                    recipient_name = request.json.get('recipient_name', None)
                    destination = request.json.get('destination', None)
                    status = request.json.get('status', None)

                    if sender_name == '' or descr == '' or sent_from == '' or quantity == '' \
                    or price == '' or recipient_name == '' or destination == '' or status == '':
                        return {'error': 'Fields cannot be empty'}, 401 

                    # Check for duplicate of the order items
                    present = check_if_parcel_exists(descr)
                    if present:
                        return {'msg':'Parcel order delivery already exists'}, 401

                    # ensure that status is sent
                    if status != "sent":
                        return {'msg':'status, can only be sent when creating an order'}, 401

                    # Checks for numbers less than 0
                    size = check_if_numbers_are_negatives(quantity, price)
                    if size:
                        return {'msg':'Cannot supply a value less than 0'}, 401

        
                    # Add all values to a parcel delivery dictionary
                    parcel_dict = {
                        "order_id": len(parcels) + 1,
                        "sender_id": len(parcels) + 1,
                        "sender_name" : sender_name.rstrip(),
                        "descr" : descr,
                        "sent_from" : sent_from,
                        "quantity" : quantity,
                        "price" : price,
                        "recipient_name" : recipient_name,
                        "destination" : destination,
                        "status" : status
                    }
                    # Append to the parcel order ditalis to list
                    parcels.append(parcel_dict)
                    return {"msg": "Parcel delivery order successfully created"}, 200

    def get_all_parcels(self):
        """Fetch all parcels delivery orders from the list"""
        # If parcel list is empty
        if len(parcels) == 0:
            return {'msg':'No parcel delivery order added yet'}, 401
        return jsonify({'parcel orders':parcels}), 200
    
    def get_one_parcel(self, order_id):
        """Fetches a specific parcel order from the percel delivery order list"""
        parcel = [parcel for parcel in parcels if parcel['order_id'] == order_id]
        if parcel:
            return jsonify({'parcel order': parcel}), 200
        # no parcel order found
        return jsonify({'msg':'Parcel not found'}), 401

    def update_parcel(self, order_id, sender_name, descr, sent_from, \
                quantity, price, recipient_name, destination, status):
        """ update parcel delivery order """
        if status != "canceled":
            return {'msg':'You can only change the status to canceled'}, 401

        for parcel in parcels:
            if parcel['order_id'] == order_id:
                if parcel['status'] != "delivered" and parcel['status'] != "on-transit":
                    parcel['sender_name'] = sender_name
                    parcel['descr'] = descr
                    parcel['sent_from'] = sender_name
                    parcel['quantity'] = quantity
                    parcel['price'] = price
                    parcel['recipient_name'] = recipient_name
                    parcel['destination'] = destination
                    parcel['status'] = status
                    return jsonify({
                        "message": "Update Successful.",
                        "Product": parcels}), 201
                return jsonify({
                    'msg':'Canceling error! Order is being transported or already deliverd'}), 401        
        return jsonify({
                "message": "No parcel delivery order with that id."}), 404
 