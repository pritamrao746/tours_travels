
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

def verification_mail(link,user):
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	
	ei=os.environ.get('EMAIL_USER')
	password=os.environ.get('EMAIL_PASSWORD')

	# print(ei,password)
	
	s.login(ei,password)
	msg = MIMEMultipart()
	# print(link,user.email,type(user.email ))
	msg['From'] = "mahipalkeizer@gmail.com"
	msg['To'] = user.email
	msg['Subject'] = "testing message from mahipal keizer"
	message ='Hi '+user.username + ' welcome to tours and trvel to \
	activate your account click link below\n'+link
	
	msg.attach(MIMEText(message, 'html'))
	s.send_message(msg)
	s.quit()



