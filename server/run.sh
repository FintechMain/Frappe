#!/bin/bash
# Script to run the Loan Management API Gateway

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Run the server
python app.py

