from twilio.rest import Client
import time

# Twilio API credentials
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
FAMILY_PHONE_NUMBER = "RECIPIENT_PHONE_NUMBER"

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_alert(message):
    """
    Send an SMS alert to the family.
    """
    twilio_client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=FAMILY_PHONE_NUMBER,
    )

# Detect consecutive distress signals
distress_count = 0
while True:
    detected_emotion = "sad"  # Replace with real-time emotion detection
    if detected_emotion in ["sad", "distress"]:
        distress_count += 1
    else:
        distress_count = 0

    if distress_count > 3:  # Trigger alert after 3 consecutive detections
        send_alert("Detected prolonged sadness/distress. Please check on your loved one.")
        distress_count = 0

    time.sleep(10)  # Check every 10 seconds
