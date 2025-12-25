# Hosting Guide for EC2 (Linux)

This guide details how to host the Loan Management API Gateway on an AWS EC2 Linux instance (Ubuntu recommended).

## Prerequisites

1.  **Launch an EC2 Instance**:
    *   **AMI**: Ubuntu Server 22.04 LTS (or Amazon Linux 2023).
    *   **Instance Type**: t2.micro or t3.micro (sufficient for low traffic).
    *   **Security Group**:
        *   Allow **SSH (22)** from your IP.
        *   Allow **Custom TCP (5001)** from Anywhere (0.0.0.0/0) - *If accessing directly*.
        *   Allow **HTTP (80)** and **HTTPS (443)** - *If using Nginx reverse proxy (Recommended)*.

2.  **Connect to your instance**:
    ```bash
    ssh -i "your-key.pem" ubuntu@your-ec2-public-ip
    ```

---

## Method 1: Using Docker (Easiest)

Since you already have a `Dockerfile`, this is the simplest way to get running.

1.  **Install Docker on EC2**:
    ```bash
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    # Install Docker
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

    # Add user to docker group (avoid sudo)
    sudo usermod -aG docker $USER
    newgrp docker
    ```

2.  **Upload your code**:
    You can use `git clone` if your repo is on GitHub, or `scp` to copy files from your local machine.
    ```bash
    # Example using SCP from your local machine
    scp -i "key.pem" -r ./Frappe/server ubuntu@your-ip:~/app
    ```

3.  **Build and Run**:
    Navigate to the directory and build the image.
    ```bash
    cd ~/app
    
    # Create your .env file
    nano .env
    # Paste your environment variables (FRAPPE_BASE_URL, etc.)
    
    # Build the image
    docker build -t loan-api .
    
    # Run the container (Background mode, mapping port 5001)
    docker run -d -p 5001:5001 --env-file .env --name loan-api-container loan-api
    ```

4.  **Verify**:
    Visit `http://your-ec2-public-ip:5001/health`

---

## Method 2: Manual Setup with Systemd (Production Standard)

This method runs the app as a background service and uses Nginx as a reverse proxy.

### 1. Install Python and Dependencies
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv nginx git
```

### 2. Setup Application
```bash
# Clone or copy your code to /var/www/loan-api or home directory
mkdir -p ~/loan-api
# (Copy your files here, e.g., via git clone or scp)

cd ~/loan-api

# Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install Requirements
pip install -r requirements.txt

# Create .env file
nano .env
# (Paste your environment variables here)
```

### 3. Create Systemd Service
This ensures your app restarts automatically if the server reboots or crashes.

Create file: `/etc/systemd/system/loan-api.service`
```bash
sudo nano /etc/systemd/system/loan-api.service
```

Paste the following (adjust paths if needed):
```ini
[Unit]
Description=Gunicorn instance to serve Loan API
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/loan-api
Environment="PATH=/home/ubuntu/loan-api/venv/bin"
EnvironmentFile=/home/ubuntu/loan-api/.env
ExecStart=/home/ubuntu/loan-api/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5001 app:app

[Install]
WantedBy=multi-user.target
```

**Start and Enable the Service:**
```bash
sudo systemctl start loan-api
sudo systemctl enable loan-api
sudo systemctl status loan-api
```

### 4. Configure Nginx (Reverse Proxy)
This allows you to access the app on port 80 (HTTP) instead of 5001.

Create config: `/etc/nginx/sites-available/loan-api`
```bash
sudo nano /etc/nginx/sites-available/loan-api
```

Paste:
```nginx
server {
    listen 80;
    server_name your-domain.com_or_public_ip;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

**Enable Site and Restart Nginx:**
```bash
sudo ln -s /etc/nginx/sites-available/loan-api /etc/nginx/sites-enabled
sudo rm /etc/nginx/sites-enabled/default  # Remove default if needed
sudo nginx -t
sudo systemctl restart nginx
```

Now your API is accessible at `http://your-ec2-public-ip/`.
