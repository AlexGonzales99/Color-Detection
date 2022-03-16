import cv2
import numpy as np

img = cv2.imread('color.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


#To get the lower range go to https://alloyui.com/examples/color-picker/hsv.html
#To get the H value divide by 2 from the value on the website the S and V values stay as is

#Currently set to green
lower_rang = np.array([42,100,100])
upper_range = np.array([76,255,255])


mask = cv2.inRange(hsv,lower_rang, upper_range)

cv2.imshow('Image', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()