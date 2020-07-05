import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'xxxxxx@gmail.com'
email['subject'] = 'Send Through Python Code'

email.set_content('I am Python Master!')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('xxxxxx@gmail.com', 'password')
	smtp.send_message(email)
	print('all good boss')
