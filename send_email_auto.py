# Modify from https://realpython.com/python-send-email/

import smtplib, ssl
import getpass
from email.mime.text import MIMEText

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'
content="""\
Test message
"""
subject="Sent from Python"

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = 'sender@email.com'
print("Type your password and press enter:")
password = getpass.getpass()

tolist =  ['receiver1@email.com', 'receiver2@email.com']

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    msg = MIMEText(content, text_subtype)
    msg['Subject'] = subject
    msg['From']   = sender_email # some SMTP servers will do this automatically, not all
    # msg['To'] = tolist
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, tolist, msg.as_string())
except Exception as e:
    # Print any error messages to stdout
    print('Error')
    print(e)
finally:
    server.quit() 
