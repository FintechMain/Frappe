"""
Process Loan Classification API Module
Handles all CRUD operations for Process Loan Classification
"""
from flask import Blueprint, request, jsonify
from utils import make_frappe_request, url_encode_doctype

process_loan_classification_bp = Blueprint('process_loan_classification', __name__)
DOCTYPE = "Process Loan Classification"
ENCODED_DOCTYPE = url_encode_doctype(DOCTYPE)
BASE_ENDPOINT = f'/api/resource/{ENCODED_DOCTYPE}'


@process_loan_classification_bp.route('/api/process-loan-classification', methods=['POST'])
def create_process_loan_classification():
    """Create a new process loan classification"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    status_code, response_data = make_frappe_request('POST', BASE_ENDPOINT, data)
    return jsonify(response_data), status_code


@process_loan_classification_bp.route('/api/process-loan-classification', methods=['GET'])
def get_process_loan_classification():
    """Get list of process loan classification records"""
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


@process_loan_classification_bp.route('/api/process-loan-classification/<process_name>', methods=['GET'])
def get_one_process_loan_classification(process_name: str):
    """Get a specific process loan classification"""
    endpoint = f'{BASE_ENDPOINT}/{process_name}'
    status_code, response_data = make_frappe_request('GET', endpoint)
    return jsonify(response_data), status_code


@process_loan_classification_bp.route('/api/process-loan-classification/<process_name>', methods=['PUT'])
def update_process_loan_classification(process_name: str):
    """Update a process loan classification"""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is required'}), 400
    endpoint = f'{BASE_ENDPOINT}/{process_name}'
    status_code, response_data = make_frappe_request('PUT', endpoint, data)
    return jsonify(response_data), status_code


@process_loan_classification_bp.route('/api/process-loan-classification/<process_name>', methods=['DELETE'])
def delete_process_loan_classification(process_name: str):
    """Delete a process loan classification"""
    endpoint = f'{BASE_ENDPOINT}/{process_name}'
    status_code, response_data = make_frappe_request('DELETE', endpoint)
    return jsonify(response_data), status_code

