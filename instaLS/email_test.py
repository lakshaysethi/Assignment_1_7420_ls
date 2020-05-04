import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'pythondjangolakshay@gmail.com'
# os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = 'testing321'
# os.environ.get('EMAIL_PASS')

contacts = ['lakshaynew@gmail.com',]
msg = EmailMessage()
msg['From'] = 'lakshaynew@gmail.com'
msg['To'] = EMAIL_ADDRESS
msg['BCC'] = contacts
msg['Subject'] = 'Test Email from python code'
msg.set_content('hello! how are you ? this message was sent using the python code')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
