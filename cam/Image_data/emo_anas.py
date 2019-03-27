import numpy as np
np.random.seed(123)  # for reproducibility
from skimage import io as io
from skimage.io import imread_collection
from numpy import loadtxt
import time
import cv2
import imutils


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import os
import glob

path=os.listdir()

images = []
	
labels = []
for w in path:
	if w.endswith('.png'):
		images.append(io.imread(w))
	if w.endswith('.txt'):
	
		labels.append(loadtxt(w, comments="#", unpack=False))	


	
print("done appending data")

images = np.asarray(images)

print(len(images))

print(images.shape)

print(images.shape[0])

X_train = images.reshape(images.shape[0], 24, 32,3)
X_test = images.reshape(images.shape[0], 24, 32,3)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')



#exit()
X_train /= 255
X_test /= 255


Y_train = np_utils.to_categorical(labels, 8)
Y_test = np_utils.to_categorical(labels, 8)
#print(X_train)


model = Sequential()
 
'''model.add(Convolution2D(32, (3, 3), activation='relu',
    input_shape=(24,32,3)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, activation='softmax'))
'''
model.add(Convolution2D(32, (3, 3), padding = 'same', activation='relu',
    input_shape=(24,32,3)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
#model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, activation='softmax'))
  
# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
# Fit model on training data
model.fit(X_train, Y_train,
          batch_size=69, epochs=40, verbose=1)
 

def predic():

	# Evaluate model on test data
	im_ver = io.imread("/media/venkat/3DA9-17EC/ReactSense/cap.png")
	im_np = np.array(im_ver)
	test_img = im_np.reshape(1, 24, 32,3)

	img_class = model.predict_classes(test_img)
	prediction = img_class[0]
	class_name = img_class[0]
	#score = model.evaluate(X_test, Y_test, verbose=0)
	print(class_name)

	if(class_name==1):
		print("Anger")
	elif class_name == 2:
		print("Contempt")
	elif class_name == 3:
		print("Disgust")
	elif class_name == 4:
		print("Fear")
	elif class_name == 5:
		print("Happy")
	elif class_name == 6:
		print("Sad")
	elif class_name == 7:
		print("Surprise")

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #this file is available at repository
cap=cv2.VideoCapture(0)

while True:
	ret,img=cap.read()
	if ret==True:
		
		gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces=face_cascade.detectMultiScale(gray,1.3,5)
		if len(faces)>0:
			maxface=faces[0]
			for face in faces:
				if face[2]*face[3]>maxface[2]*maxface[3]:
					maxface=face
			(x,y,b,h)=maxface
			image = img[y-h:(y + (5*h)), x-b:(x + (b*2))]
			#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
			cv2.imshow('image' , image)
			img = imutils.resize(image, width=32)
			
			img = img[0:(0 + 24), 0:(0 + 32)]			
			

			cv2.imwrite("/media/venkat/3DA9-17EC/ReactSense/cap.png",img)
			
			
			predic()
			
			
			
		k=cv2.waitKey(30)&0xff
		if k==27:
			break
cap.release()
cv2.destroyAllWindows()

		

	





