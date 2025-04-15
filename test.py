from isend import ISend

API_KEY = "isend_9cfa50031be949ad0d59f041df45ec"

client = ISend(API_KEY)

email_response = client.send_email(
    template_name="WelcomeTemplate",
    to_address="testuser@example.com",
    data_mapping={"name": "Test User", "signup_date": "2025-04-15"}
)
print("Email Response:", email_response)