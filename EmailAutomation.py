import smtplib 
import ssl
from email.message import EmailMessage
EMAIL = "deepakdiya18@gmail.com"
APP_PASSWORD = "xxxxxx"
RECEIVER = "babagspeaking@gmail.com"
msg = EmailMessage()
msg ["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello From Python"
msg.set_content("This is send by the Python code.....")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465 , context=context) as server: 
    server.set_debuglevel(1)
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
print("Email Sent Successfully___")
