"""creating bp routes for parcel delivery orders"""
from flask import Blueprint, request, jsonify
from app.version1.parcel_delivery_order.models import Parcels
from app.version1.parcel_delivery_order.validator import validate_parcel_data

ParcelObject = Parcels()


version1parcels_bp = Blueprint('version1parcels_bp', __name__, url_prefix='/api/v1/parcels')

@version1parcels_bp.route('/', methods=['GET', 'POST'])
def product():
    # Method to create and retrieve parcel delvery orders.
    if request.method == "POST":
        data = request.get_json()
        response = validate_parcel_data(data)
        if response == "valid":
            sender_name = data['sender_name']
            descr = data['descr']
            sent_from = data['sent_from']
            quantity = data['quantity']
            price = data['price']
            recipient_name = data['recipient_name']
            destination = data['destination']
            status = data['status']

            response = ParcelObject.add_parcel_order(
                sender_name, descr, sent_from, quantity, \
                price, recipient_name, destination, status)
        return jsonify({"message":response}), 201
    data = ParcelObject.get_all_parcels()
    return jsonify({"message":data}), 201

@version1parcels_bp.route('/<int:order_id>', methods=['GET'])
def get_parcel_by_id(order_id):
    """getting a parcel delivery record by the ID"""
    data = ParcelObject.get_one_parcel(order_id)
    return jsonify({"message":data}), 201
