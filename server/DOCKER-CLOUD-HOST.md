# Custom Frappe ERPNext with Lending Module - Docker Setup Guide

This guide walks you through setting up a custom Frappe ERPNext instance with the Lending module using Docker.

## Prerequisites

- A Linux server (Ubuntu/Debian recommended)
- Root or sudo access
- Basic knowledge of command line

## Video Reference

Tutorial: [https://youtu.be/hbSMiJTooJI?si=KkCgRl8eSss8C1rx](https://youtu.be/hbSMiJTooJI?si=KkCgRl8eSss8C1rx)

---

## Step 1: Install Docker

First, install Docker and Docker Compose on your system:

```bash
# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify installation
docker --version
docker compose version
```

---

## Step 2: Create Apps Configuration

Create a JSON file defining the apps to install:

```bash
# Create apps.json file
nano apps.json
```

Paste the following content:

```json
[
  {
    "url": "https://github.com/frappe/erpnext",
    "branch": "version-15"
  },
  {
    "url": "https://github.com/frappe/lending.git",
    "branch": "v1.5.0"
  }
]
```

Save and exit (Ctrl+X, then Y, then Enter).

---

## Step 3: Encode Apps Configuration

Convert the apps.json to base64 and export as environment variable:

```bash
export APPS_JSON_BASE64=$(base64 -w 0 ./apps.json)

# Verify the variable is set
echo $APPS_JSON_BASE64
```

---

## Step 4: Clone Frappe Docker Repository

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
```

---

## Step 5: Build Custom Docker Image

Build a custom Docker image with ERPNext and Lending module:

```bash
docker build \
  --build-arg=FRAPPE_PATH=https://github.com/frappe/frappe \
  --build-arg=FRAPPE_BRANCH=version-15 \
  --build-arg=PYTHON_VERSION=3.11.9 \
  --build-arg=NODE_VERSION=18.20.2 \
  --build-arg=APPS_JSON_BASE64=$APPS_JSON_BASE64 \
  --tag=frappe-custom \
  --file=images/custom/Containerfile .
```

This process may take 15-30 minutes depending on your internet speed and server resources.

Verify the image was created:

```bash
docker images | grep frappe-custom
```

---

## Step 6: Update Docker Compose Configuration

Modify the `pwd.yml` file to use your custom image:

```bash
sed -i "s|frappe/erpnext:v15.93.0|frappe-custom|g" pwd.yml
```

You can verify the change:

```bash
grep "image:" pwd.yml
```

---

## Step 7: Start the Services

Launch all containers using Docker Compose:

```bash
docker compose -f pwd.yml up -d
```

Wait for all services to start (this may take a few minutes).

Check running containers:

```bash
docker ps
```

---

## Step 8: Verify Installation

Test the API endpoint to ensure the system is running:

```bash
# Replace with your server IP
curl http://13.203.229.21:8080/api/method/ping
```

Expected response:
```json
{"message":"pong"}
```

---

## Step 9: Access Your Instance

Open your browser and navigate to:

```
http://YOUR_SERVER_IP:8080
```

Default credentials are typically:
- **Username:** Administrator
- **Password:** Check the logs or set during setup

---

## Step 10: Generate API Keys

1. Log in to your ERPNext instance
2. Navigate to: **User Menu → My Settings → API Access**
3. Click **Generate Keys**

Example API credentials:
```
API Key: 7aaf5b1c5c3228c
API Secret: 33fded50a7bb73e
```

**Important:** Keep these credentials secure!

---

## Step 11: Test API with Authentication

Test the API with your credentials:

```bash
curl -X GET "http://13.203.229.21:8080/api/method/frappe.client.get_list" \
  -d 'doctype=Module Def' \
  -d 'fields=["app_name"]' \
  -H "Authorization: token 7aaf5b1c5c3228c:33fded50a7bb73e"
```

This should return a list of installed modules including the Lending app.

---

## Managing Your Instance

### View Logs

```bash
# All services
docker compose -f pwd.yml logs -f

# Specific service
docker compose -f pwd.yml logs -f backend
```

### Stop Services

```bash
docker compose -f pwd.yml down
```

### Start Services

```bash
docker compose -f pwd.yml up -d
```

### Restart Services

```bash
docker compose -f pwd.yml restart
```

### Access Backend Container Shell

```bash
docker compose -f pwd.yml exec backend bash
```

---

## Troubleshooting

### Container Won't Start

Check logs for errors:
```bash
docker compose -f pwd.yml logs backend
```

### API Returns Errors

1. Verify services are running: `docker ps`
2. Check if the site is accessible: `curl http://YOUR_IP:8080`
3. Verify API credentials are correct

### Permission Issues

Ensure proper permissions on volumes:
```bash
sudo chown -R 1000:1000 ./volumes
```

### Port Already in Use

Change the port mapping in `pwd.yml`:
```yaml
ports:
  - "8080:8080"  # Change first 8080 to another port
```

---

## Accessing the Lending Module

Once logged in:

1. Go to **Desk → Lending**
2. You'll find doctypes like:
   - Loan Application
   - Loan
   - Loan Security
   - Loan Type
   - And more...

---

## Production Considerations

For production deployment, consider:

1. **Use HTTPS**: Set up SSL/TLS certificates
2. **Configure Backups**: Set up automated database backups
3. **Resource Limits**: Configure proper CPU and memory limits
4. **Monitoring**: Set up monitoring and alerting
5. **Security**: Change default passwords and secure API keys
6. **Domain Name**: Use a proper domain instead of IP

---

## Useful API Endpoints

### Get List of Doctypes

```bash
curl -X GET "http://YOUR_IP:8080/api/method/frappe.client.get_list" \
  -d 'doctype=DocType' \
  -H "Authorization: token API_KEY:API_SECRET"
```

### Get Loan Applications

```bash
curl -X GET "http://YOUR_IP:8080/api/method/frappe.client.get_list" \
  -d 'doctype=Loan Application' \
  -d 'fields=["name","applicant","loan_amount","status"]' \
  -H "Authorization: token API_KEY:API_SECRET"
```

### Create a New Document

```bash
curl -X POST "http://YOUR_IP:8080/api/resource/Loan Type" \
  -H "Authorization: token API_KEY:API_SECRET" \
  -H "Content-Type: application/json" \
  -d '{
    "loan_name": "Personal Loan",
    "maximum_loan_amount": 500000,
    "rate_of_interest": 10.5
  }'
```

---

## Resources

- **Frappe Documentation**: https://frappeframework.com/docs
- **ERPNext Documentation**: https://docs.erpnext.com
- **Lending Module**: https://github.com/frappe/lending
- **API Documentation**: https://frappeframework.com/docs/user/en/api

---

## Support

For issues and questions:
- Frappe Forum: https://discuss.frappe.io
- GitHub Issues: https://github.com/frappe/frappe_docker/issues

---

**Last Updated:** December 2025