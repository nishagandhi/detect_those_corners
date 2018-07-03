import numpy as np
import cv2
import sys,getopt
import copy as cp

def harris_corners(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_img = np.float32(gray_img)
    
    corners_img = cv2.cornerHarris(gray_img,3,3,0.04)

    image[corners_img>0.001*corners_img.max()] = [0,255,0]

    return image

def main():
    
    cap = cv2.VideoCapture(0)

    while(True):

        ret,img = cap.read()
        cv2.imshow('Original Image',img)
        corners = harris_corners(img)
        cv2.imshow('After detecting Harris corners',corners)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
