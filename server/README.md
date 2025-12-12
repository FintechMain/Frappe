# Loan Management API Gateway

A comprehensive Python Flask server that acts as an API gateway for the Loan Management System, providing RESTful endpoints to interact with Frappe backend.

## Features

- ✅ **16 Complete API Modules** covering all loan management operations
- ✅ **Standard CRUD Operations** for all entities
- ✅ **Modular Architecture** - Easy to extend and maintain
- ✅ **Shared Utilities** - Common functions for all modules
- ✅ **Comprehensive Documentation** - Full API reference included

## Server Structure

```
server/
├── app.py                              # Main application entry point
├── utils.py                            # Shared utility functions
├── module_template.py                  # Template for creating new modules
│
├── loan_categories.py                  # Loan Categories API
├── loan_products.py                    # Loan Products API
├── loan_applications.py                # Loan Applications API
├── loans.py                            # Loans API
├── loan_restructures.py                # Loan Restructures API
├── loan_disbursements.py               # Loan Disbursements API
├── loan_security_deposits.py           # Loan Security Deposits API
├── loan_repayment_schedules.py         # Loan Repayment Schedules API
├── loan_interest_accruals.py           # Loan Interest Accruals API
├── loan_demands.py                     # Loan Demands API
├── loan_repayments.py                  # Loan Repayments API
├── process_loan_security_shortfall.py  # Process Loan Security Shortfall API
├── process_loan_interest_accrual.py    # Process Loan Interest Accrual API
├── process_loan_demand.py              # Process Loan Demand API
├── process_loan_classification.py      # Process Loan Classification API
├── users.py                            # Users API
│
├── requirements.txt                    # Python dependencies
├── run.sh                              # Quick run script
├── README.md                           # This file
├── QUICK_START.md                      # Quick start guide
└── API_DOCUMENTATION.md                # Complete API documentation
```

## Quick Start

### 1. Install Dependencies

```bash
cd server
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Server

**Option 1: Using the run script**
```bash
./run.sh
```

**Option 2: Manual**
```bash
source venv/bin/activate
python app.py
```

**Option 3: One-liner**
```bash
cd server && source venv/bin/activate && python app.py
```

### 3. Verify Server is Running

```bash
curl http://localhost:5001/health
```

## Configuration

### Environment Variables

You can configure the server using environment variables:

```bash
export FRAPPE_BASE_URL=http://127.0.0.1:8000
export FRAPPE_SITE_NAME=lending.localhost
export FRAPPE_API_KEY=your_api_key
export FRAPPE_API_SECRET=your_api_secret
export PORT=5001
export FLASK_DEBUG=True
```

### Default Values

- **Port:** 5001 (5000 is used by macOS AirPlay)
- **Frappe URL:** http://127.0.0.1:8000
- **Site Name:** lending.localhost
- **API Keys:** Configured from your existing setup

## API Modules

### Core Loan Management
1. **Loan Categories** - `/api/loan-categories`
2. **Loan Products** - `/api/loan-products`
3. **Loan Applications** - `/api/loan-applications`
4. **Loans** - `/api/loans`
5. **Loan Restructures** - `/api/loan-restructures`

### Loan Operations
6. **Loan Disbursements** - `/api/loan-disbursements`
7. **Loan Security Deposits** - `/api/loan-security-deposits`
8. **Loan Repayment Schedules** - `/api/loan-repayment-schedules`
9. **Loan Interest Accruals** - `/api/loan-interest-accruals`
10. **Loan Demands** - `/api/loan-demands`
11. **Loan Repayments** - `/api/loan-repayments`

### Loan Processes
12. **Process Loan Security Shortfall** - `/api/process-loan-security-shortfall`
13. **Process Loan Interest Accrual** - `/api/process-loan-interest-accrual`
14. **Process Loan Demand** - `/api/process-loan-demand`
15. **Process Loan Classification** - `/api/process-loan-classification`

### System
16. **Users** - `/api/users`

## API Endpoints Pattern

All modules follow the same RESTful pattern:

- **POST** `/api/{module-name}` - Create
- **GET** `/api/{module-name}` - List all
- **GET** `/api/{module-name}/<id>` - Get one
- **PUT** `/api/{module-name}/<id>` - Update
- **DELETE** `/api/{module-name}/<id>` - Delete

## Example Usage

### Create a Loan Category
```bash
curl -X POST http://localhost:5001/api/loan-categories \
  -H "Content-Type: application/json" \
  -d '{
    "loan_category_code": "PL-001",
    "loan_category_name": "Personal Loan",
    "disabled": 0
  }'
```

### Get All Loans
```bash
curl http://localhost:5001/api/loans
```

### Update a Loan Product
```bash
curl -X PUT http://localhost:5001/api/loan-products/PROD-001 \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Updated Product Name"
  }'
```

### Delete a Loan Application
```bash
curl -X DELETE http://localhost:5001/api/loan-applications/APP-001
```

## Query Parameters

All GET endpoints support query parameters:

- `fields` - Comma-separated list of fields to retrieve
- `filters` - JSON string of filters
- `limit_start` - Starting index for pagination
- `limit_page_length` - Number of records per page

**Example:**
```bash
curl "http://localhost:5001/api/loans?limit_page_length=10&limit_start=0"
```

## Adding New Modules

To add a new module:

1. Copy `module_template.py` to create your new module file
2. Update the doctype name and route prefix
3. Import and register the blueprint in `app.py`
4. Follow the same pattern as existing modules

## Troubleshooting

### Port Already in Use
Change the port:
```bash
export PORT=5002
python app.py
```

### Cannot Connect to Frappe
Make sure Frappe server is running:
```bash
# In frappe-bench directory
bench start
```

### Module Import Errors
Make sure you're in the server directory and virtual environment is activated:
```bash
cd server
source venv/bin/activate
```

## Documentation

- **Quick Start Guide:** See `QUICK_START.md`
- **Complete API Reference:** See `API_DOCUMENTATION.md`
- **Module Template:** See `module_template.py` for creating new modules

## Support

For issues or questions:
1. Check the documentation files
2. Verify Frappe server is running
3. Check server logs for error messages
4. Ensure all dependencies are installed

## License

This API Gateway is part of your Loan Management System.
