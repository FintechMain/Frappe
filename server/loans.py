"""
Loans API Module
Handles all CRUD operations for Loans
"""
from flask import Blueprint, request, jsonify
from utils import make_frappe_request, url_encode_doctype

loans_bp = Blueprint('loans', __name__)
DOCTYPE = "Loan"
ENCODED_DOCTYPE = url_encode_doctype(DOCTYPE)
BASE_ENDPOINT = f'/api/resource/{ENCODED_DOCTYPE}'


@loans_bp.route('/api/loans', methods=['POST'])
def create_loan():
    """Create a new loan"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    status_code, response_data = make_frappe_request('POST', BASE_ENDPOINT, data)
    return jsonify(response_data), status_code


@loans_bp.route('/api/loans', methods=['GET'])
def get_loans():
    """Get list of loans"""
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


@loans_bp.route('/api/loans/<loan_name>', methods=['GET'])
def get_loan(loan_name: str):
    """Get a specific loan"""
    endpoint = f'{BASE_ENDPOINT}/{loan_name}'
    status_code, response_data = make_frappe_request('GET', endpoint)
    return jsonify(response_data), status_code


@loans_bp.route('/api/loans/<loan_name>', methods=['PUT'])
def update_loan(loan_name: str):
    """Update a loan"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    endpoint = f'{BASE_ENDPOINT}/{loan_name}'
    status_code, response_data = make_frappe_request('PUT', endpoint, data)
    return jsonify(response_data), status_code


@loans_bp.route('/api/loans/<loan_name>', methods=['DELETE'])
def delete_loan(loan_name: str):
    """Delete a loan"""
    endpoint = f'{BASE_ENDPOINT}/{loan_name}'
    status_code, response_data = make_frappe_request('DELETE', endpoint)
    return jsonify(response_data), status_code

