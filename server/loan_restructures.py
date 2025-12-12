"""
Loan Restructures API Module
Handles all CRUD operations for Loan Restructures
"""
from flask import Blueprint, request, jsonify
from utils import make_frappe_request, url_encode_doctype

loan_restructures_bp = Blueprint('loan_restructures', __name__)
DOCTYPE = "Loan Restructure"
ENCODED_DOCTYPE = url_encode_doctype(DOCTYPE)
BASE_ENDPOINT = f'/api/resource/{ENCODED_DOCTYPE}'


@loan_restructures_bp.route('/api/loan-restructures', methods=['POST'])
def create_loan_restructure():
    """Create a new loan restructure"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    status_code, response_data = make_frappe_request('POST', BASE_ENDPOINT, data)
    return jsonify(response_data), status_code


@loan_restructures_bp.route('/api/loan-restructures', methods=['GET'])
def get_loan_restructures():
    """Get list of loan restructures"""
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


@loan_restructures_bp.route('/api/loan-restructures/<restructure_name>', methods=['GET'])
def get_loan_restructure(restructure_name: str):
    """Get a specific loan restructure"""
    endpoint = f'{BASE_ENDPOINT}/{restructure_name}'
    status_code, response_data = make_frappe_request('GET', endpoint)
    return jsonify(response_data), status_code


@loan_restructures_bp.route('/api/loan-restructures/<restructure_name>', methods=['PUT'])
def update_loan_restructure(restructure_name: str):
    """Update a loan restructure"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    endpoint = f'{BASE_ENDPOINT}/{restructure_name}'
    status_code, response_data = make_frappe_request('PUT', endpoint, data)
    return jsonify(response_data), status_code


@loan_restructures_bp.route('/api/loan-restructures/<restructure_name>', methods=['DELETE'])
def delete_loan_restructure(restructure_name: str):
    """Delete a loan restructure"""
    endpoint = f'{BASE_ENDPOINT}/{restructure_name}'
    status_code, response_data = make_frappe_request('DELETE', endpoint)
    return jsonify(response_data), status_code

