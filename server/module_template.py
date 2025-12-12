"""
Template for creating CRUD API modules
This is a reference template - copy and modify for new modules
"""
from flask import Blueprint, request, jsonify
from utils import make_frappe_request, url_encode_doctype

# Create blueprint
module_bp = Blueprint('module_name', __name__)

# Set the doctype name
DOCTYPE = "Your DocType Name"


def create_crud_endpoints(blueprint, doctype_name, route_prefix):
    """
    Create standard CRUD endpoints for a doctype
    
    Args:
        blueprint: Flask Blueprint instance
        doctype_name: Name of the Frappe DocType
        route_prefix: URL prefix for routes (e.g., 'api/loan-products')
    """
    encoded_doctype = url_encode_doctype(doctype_name)
    base_endpoint = f'/api/resource/{encoded_doctype}'
    
    @blueprint.route(f'/{route_prefix}', methods=['POST'])
    def create():
        """Create a new document"""
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        status_code, response_data = make_frappe_request('POST', base_endpoint, data)
        return jsonify(response_data), status_code
    
    @blueprint.route(f'/{route_prefix}', methods=['GET'])
    def list_all():
        """Get list of documents"""
        params = {}
        if request.args.get('fields'):
            params['fields'] = request.args.get('fields')
        if request.args.get('filters'):
            params['filters'] = request.args.get('filters')
        if request.args.get('limit_start'):
            params['limit_start'] = request.args.get('limit_start')
        if request.args.get('limit_page_length'):
            params['limit_page_length'] = request.args.get('limit_page_length')
        
        endpoint = base_endpoint
        if params:
            query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
            endpoint = f"{endpoint}?{query_string}"
        
        status_code, response_data = make_frappe_request('GET', endpoint)
        return jsonify(response_data), status_code
    
    @blueprint.route(f'/{route_prefix}/<doc_name>', methods=['GET'])
    def get_one(doc_name):
        """Get a specific document"""
        endpoint = f'{base_endpoint}/{doc_name}'
        status_code, response_data = make_frappe_request('GET', endpoint)
        return jsonify(response_data), status_code
    
    @blueprint.route(f'/{route_prefix}/<doc_name>', methods=['PUT'])
    def update(doc_name):
        """Update a document"""
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        endpoint = f'{base_endpoint}/{doc_name}'
        status_code, response_data = make_frappe_request('PUT', endpoint, data)
        return jsonify(response_data), status_code
    
    @blueprint.route(f'/{route_prefix}/<doc_name>', methods=['DELETE'])
    def delete(doc_name):
        """Delete a document"""
        endpoint = f'{base_endpoint}/{doc_name}'
        status_code, response_data = make_frappe_request('DELETE', endpoint)
        return jsonify(response_data), status_code

