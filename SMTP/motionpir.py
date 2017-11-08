import time
import serial
import smtplib

TO = 'shashanksharma.2015@vit.ac.in'
GMAIL_USER = 'ssharma0704@gmail.com'
GMAIL_PASS = 'monuqwer@11'

SUBJECT = '!Toll Gate!'
TEXT = 'Vehicle passed through VIT Gate..'
  
ser = serial.Serial('COM8', 9600)
def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    print(message)
    if message[0] == 'W' :
        send_email()
    time.sleep(0.5)
    # Download the Python helper library from twilio.com/docs/python/install
    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC0b32775b3bec47d20e0b46ca9ad006f7"
    auth_token  = "0be2e89d79f40420ea63584fc318a9a6"
    client = TwilioRestClient(account_sid, auth_token)
    sms = client.sms.messages.create(body="Toll Gate",
    to="+917871232434",
    from_="+12513016618")

    print sms.sid

