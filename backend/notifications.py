"""Author: Harshada Tupe"""
# Third party library imports
from twilio.rest import Client
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER = os.getenv("TWILIO_SEND_NUMBER")
RECEIVER = os.getenv("TWILIO_RECEIVE_NUMBER")

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_notification(url):
    current_datetime = datetime.now()
    formatted_current_datetime = current_datetime.strftime("%d/%m/%y %H:%M:%S")
    twilio_client.messages.create(
        body=f"Person motion detected @{formatted_current_datetime}: {url}",
        from_=SENDER,
        to=RECEIVER
    )
