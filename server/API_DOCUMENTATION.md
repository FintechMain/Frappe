# Loan Management API Gateway - Complete Documentation

## Overview

This API Gateway provides RESTful endpoints for all loan management operations in your Frappe-based loan management system. It acts as a proxy between external frontend applications and your Frappe backend.

## Base URL

```
http://localhost:5001
```

## Authentication

All requests are authenticated using Frappe API keys configured in the server. The authentication is handled automatically by the gateway.

## API Endpoints

### Health Check

**GET** `/health`

Check if the server is running and see all registered modules.

**Response:**
```json
{
  "status": "healthy",
  "service": "Loan Management API Gateway",
  "modules": [...]
}
```

---

## 1. Loan Categories

### Create Loan Category
**POST** `/api/loan-categories`

**Request Body:**
```json
{
  "loan_category_code": "PL-001",
  "loan_category_name": "Personal Loan",
  "disabled": 0
}
```

### Get All Loan Categories
**GET** `/api/loan-categories`

**Query Parameters:**
- `fields` - Comma-separated list of fields
- `filters` - JSON string of filters
- `limit_start` - Pagination start
- `limit_page_length` - Records per page

### Get Loan Category
**GET** `/api/loan-categories/<category_name>`

### Update Loan Category
**PUT** `/api/loan-categories/<category_name>`

### Delete Loan Category
**DELETE** `/api/loan-categories/<category_name>`

---

## 2. Loan Products

### Create Loan Product
**POST** `/api/loan-products`

### Get All Loan Products
**GET** `/api/loan-products`

### Get Loan Product
**GET** `/api/loan-products/<product_name>`

### Update Loan Product
**PUT** `/api/loan-products/<product_name>`

### Delete Loan Product
**DELETE** `/api/loan-products/<product_name>`

---

## 3. Loan Applications

### Create Loan Application
**POST** `/api/loan-applications`

### Get All Loan Applications
**GET** `/api/loan-applications`

### Get Loan Application
**GET** `/api/loan-applications/<app_name>`

### Update Loan Application
**PUT** `/api/loan-applications/<app_name>`

### Delete Loan Application
**DELETE** `/api/loan-applications/<app_name>`

---

## 4. Loans

### Create Loan
**POST** `/api/loans`

### Get All Loans
**GET** `/api/loans`

### Get Loan
**GET** `/api/loans/<loan_name>`

### Update Loan
**PUT** `/api/loans/<loan_name>`

### Delete Loan
**DELETE** `/api/loans/<loan_name>`

---

## 5. Loan Restructures

### Create Loan Restructure
**POST** `/api/loan-restructures`

### Get All Loan Restructures
**GET** `/api/loan-restructures`

### Get Loan Restructure
**GET** `/api/loan-restructures/<restructure_name>`

### Update Loan Restructure
**PUT** `/api/loan-restructures/<restructure_name>`

### Delete Loan Restructure
**DELETE** `/api/loan-restructures/<restructure_name>`

---

## 6. Loan Disbursements

### Create Loan Disbursement
**POST** `/api/loan-disbursements`

### Get All Loan Disbursements
**GET** `/api/loan-disbursements`

### Get Loan Disbursement
**GET** `/api/loan-disbursements/<disbursement_name>`

### Update Loan Disbursement
**PUT** `/api/loan-disbursements/<disbursement_name>`

### Delete Loan Disbursement
**DELETE** `/api/loan-disbursements/<disbursement_name>`

---

## 7. Loan Security Deposits

### Create Loan Security Deposit
**POST** `/api/loan-security-deposits`

### Get All Loan Security Deposits
**GET** `/api/loan-security-deposits`

### Get Loan Security Deposit
**GET** `/api/loan-security-deposits/<deposit_name>`

### Update Loan Security Deposit
**PUT** `/api/loan-security-deposits/<deposit_name>`

### Delete Loan Security Deposit
**DELETE** `/api/loan-security-deposits/<deposit_name>`

---

## 8. Loan Repayment Schedules

### Create Loan Repayment Schedule
**POST** `/api/loan-repayment-schedules`

### Get All Loan Repayment Schedules
**GET** `/api/loan-repayment-schedules`

### Get Loan Repayment Schedule
**GET** `/api/loan-repayment-schedules/<schedule_name>`

### Update Loan Repayment Schedule
**PUT** `/api/loan-repayment-schedules/<schedule_name>`

### Delete Loan Repayment Schedule
**DELETE** `/api/loan-repayment-schedules/<schedule_name>`

---

## 9. Loan Interest Accruals

