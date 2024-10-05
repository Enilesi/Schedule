import smtplib, ssl

import os
from dotenv import load_dotenv
load_dotenv()

class EmailSender:
    def __init__(self, smtp_server="smtp.gmail.com", port=587):
        self.smtp_server=smtp_server
        self.port=port
        self.context = ssl.create_default_context()
        self.load_credentials()

    def load_credentials(self):
        load_dotenv()
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.password = os.getenv('PASSWORD')
        self.receiver_email = os.getenv('RECEIVER_EMAIL')

    def create_headers(self):
        headers = "\r\n".join([
            "from: " + "noreply@gmail.com",
            "subject: " + "UPT Schedule changed!",
            "to: " + self.receiver_email,
            "mime-version: 1.0",
            "content-type: text/html"
        ])
        return headers
    
    def create_email_message(self, message):
        headers = self.create_headers()
        return headers + "\r\n\r\n" + message

    def send_email(self, message="Check your new schedule!"):
        content = self.create_email_message(message)
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls(context=self.context)
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, content)

if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.send_email()