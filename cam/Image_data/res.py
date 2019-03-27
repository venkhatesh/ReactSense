import os
import imutils
import cv2
import numpy as np

l=os.listdir()
print(l)
for s in l:
	if s.endswith('.png'):
		print(s)
		img=cv2.imread(s)
		img2 = imutils.resize(img, width=32)
		cv2.imwrite(s,img2)

