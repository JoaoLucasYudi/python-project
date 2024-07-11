from flask import jsonify, Blueprint

links_routes_bp = Blueprint('links_routes',__name__)

@links_routes_bp.route('/links', methods=['POST'])
def create_link():
    return jsonify({'success': 'created successfully'}), 200