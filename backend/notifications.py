"""Author: Harshada Tupe"""
# Third party library imports
from twilio.rest import Client
import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from email.message import EmailMessage


load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER = os.getenv("TWILIO_SEND_NUMBER")
RECEIVER = os.getenv("TWILIO_RECEIVE_NUMBER")
SENDER_GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
SENDER_GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
RECEIVER_GMAIL_ADDRESS = os.getenv("RECEIVER_GMAIL_ADDRESS")

twilio_client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_email_notifications(url):
    current_datetime = datetime.now()
    formatted_current_datetime = current_datetime.strftime("%d/%m/%y %H:%M:%S")
    body = f"Person motion detected @{formatted_current_datetime}: {url}"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = "Twilio Notification: Motion detected!"
    msg['to'] = RECEIVER_GMAIL_ADDRESS
    msg['from'] = SENDER_GMAIL_ADDRESS

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SENDER_GMAIL_ADDRESS, SENDER_GMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()


def send_notification(url):
    current_datetime = datetime.now()
    formatted_current_datetime = current_datetime.strftime("%d/%m/%y %H:%M:%S")
    send_email_notifications(url)

    # twilio_client.messages.create(
    #     body=f"Person motion detected @{formatted_current_datetime}: {url}",
    #     from_=SENDER,
    #     to=RECEIVER
    # )

# Third party library imports





