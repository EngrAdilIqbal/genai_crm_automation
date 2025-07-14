# tools/email_tools.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_EMAIL = "adiliqbal0317@gmail.com"
SMTP_APP_PASSWORD = "fytcdnenpwjbqrxm"

def send_email(recipient: str, subject: str, body: str):
    sender_email = SMTP_EMAIL
    password = SMTP_APP_PASSWORD

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, message.as_string())

    print(f"Sending email to: {recipient}\nSubject: {subject}\nBody:\n{body}")

    return {
        "status": "success",
        "message": f"Email sent to {recipient} with subject '{subject}'"
    }
