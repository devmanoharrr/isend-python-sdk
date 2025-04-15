from client import Client

class ISend:
    def __init__(self, auth_token):
        self.client = Client(auth_token)

    def send_email(self, template_name, to_address, data_mapping):
        return self.client.send_email(template_name, to_address, data_mapping)

    def send_event(self, event_name, customer_email, properties):
        return self.client.send_event(event_name, customer_email, properties)
