import smtplib
import os
from email.message import EmailMessage
from email.utils import formataddr
from picamera2 import Picamera2, encoders
from picamera2.outputs import FfmpegOutput
import time
from PIL import Image, ImageChops, ImageStat
import os

def photo(app_password):
	picam2 = Picamera2()
	still = picam2.create_still_configuration()#(main={"size": (20, 20)})
	picam2.configure(still)	
	picam2.start()
	picam2.capture_file('rover.jpg')
	print('Photo taken')
	picam2.stop()
	picam2.close()

	msg = EmailMessage()
	msg['From'] = formataddr(('Samuel Malaj', 'malajsamuel287@gmail.com'))
	msg['To'] = 'malajsamuel287@gmail.com'
	msg['Subject'] = 'ROVER IMAGE'
	
	with open('rover.jpg', 'rb') as f1:
		f1_data = f1.read()
		msg.add_attachment(f1_data, maintype='image', subtype='JPEG', filename='rover.jpg')
	
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login('malajsamuel287@gmail.com', app_password)
		smtp.send_message(msg)

photo()
