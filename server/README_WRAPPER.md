# Frappe API Wrapper Configuration

This wrapper allows you to connect to any Frappe instance (Local or Cloud) by configuring the environment variables.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment:**
    The `.env` file contains all the necessary configuration.

    Open `.env` and update the following values:

    ```dotenv
    # Base URL of your Frappe instance
    FRAPPE_BASE_URL=https://your-site.frappe.cloud

    # The site name (important for cloud hosting)
    FRAPPE_SITE_NAME=your-site.frappe.cloud

    # API Key and Secret
    # Generate these in Frappe: User > API Access
    FRAPPE_API_KEY=your_api_key
    FRAPPE_API_SECRET=your_api_secret
    ```

## Cloud Hosting (e.g., Frappe Cloud)

If your Frappe instance is hosted on Frappe Cloud or another provider:

1.  **URL:** Set `FRAPPE_BASE_URL` to your public URL (e.g., `https://mysite.frappe.cloud`).
2.  **Site Name:** Set `FRAPPE_SITE_NAME` to the same domain (e.g., `mysite.frappe.cloud`). This is used for the `Host` header, which is required for the server to route the request to the correct site.
3.  **API Keys:** Ensure the user you generated keys for has the necessary permissions on the cloud instance.

## Running the Server

```bash
python app.py
```
