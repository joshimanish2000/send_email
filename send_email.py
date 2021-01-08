#! /usr/bin/env python3
import os
import sys
from email.message import EmailMessage #Module to send emails
import mimetypes  #for encoding attachments
import smtplib    # to set a mail server up
import getpass   # to hide typing passwords

message = EmailMessage() #EmailMessage's object

sender = 'manishjoshicsj@gmail.com'
recipient = 'thehonchorko@gmail.com'

message['To'] = recipient
message['From'] = sender

message["Subject"] = "Greetings from {}".format(sender)

body = "Greetings {}.Here is a nice wallpaper for your desktop \n. This is a python generated email. Don't reply".format(recipient)

message.set_content(body) #set_content method adds the email body
#print(message)

attachment_path = sys.argv[1]
os.chdir(os.path.dirname(attachment_path))
print(attachment_path,os.getcwd())

mime_type, _ = mimetypes.guess_type(attachment_path) #To tell recipient's server how it should interpret our message (decode and all) mentioning mimetype is necessary.
print(mime_type)
mime_type, mime_subtype = mime_type.split("/",1) # mime_type contains type and subtype of the attachment, e.g. image/png

with open(attachment_path,'rb') as f:
  message.add_attachment(f.read(),maintype = mime_type , subtype = mime_subtype, filename = os.path.basename(attachment_path))
#print(message)

try:
  mail_server = smtplib.SMTP('localhost')
except:
  mail_server = smtplib.SMTP_SSL("smtp.gmail.com")
  mail_pass = getpass.getpass("pswd? ")
  mail_server.login(sender,mail_pass)



mail_server.send_message(message)
