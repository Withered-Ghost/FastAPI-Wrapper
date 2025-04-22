# Create Agent Wrapper API using FastAPI in Python

This API is a wrapper for two different API endpoints:

```http
POST https://api.vapi.ai/assistant

POST https://api.retellai.com/create-agent
```

## Tech Stack

**Code:** Python 3.11.9

**Web-Server:** FastAPI

## Installation

Install the source code with:

```bash
git clone https://github.com/Withered-Ghost/FastAPI-Wrapper.git
cd FastAPI-Wrapper
```

Activate the virtual environment:

For **Powershell**:
```bash
./.venv/Scripts/Activate.ps1
```

For **Unix**:
```bash
. ./.venv/Scripts/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run the server:
```bash
fastapi run main.py
```

Access the API at:

```http
http://<Host_IP>:8000/
```

To deactivate the virtual environment:
```bash
deactivate
```

## API Reference

This API accepts request payload only in JSON format.

Header: `Content-Type: application/json; charset=UTF-8`

Requests to endpoints marked as `Protected: YES` must also have the `Authorization` header.

Header: `Authorization: Bearer <token>`

#### Create agent

```http
POST /create
Protected: YES

Payload:
{
    "api": int,
    "body": {}
}
```

Please view the documentation for each create agent API for the required keys in `body`