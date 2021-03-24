# Face-Recognition-Based-Door-Lock-System-

This project aims at combining automation and and security 
The idea behind is to provide security to homes without much effort spent by the owner of the house.
We have built a model which basically detects a face whenever a person is standing at the door. 
If the person is the owner or a permamnent resident of the house, the door lock opens automatically,
else an image is clicked and a mail is sent to the owner of the house asking for permission to open the door or not.
If he approves it the door opens else an appropriate message will be diplayed on the lcd screen placed infront of the door

Methodology

Face detetction and recognition

We have used Haar-cascade classifier algorithm for face detection.
The haar cascade xml file has been provided above which is a pre built file which contains all the feature vectors.
The face detection and recognition using haar cascade classifier algorithm is done with the help of open cv in python

We first run the program to find the feature vectors of a few images of the permanent residents of the house
and their feature vectors are stored into a .npy file,this is done by the program named initial_code.py. More the number of images more accurate the model will become.
Each time their is a visitor at the door the face is detetcted and its feature vectors are compared with the preobtained fearure vectors and if it returns tru the door will open automatically . Else the image of the person will be sent to the owner of the house to seek permission to open or not. If the owner approves the door will open automatically else if he denies an appropriate meggase will be displayed on the lcd display placed outside the door.

Lock opening system

In our model we have used a servo motor which behaves as a lock and rotates to open or close accordingly.
We have used an arduino uno to run the servo motor. The code for the arduino uno has been attached above with .ino extension.

Sending message to the owner

We have used gmail api access to send mails to the owner of the house which contains the image of the visitor.
In the program please note wherever you find ' your mail id' please replace by your mail id and for the 'password'
please note IT IS NOT YOUR GMAIL PASSWORD , it is the password obtained after allowing access to third party applications in your gamil settings and after completing the two step verification. 
Inorder to maintain security and privacy in our model the mail which contains the image will be two secret codes which are random ( which means each time a mail is sent the secret codes will be different and random ) one is to open the door and the other is  to deny acces for the person. The owner has to reply the same code inorder to do that particular function.

Pre requisites

Software

1)python
  modules under python
  a) cv2
  b) face_recognition
  c) numpy
  d) serial
  e) time
  f) smtplib
  g) email
  h) easyimap
  i) random
  j) string

2) arduino ide 1.8.9

Hardware

1) Arduino uno
2) Servo motor
3) lcd display
4) Bread board
5) connecting wires
6) webcam 


