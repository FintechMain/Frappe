# Quick Start Guide - Loan Management API Gateway

## Prerequisites

1. **Python 3** installed on your system
2. **Frappe server** running on `http://127.0.0.1:8000`
3. Virtual environment already set up (in `venv/` folder)

## How to Run the Server

### Option 1: Using the Run Script (Easiest)

```bash
cd /Users/prom3/Desktop/regal/frappe-bench/server
./run.sh
```

### Option 2: Manual Steps

**Step 1:** Open Terminal and navigate to the server directory
```bash
cd /Users/prom3/Desktop/regal/frappe-bench/server
```

**Step 2:** Activate the virtual environment
```bash
source venv/bin/activate
```

**Step 3:** Run the server
```bash
python app.py
```

### Option 3: One-Line Command

```bash
cd /Users/prom3/Desktop/regal/frappe-bench/server && source venv/bin/activate && python app.py
```

## What You'll See When Server Starts

```
🚀 Starting Loan Management API Gateway on port 5001
📡 Registered modules: Loan Categories
 * Running on http://0.0.0.0:5001
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

## Verify Server is Running

Open a **new terminal window** and run:

```bash
curl http://localhost:5001/health
```

You should see:
```json
{"service":"Loan Management API Gateway","status":"healthy"}
```

## Server Configuration

The server runs on **port 5001** by default (port 5000 is used by macOS AirPlay).

### Change Port (Optional)

Set environment variable before running:
```bash
export PORT=8080
python app.py
```

### Change Frappe Settings (Optional)

```bash
export FRAPPE_BASE_URL=http://127.0.0.1:8000
export FRAPPE_SITE_NAME=lending.localhost
export FRAPPE_API_KEY=your_api_key
export FRAPPE_API_SECRET=your_api_secret
python app.py
```

## Stop the Server

Press `Ctrl + C` in the terminal where the server is running.

## Test the API

### Create a Loan Category
```bash
curl -X POST http://localhost:5001/api/loan-categories \
  -H "Content-Type: application/json" \
  -d '{
    "loan_category_code": "TEST-001",
    "loan_category_name": "Test Category",
    "disabled": 0
  }'
```

### Get All Categories
```bash
curl http://localhost:5001/api/loan-categories
```

### Get Specific Category
```bash
curl http://localhost:5001/api/loan-categories/TEST-001
```

### Update Category
```bash
curl -X PUT http://localhost:5001/api/loan-categories/TEST-001 \
  -H "Content-Type: application/json" \
  -d '{
    "loan_category_name": "Updated Name"
  }'
```

### Delete Category
```bash
curl -X DELETE http://localhost:5001/api/loan-categories/TEST-001
```

## Troubleshooting

### Port Already in Use
If port 5001 is busy, change it:
```bash
export PORT=5002
python app.py
```

### Cannot Connect to Frappe
Make sure your Frappe server is running:
```bash
# In your frappe-bench directory
bench start
```

### Module Not Found Error
Activate the virtual environment:
```bash
source venv/bin/activate
```

### Permission Denied on run.sh
Make it executable:
```bash
chmod +x run.sh
```

## Server Structure

```
server/
├── app.py                 # Main application (entry point)
├── loan_categories.py     # Loan Categories API module
├── requirements.txt       # Python dependencies
├── venv/                  # Virtual environment
├── run.sh                 # Quick run script
└── README.md              # Full documentation
```

## Next Steps

- Add more modules (e.g., `loan_applications.py`, `loans.py`)
- Customize API endpoints
- Add authentication/authorization
- Add logging and error handling

