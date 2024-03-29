import os
import smtplib
from email.message import EmailMessage
import imghdr 
EMAIL_ADDRESS =  os.environ.get('EMAIL_USER')
EMAIL_PASSWORD =  os.environ.get('EMAIL_PASS')


def test_email():
        
    contacts = ['lakshaynew@gmail.com']
    msg = EmailMessage()
    msg['From'] = 'lakshaynew@gmail.com'
    msg['To'] = contacts
    msg['Subject'] = 'Test Email from python code'
    msg.set_content('hello! how are you ? this message was sent using the python code - you will see this if you ha ve html disabled :(')

    html = '<h1>Hello, html email from python by lakshay</h1>'
    msg.add_alternative(html,subtype ='html')

    files = ["instaLS\default.png"]
    for file in files:
        with open(file ,'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)

def print_email():
    print('email sent')
def like_email():
        
    contacts = ['lakshaynew@gmail.com']
    msg = EmailMessage()
    msg['From'] = 'lakshaynew@gmail.com'
    msg['To'] = contacts
    msg['Subject'] = 'someone pressed the like button on a post, this message was sent using the python code'
    msg.set_content('someone pressed the like button on a post hello! how are you ? this message was sent using the python code - you will see this if you ha ve html disabled :(')

    html = '<h1>someone pressed the like button on a post Hello, html email from python by lakshay</h1>'
    msg.add_alternative(html,subtype ='html')

    files = ["instaLS\default.png"]
    for file in files:
        with open(file ,'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)



def send_email(email,username,message,subject):   
    contacts = [email]
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg['Subject'] = subject
    msg.set_content(message)

    html = f"""<h1>Welcome</h1>
    <p>Dear,{username}!</p>
    <p>{message}</p>
    
    <a href='http://127.0.0.1:8000/login/'>Login here</a>"""
    msg.add_alternative(html,subtype ='html')

    files = []
    for file in files:
        with open(file ,'rb') as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg)
