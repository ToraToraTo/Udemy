"""
Emailの送信について
"""

from email import message
# smtpServerを使ってメールを送信する為のもの
import smtplib
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config_data = config['email']

smtp_host = 'smtp.gmail.com'
smtp_port = '587'

from_email = config_data['from_email']
to_email = config_data['to_email']
user_name = config_data['user_name']
password = config_data['password']

msg = message.EmailMessage()
msg.set_content('The python auto message')
msg['Subject'] = 'Python system message'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user_name, password)
server.send_message(msg)
server.quit()