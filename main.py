import cv2
import numpy as np
from colordetect import ColorDetect

def color_correction():
    img = cv2.imread('photos/scale.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #To get the lower range go to https://alloyui.com/examples/color-picker/hsv.html
    #To get the H value divide by 2 from the value on the website the S and V values stay as is

    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Red color bounds
    red_lower_rang = np.array([0,100,0])
    red_upper_range = np.array([17,255,255])

    #Orange color bounds
    orange_lower_rang = np.array([17, 100, 0])
    orange_upper_range = np.array([33, 255, 255])

    # Green color bounds
    green_lower_rang = np.array([33, 100, 0])
    green_upper_range = np.array([76, 255, 255])


    green_mask = cv2.inRange(hsv,green_lower_rang, green_upper_range)
    red_mask = cv2.inRange(hsv,red_lower_rang, red_upper_range)
    orange_mask = cv2.inRange(hsv,orange_lower_rang, orange_upper_range)

    not_red = cv2.bitwise_not(red_mask)

    #Combines the red color to the photo
    red = cv2.bitwise_and(img, img, mask=not_red)
    red[red_mask > 0] = [144,139,246]

    # Opacity settings
    alpha = 0.3
    beta = (1.0 - alpha)

    #changes opacity of the picture
    dst = cv2.addWeighted(img, alpha, red, beta, 0.0)


    #output = red
    cv2.imshow('Image', img)
    cv2.imshow('mask', dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def prompts():
    print("Select the form of color-blindness")
    print("a.)Red-Green")
   # val = input("Select an option")
    color_correction()

#prompts()

def colorDetection():
    my_car = ColorDetect('photos/blue shirt.jpg')
    monochromatic, gray, segmented, mask = my_car.get_segmented_image(lower_bound=(0, 70, 0), upper_bound=(80, 255, 255))
    cv2.imshow('Segmented', segmented)
    cv2.imshow('monochromatic', monochromatic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   # cv2.wait(0)

colorDetection()