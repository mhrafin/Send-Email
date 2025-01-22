import os

from dotenv import load_dotenv

import send_email

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


sender = send_email.EmailSender(
    smtp_host="smtp.gmail.com",
    sender_email=email,
    sender_password=password,
)

sender.send_email("@gmail.com", subject="dhoincha kam korse?", email_body="Ho korse Niga!!!sdffdgssfdgfdgsgdfsgdfsfdgsfsgd")