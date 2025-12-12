"""
Shared utility functions for all API modules
"""
import requests
import os
from typing import Dict, Optional, Tuple

# Frappe Configuration
FRAPPE_BASE_URL = os.getenv('FRAPPE_BASE_URL', 'http://127.0.0.1:8000')
FRAPPE_SITE_NAME = os.getenv('FRAPPE_SITE_NAME', 'lending.localhost')
FRAPPE_API_KEY = os.getenv('FRAPPE_API_KEY', '64726967de821d4')
FRAPPE_API_SECRET = os.getenv('FRAPPE_API_SECRET', '18fe12924de8f23')


def get_frappe_headers() -> Dict[str, str]:
    """
    Generate headers for Frappe API requests
    Includes authentication token and site name
    """
    return {
        'Authorization': f'token {FRAPPE_API_KEY}:{FRAPPE_API_SECRET}',
        'Content-Type': 'application/json',
        'Host': FRAPPE_SITE_NAME
    }


def make_frappe_request(method: str, endpoint: str, data: Optional[Dict] = None) -> Tuple[int, Dict]:
    """
    Make a request to Frappe API
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        endpoint: API endpoint path
        data: Request body data (optional)
    
    Returns:
        tuple: (status_code, response_data)
    """
    url = f"{FRAPPE_BASE_URL}{endpoint}"
    headers = get_frappe_headers()
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, json=data)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            return 405, {'error': 'Method not allowed'}
        
        # Try to parse JSON response
        try:
            response_data = response.json()
        except ValueError:
            response_data = {'message': response.text}
        
        return response.status_code, response_data
    
    except requests.exceptions.ConnectionError:
        return 503, {'error': 'Cannot connect to Frappe server. Make sure it is running.'}
    except requests.exceptions.RequestException as e:
        return 500, {'error': f'Request failed: {str(e)}'}


def url_encode_doctype(doctype: str) -> str:
    """
    URL encode doctype name (handles spaces)
    Example: "Loan Category" -> "Loan%20Category"
    """
    return doctype.replace(' ', '%20')

