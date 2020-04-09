from smtplib import SMTP
from email.message import EmailMessage

email = EmailMessage()

email["from"] = "test@gmail.com"
email["to"] = "test1@gmail.com"
email["subject"] = "You won 1 million dollars"
email.set_content("Hey user you won 1 million dollars")

with SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('test@gmail.com','test')
    smtp.ehlo()
    smtp.send_message(email)
    print("All works")
