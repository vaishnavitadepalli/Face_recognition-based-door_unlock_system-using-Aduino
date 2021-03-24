



import cv2
import face_recognition
from PIL import Image
import numpy as geek
import serial
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import random
import string
import easyimap


b= geek.load('geekfile1.npy')
l=[]
for i in b:
	l.append(i)

def randomString(stringLength=10):
		
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringLength))


def app(img):
	fromaddr = "navneethnarendra@gmail.com"
	toaddr = "vilconsnarendra@gmail.com"
	#toaddr1 = "sushanthmullangi123@gmail.com"
	msg = MIMEMultipart() 
	msg['From'] = fromaddr
	msg['To'] = toaddr 
	msg['Subject'] = "Someone's at the door"
	secret_code_open=randomString(5)
	secret_code_close=randomString(3)
	body = "reply this following code to open the door : " + secret_code_open + "\n" + "or if you dont wan't to open the door reply this code :" + secret_code_close
	msg.attach(MIMEText(body, 'plain')) 
	filename = img
	conc="/home/navneeth/special_topic/" + filename
	attachment = open(conc, "rb") 
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(fromaddr, "bmexggxmcjvlwanz") 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text) 
	#s.sendmail(fromaddr, toaddr1, text)
	s.quit() 
	ser.write(b'sent')
	time.sleep(1.25)	
	print('message sent to owner waiting to be approved')
	return secret_code_open,secret_code_close


def read_mail(img):
	c=0
	p,q=app(img)
	imapper = easyimap.connect('imap.gmail.com', 'navneethnarendra@gmail.com', 'bmexggxmcjvlwanz')
	while (c==0):
		for mail_id in imapper.listids(limit=1):

			mail = imapper.mail(mail_id)
				
			if (mail.title=="Re: Someone's at the door"):
					
				if mail.body[0:5]==p:
					

					ser.write(b'open')
					print('Please Enter...')
					time.sleep(10)
					
					c=1
					return 2
						
				elif mail.body[0:3]==q:
					print("no")
					ser.write(b'close')
					time.sleep(15)
					c=1
					return 2
					
				else:
					pass
def recognize(s,leap):
		


	unknown_picture = face_recognition.load_image_file(s)
	unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
		


	results = face_recognition.api.face_distance(leap,unknown_face_encoding)
	r=list(results)
	q=min(r)
		
	if q<=0.45:
		
		ser.write(b'open')
		
		im = Image.open(s)
		im.show()
		print("hello !!! How was your day ?")
		print("Please Enter...")
		
		time.sleep(15)
		return 1	
	else :
		
		im = Image.open(s)
		im.show()
		print('Wait for confirmation')
		#ser.write(b'sent')
		time.sleep(1.25)
		nav=read_mail(s)
		
		if nav==2:
			return 1
		
				
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img_counter = 0
cond=1
while(cond==1):
	cap = cv2.VideoCapture(2)
	ret, frame = cap.read()
	cap.release()
	if ret:	

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
				#flags = cv2.CV_HAAR_SCALE_IMAGE
		)

			
		if (len(faces)>0):
			

			ser.write(b'done')
			time.sleep(1.25)
			print('done')
			print("Found {0} faces".format(len(faces)))
			img_name = "opencv_frame_{}.png".format(img_counter)
			cv2.imwrite(img_name, frame)
				
			img_counter += 1
			
			try:
				qs=recognize(img_name,l)
				if qs==1:
					
					ser.write(b'done')
					time.sleep(1.25)
			except:
				pass
				
			


		
		


