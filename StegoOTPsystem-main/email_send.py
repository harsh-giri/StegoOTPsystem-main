import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formatdate
from email import encoders
from config import *

def send_an_email(client, image):
    toaddr = client    
    me = config["emailID"] 
    subject = "OTP from StegoOTPSystem"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "" 

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(image, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{image}"')
    msg.attach(part)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = config["emailID"], password = config["passwd"])
       s.sendmail(me, toaddr, msg.as_string())
       s.quit()
    except smtplib.SMTPException as error:
          print ("Error")

#send_an_email("sanyam.jain17102001@gmail.com", "submit.png")