### Create Loan Interest Accrual
**POST** `/api/loan-interest-accruals`

### Get All Loan Interest Accruals
**GET** `/api/loan-interest-accruals`

### Get Loan Interest Accrual
**GET** `/api/loan-interest-accruals/<accrual_name>`

### Update Loan Interest Accrual
**PUT** `/api/loan-interest-accruals/<accrual_name>`

### Delete Loan Interest Accrual
**DELETE** `/api/loan-interest-accruals/<accrual_name>`

---

## 10. Loan Demands

### Create Loan Demand
**POST** `/api/loan-demands`

### Get All Loan Demands
**GET** `/api/loan-demands`

### Get Loan Demand
**GET** `/api/loan-demands/<demand_name>`

### Update Loan Demand
**PUT** `/api/loan-demands/<demand_name>`

### Delete Loan Demand
**DELETE** `/api/loan-demands/<demand_name>`

---

## 11. Loan Repayments

### Create Loan Repayment
**POST** `/api/loan-repayments`

### Get All Loan Repayments
**GET** `/api/loan-repayments`

### Get Loan Repayment
**GET** `/api/loan-repayments/<repayment_name>`

### Update Loan Repayment
**PUT** `/api/loan-repayments/<repayment_name>`

### Delete Loan Repayment
**DELETE** `/api/loan-repayments/<repayment_name>`

---

## 12. Process Loan Security Shortfall

### Create Process Loan Security Shortfall
**POST** `/api/process-loan-security-shortfall`

### Get All Process Loan Security Shortfall
**GET** `/api/process-loan-security-shortfall`

### Get Process Loan Security Shortfall
**GET** `/api/process-loan-security-shortfall/<process_name>`

### Update Process Loan Security Shortfall
**PUT** `/api/process-loan-security-shortfall/<process_name>`

### Delete Process Loan Security Shortfall
**DELETE** `/api/process-loan-security-shortfall/<process_name>`

---

## 13. Process Loan Interest Accrual

### Create Process Loan Interest Accrual
**POST** `/api/process-loan-interest-accrual`

### Get All Process Loan Interest Accrual
**GET** `/api/process-loan-interest-accrual`

### Get Process Loan Interest Accrual
**GET** `/api/process-loan-interest-accrual/<process_name>`

### Update Process Loan Interest Accrual
**PUT** `/api/process-loan-interest-accrual/<process_name>`

### Delete Process Loan Interest Accrual
**DELETE** `/api/process-loan-interest-accrual/<process_name>`

---

## 14. Process Loan Demand

### Create Process Loan Demand
**POST** `/api/process-loan-demand`

### Get All Process Loan Demand
**GET** `/api/process-loan-demand`

### Get Process Loan Demand
**GET** `/api/process-loan-demand/<process_name>`

### Update Process Loan Demand
**PUT** `/api/process-loan-demand/<process_name>`

### Delete Process Loan Demand
**DELETE** `/api/process-loan-demand/<process_name>`

---

## 15. Process Loan Classification

### Create Process Loan Classification
**POST** `/api/process-loan-classification`

### Get All Process Loan Classification
**GET** `/api/process-loan-classification`

### Get Process Loan Classification
**GET** `/api/process-loan-classification/<process_name>`

### Update Process Loan Classification
**PUT** `/api/process-loan-classification/<process_name>`

### Delete Process Loan Classification
**DELETE** `/api/process-loan-classification/<process_name>`

---

## 16. Users

### Create User
**POST** `/api/users`

### Get All Users
**GET** `/api/users`

### Get User
**GET** `/api/users/<user_name>`

### Update User
**PUT** `/api/users/<user_name>`

### Delete User
**DELETE** `/api/users/<user_name>`

---

## Common Response Format

### Success Response
```json
{
  "data": {
    "name": "DOC-001",
    ...
  }
}
```

### Error Response
```json
{
  "error": "Error message",
  "exc_type": "ErrorType",
  "exc": "Detailed error information"
}
```

## Example cURL Commands

### Create Loan Category
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

### Update Loan Product
```bash
curl -X PUT http://localhost:5001/api/loan-products/PROD-001 \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Updated Product Name"
  }'
```

### Delete Loan Application
```bash
curl -X DELETE http://localhost:5001/api/loan-applications/APP-001
```

## Notes

- All endpoints follow RESTful conventions
- All endpoints support standard CRUD operations (Create, Read, Update, Delete)
- GET endpoints support query parameters for filtering and pagination
- All requests require `Content-Type: application/json` header for POST/PUT requests
- Document names in URLs are case-sensitive

