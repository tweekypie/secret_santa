import smtplib
import ssl
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "joedonal@gmail.com"

password = "password"

addr_to = ""
addr_from = sender_email


def send_mail(email,username):
    #sending process
    addr_to = email
    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header('Joe Donal', 'utf-8')), 'joedonal@gmail.com'))       #this part need to change sender in email app
    msg['To'] = addr_to
    msg['Subject'] = 'SECRET SANTA'                                                           #change this if you want
    body = "You were chosen as a secret Santa for: \n" + username                             #change this if you want
    msg.attach(MIMEText(body, 'plain'))

    message = msg.as_string()                                   #build email text
    reciever_email = email
    server = smtplib.SMTP(smtp_server, port)                    #set server settings
    server.starttls()                                           #start secret connection
    server.login(addr_from, password)                           #server autentification
    server.sendmail(sender_email, reciever_email, message)      #sending email
    server.quit()                                               #close server session
    print("MESSAGE SUCCESSFULLY SENT")                          #message sending status in console

def check(list1, list2):
    for i in range(len(list1)):
        if list1[i] == dict.get(list2[i]):
            trig = 0
            random.shuffle(list2)
            break
        else:
            trig = 1
    return trig

emails = []
users = []

with open("emails.txt", "r") as email:      #email_list.txt is list of emails with "\n" diveritive
    emails = email.read().splitlines()

with open("usernames.txt", "r") as user:    #username_list.txt is list of usernames with "\n" diveritive
    users = user.read().splitlines()

dict = dict(map(None, users, emails))           #create and consist dictionry of {username: email}
print(dict)

random.shuffle(emails)                          #shuffle lists
random.shuffle(users)

trigger = 0                                     #check of selfsending
while trigger == 0:
    trigger = check(emails, users)

print("SENDING PROCESS...")

for i in range(len(emails)):                    #send message loop
    print("\nSending message TO: " + emails[i]) #print status of script in console
    print(users[i])
    send_mail(emails[i],users[i])
