
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from secret import API_KEY

message = Mail(
    from_email='breuss.martin@gmail.com',
    to_emails='sadiemparker@gmail.com',
    subject='Hey Sarah',
    html_content='<strong>what is your email password again?</strong>')

try:
    sg = SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)