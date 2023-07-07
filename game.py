import random
import smtplib
from email.mime.text import MIMEText

f = open('emails', 'r')
emails = [line.strip() for line in f.readlines()]
print(emails)

spy = random.choice(emails)
for email in emails:
    if email == spy:
        msg = MIMEText('SPY')
    else:
        msg = MIMEText('ZOO')
    msg['Subject'] = 'Game of Spy'
    msg['From'] = 'mahmudhera93@gmail.com'
    msg['To'] = email

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.sendmail('mahmudhera93@gmail.com', [email], msg.as_string())
    s.quit()
