import smtplib

# Configuration
port = 587 #for gmail 587 or 465
smtp_server = 'smtp.gmail.com' #for gmail smtp.gmail.com
login = ""  # Login to mail
password = ""  # Your password gto mail

#information
sender_email = "" #string
receiver_email = "" #string or list

print('1')

# Plain text content
text = """\
Subject:Topic


This is text"""

# Send the email
with smtplib.SMTP_SSL(smtp_server, port) as server:
  server.login(login, password)
  server.sendmail(sender_email, receiver_email, text)
  server.quit()
print('Sent', f'{text}\nTo: {receiver_email}')