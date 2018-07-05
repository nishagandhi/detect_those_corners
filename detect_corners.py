import numpy as np
import cv2
import sys,getopt
import copy as cp
import matplotlib.pyplot as plt

   
def harris_corners(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_img = np.float32(gray_img)
    
    corners_img = cv2.cornerHarris(gray_img,3,3,0.04)

    image[corners_img>0.001*corners_img.max()] = [0,255,0]

    return image

def shi_tomasi(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    corners_img = cv2.goodFeaturesToTrack(gray_img,25,0.01,10)
    corners_img = np.int0(corners_img)
    
    for corners in corners_img:

        x,y = corners.ravel()
        cv2.circle(image,(x,y),3,[0,255,0],-1)

    return image

def main():
    
    cap = cv2.VideoCapture(0)
    
    while(True):

        ret,img = cap.read()
        cv2.imshow('Original Image',img)
    
        img1 = cp.copy(img)

        harris = harris_corners(img)
        shitomasi = shi_tomasi(img1)
        
        cv2.imshow('After detecting Harris corners',harris)
        cv2.imshow('After detecting Shi-Tomasi corners',shitomasi)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
