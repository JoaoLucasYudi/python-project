from flask import jsonify, Blueprint

trips_route_bp = Blueprint('trip_routes', __name__)

@trips_route_bp.route('/trips', methods=['POST'])
def create_trip():
    return jsonify({'success': 'created successfully'}), 200