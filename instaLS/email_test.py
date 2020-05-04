import os
import smtplib


EMAIL_ADDRESS = 'pythondjangolakshay@gmail.com'
# os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = 'testing321'
# os.environ.get('EMAIL_PASS')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'test email from python'
    body = 'test email BODY from python'

    msg = f'Subject: {subject}\n\n{body}'

    
    smtp.sendmail(EMAIL_ADDRESS,'lakshaynew@gmail.com',msg)
