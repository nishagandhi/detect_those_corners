import cv2
import numpy as np


'''
Function : cv2.cornerHarris(image,blocksize,ksize,k)
Parameters are as follows :
1. image : the source image in which we wish to find the corners (grayscale)
2. blocksize : size of the neighborhood in which we compare the gradient
3. ksize : aperture parameter for the Sobel() Operator (used for finding Ix & Iy)
4. k : Harris detector free parameter (used in computing R)
'''

def harris_corners(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_img = np.float32(gray_img)

    #You can play with these parameters to get different outputs
    corners_img = cv2.cornerHarris(gray_img,3,3,0.04)

    image[corners_img>0.001*corners_img.max()] = [255,255,0]

    return image

'''
Function: cv2.goodFeaturesToTrack(image,maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])
image – Input 8-bit or floating-point 32-bit (grayscale image).
maxCorners – You can specify the maximum no. of corners to be detected. (Strongest ones are returned if detected more than max.)
qualityLevel – Minimum accepted quality of image corners.
minDistance – Minimum possible Euclidean distance between the returned corners.
corners – Output vector of detected corners.
mask – Optional region of interest. 
blockSize – Size of an average block for computing a derivative covariation matrix over each pixel neighborhood. 
useHarrisDetector – Set this to True if you want to use Harris Detector with this function.
k – Free parameter of the Harris detector (used in computing R)
'''


def shi_tomasi(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    #You can play with these parameters to get different outputs 
    corners_img = cv2.goodFeaturesToTrack(gray_img,1200,0.01,10)
    #corners_img = np.int0(corners_img)

    blank_img = np.zeros((image.shape[0],image.shape[1],3),np.uint8)

    for corners in corners_img:

        x,y = corners.ravel()
        cv2.circle(image,(x,y),3,[255,255,0],-1)
        cv2.circle(blank_img,(x,y),2,[255,255,0],-1)

    return image,blank_img

