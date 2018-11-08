"""creating bp routes for the admin operations"""
from flask import Blueprint, request, jsonify
from app.version1.parcel_status.models import ParcelStatus
from app.version1.parcel_delivery_order.validator import validate_parcel_data

ParcelObject = ParcelStatus()


version1pstatus_bp = Blueprint('version1pstatus_bp', __name__, url_prefix='/api/v1/admin_parcels')

@version1pstatus_bp.route('/<int:sender_id>', methods=['GET'])
def get_parcel_order_by_sender(sender_id, **kwargs):
    """getting sale record by name of sender"""
    data = ParcelObject.get_parcel_by_user(sender_id)
    return data

@version1pstatus_bp.route('/', methods=['GET'])
def get_all_parcels_orders_by_client():
    """getting all the parcel delivery orders"""
    data = ParcelObject.get_all_parcels()
    return data

@version1pstatus_bp.route('/<int:order_id>', methods=['PUT'])
def edit_parcel_by_client(order_id):
    """change the status of the parcel delivery record"""
    data = request.get_json()
    status = data['status']
    response = ParcelObject.update_parcel_order(order_id, status)
    return jsonify ({"message": response})
