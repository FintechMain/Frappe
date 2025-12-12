"""
Users API Module
Handles all CRUD operations for Users
"""
from flask import Blueprint, request, jsonify
from utils import make_frappe_request, url_encode_doctype

users_bp = Blueprint('users', __name__)
DOCTYPE = "User"
ENCODED_DOCTYPE = url_encode_doctype(DOCTYPE)
BASE_ENDPOINT = f'/api/resource/{ENCODED_DOCTYPE}'


@users_bp.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    status_code, response_data = make_frappe_request('POST', BASE_ENDPOINT, data)
    return jsonify(response_data), status_code


@users_bp.route('/api/users', methods=['GET'])
def get_users():
    """Get list of users"""
    params = {}
    if request.args.get('fields'):
        params['fields'] = request.args.get('fields')
    if request.args.get('filters'):
        params['filters'] = request.args.get('filters')
    if request.args.get('limit_start'):
        params['limit_start'] = request.args.get('limit_start')
    if request.args.get('limit_page_length'):
        params['limit_page_length'] = request.args.get('limit_page_length')
    
    endpoint = BASE_ENDPOINT
    if params:
        query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
        endpoint = f"{endpoint}?{query_string}"
    
    status_code, response_data = make_frappe_request('GET', endpoint)
    return jsonify(response_data), status_code


@users_bp.route('/api/users/<user_name>', methods=['GET'])
def get_user(user_name: str):
    """Get a specific user"""
    endpoint = f'{BASE_ENDPOINT}/{user_name}'
    status_code, response_data = make_frappe_request('GET', endpoint)
    return jsonify(response_data), status_code


@users_bp.route('/api/users/<user_name>', methods=['PUT'])
def update_user(user_name: str):
    """Update a user"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    endpoint = f'{BASE_ENDPOINT}/{user_name}'
    status_code, response_data = make_frappe_request('PUT', endpoint, data)
    return jsonify(response_data), status_code


@users_bp.route('/api/users/<user_name>', methods=['DELETE'])
def delete_user(user_name: str):
    """Delete a user"""
    endpoint = f'{BASE_ENDPOINT}/{user_name}'
    status_code, response_data = make_frappe_request('DELETE', endpoint)
    return jsonify(response_data), status_code

