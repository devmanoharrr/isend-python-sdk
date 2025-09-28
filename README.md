changes

# iSend Python SDK

Official Python SDK for sending emails and events using the iSend API.

## Installation

You can install it via pip:

```bash
pip install isend-python-sdk

## Usage

from isend import iSend

# Initialize with your auth token
sdk = iSend("your_auth_token")

# Send an email
response = sdk.send_email("WelcomeEmail", "user@example.com", {"name": "John"})
print(response)

# Send an event
event_response = sdk.send_event("UserSignup", "user@example.com", {"property": "value"})
print(event_response)


<!-- Security scan triggered at 2025-09-02 04:51:27 -->

<!-- Security scan triggered at 2025-09-09 05:42:43 -->

<!-- Security scan triggered at 2025-09-28 15:50:41 -->