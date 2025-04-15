import requests
import json

class Client:
    def __init__(self, auth_token):
        if not auth_token:
            raise ValueError("auth_token is required")
        self.auth_token = auth_token

    def send_email(self, template_name, to_address, data_mapping):
        return self._send("https://api.isend.com/v1/sendEmail", {
            "auth_token": self.auth_token,
            "template_name": template_name,
            "email": to_address,
            "data_mapping": data_mapping
        })

    def send_event(self, event_name, customer_email, properties):
        return self._send("https://api.isend.com/v1/sendEvent", {
            "auth_token": self.auth_token,
            "name": event_name,
            "email": customer_email,
            "properties": properties
        })

    def _send(self, endpoint, data):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.post(endpoint, data=json.dumps(data), headers=headers)
        return response.json()
