import requests
import json
from db import is_valid_api_key

class Client:
    def __init__(self, auth_token):
        if not auth_token:
            raise ValueError("auth_token is required")
        self.auth_token = auth_token

    def send_email(self, template_name, to_address, data_mapping):
        if not is_valid_api_key(self.auth_token):
            return {"success": False, "message": "Invalid API key"}

        payload = {
            "auth_token": self.auth_token,
            "template_name": template_name,
            "email": to_address,
            "data_mapping": data_mapping
        }

        try:
            response = requests.post(
                "http://localhost:1650/v1/send-email",
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=5
            )
            return response.json()
        except Exception as e:
            return {"success": False, "message": f"Request failed: {str(e)}"}

    def send_event(self, event_name, customer_email, properties):
        if not is_valid_api_key(self.auth_token):
            return {"success": False, "message": "Invalid API key"}

        payload = {
            "auth_token": self.auth_token,
            "name": event_name,
            "email": customer_email,
            "properties": properties
        }

        try:
            response = requests.post(
                "http://localhost:1650/v1/send-event",
                headers={"Content-Type": "application/json"},
                data=json.dumps(payload),
                timeout=5
            )
            return response.json()
        except Exception as e:
            return {"success": False, "message": f"Request failed: {str(e)}"}
