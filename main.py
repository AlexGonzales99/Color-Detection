import cv2
import numpy as np

#https://github.com/offsouza/color-segmentation.git
colorBlindness = 'red'
#To get the lower range go to https://alloyui.com/examples/color-picker/hsv.html
#To get the H value divide by 2 from the value on the website the S and V values stay as is


#prompts()
def red(blur, image):
    red_lower = np.array([0, 50, 100])
    red_upper = np.array([23, 255, 255])

    mask = cv2.inRange(blur, red_lower, red_upper)
    res = masking(blur, red_lower, red_upper, image)
    res[mask > 0] = [144,139,246] #pink color
    return res



def masking(blur, lower, upper, image):
    mask = cv2.inRange(blur, lower, upper)
    res = cv2.bitwise_and(image, image, mask=mask)
    return res


def colorDetection(colorBlindness):
    image = cv2.imread('photos/green.jpeg')

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blur = cv2.medianBlur(hsv, 11)

    if(colorBlindness == 'red'):
    #establishes color bounds for red
        result = red(blur, image)
       # result2 = green(blur, image)

        #need something here to adjust green
    elif(colorBlindness == 'blue'):
        print('nothing')
       
    # Opacity settings
    alpha = .3
    beta = (1.0 - alpha)

    #changes opacity of the picture
    filteredImage = cv2.addWeighted(result, alpha, image, beta, 0.0)


    cv2.imshow('img', image)

    #cv2.imshow('stack', np.hstack([image, res]))
    cv2.waitKey(0)

#img is the variable recieved from the flask project
colorDetection(colorBlindness)
