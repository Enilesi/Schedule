import smtplib, ssl

import os
from dotenv import load_dotenv
load_dotenv()

smtp_server = "smtp.gmail.com"
port = 587
sender_email = os.getenv('SENDER_EMAIL')
password=os.getenv('PASSWORD')
receiver_email = os.getenv('RECEIVER_EMAIL')
message = "Check your new schedule! "


headers = "\r\n".join(["from: " + "noreply@gmail.com",
                               "subject: "+" UPT Schedule changed!",
                               "to: " + receiver_email,
                               "mime-version: 1.0",
                               "content-type: text/html"])

content = headers + "\r\n\r\n" + message

context = ssl.create_default_context()


with  smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, content)