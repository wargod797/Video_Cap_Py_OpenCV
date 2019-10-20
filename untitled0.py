# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:19:06 2019

@author: sridhar
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('thumb-1920-127844.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#plt.plot(img)
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.plot([200][300],[300][800],'c',linewidth=50)
plt.show()

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
out.release()
cv2.destroyAllWindows()
