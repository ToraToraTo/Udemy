from email import message
from email.mime import multipart
from email.mime import text
import smtplib

# 添付ファイル付きEmail

smtp_host = ''
smtp_port = ''
from_email = ''
to_email = ''
user_name = ''
passwrod = ''

msg = multipart.MIMEMultipart()
msg.attach(text.MIMEText('Test text', 'plain'))
with open('udemy_61.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='udemy_61'
    )
    msg.attach(attachment)

msg['Subject'] = ''
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user_name, passwrod)
server.send_message(msg)
server.quit()

