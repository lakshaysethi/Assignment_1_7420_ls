import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'pythondjangolakshay@gmail.com'
EMAIL_PASSWORD = 'testing321'
contacts = ['lakshaynew@gmail.com', 'jiyoon90222@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'This is a Python test email'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)