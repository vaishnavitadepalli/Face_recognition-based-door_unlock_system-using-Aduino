import face_recognition
import numpy as geek
picture1= face_recognition.load_image_file('img1.JPG')
face_encod1= face_recognition.face_encodings(picture1)[0]
#geek.save('geekfile.npy', face_encod)


picture2= face_recognition.load_image_file('img2.JPG')
face_encod2= face_recognition.face_encodings(picture2)[0]

picture3= face_recognition.load_image_file('img3.JPG')
face_encod3= face_recognition.face_encodings(picture3)[0]

picture4= face_recognition.load_image_file('img4.JPG')
face_encod4= face_recognition.face_encodings(picture4)[0]

picture5= face_recognition.load_image_file('img5.JPG')
face_encod5= face_recognition.face_encodings(picture5)[0]

picture6= face_recognition.load_image_file('img6.jpeg')
face_encod6= face_recognition.face_encodings(picture6)[0]

picture7= face_recognition.load_image_file('img7.jpeg')
face_encod7= face_recognition.face_encodings(picture7)[0]

picture8= face_recognition.load_image_file('img8.jpeg')
face_encod8= face_recognition.face_encodings(picture8)[0]

picture9= face_recognition.load_image_file('img9.jpeg')
face_encod9= face_recognition.face_encodings(picture9)[0]

picture10= face_recognition.load_image_file('img10.jpeg')
face_encod10= face_recognition.face_encodings(picture10)[0]

picture11= face_recognition.load_image_file('img11.jpeg')
face_encod11= face_recognition.face_encodings(picture11)[0]

picture12= face_recognition.load_image_file('img12.jpeg')
face_encod12= face_recognition.face_encodings(picture12)[0]

picture13= face_recognition.load_image_file('img13.jpeg')
face_encod13= face_recognition.face_encodings(picture13)[0]

geek.save('geekfile1.npy', (face_encod1,face_encod2,face_encod3,face_encod4,face_encod5,face_encod6,face_encod7,face_encod8,face_encod9,face_encod10,face_encod11,face_encod12,face_encod13))
