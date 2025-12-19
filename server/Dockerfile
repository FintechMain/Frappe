FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PORT=5001
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 5001

# Run with Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5001", "app:app"]
