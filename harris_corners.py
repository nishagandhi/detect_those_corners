import numpy as np
import cv2
import sys,getopt
import copy as cp

def main():
    
    cap = cv2.VideoCapture(0)

    while(True):

        ret,img = cap.read()

        #img = cv2.imread('/home/nisha/Downloads/me.jpg')
        img1 = cp.copy(img)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,2,3,0.04)

        dst = cv2.dilate(dst,None)

        img[dst>0.001*dst.max()]=[0,255,0]

        cv2.imshow('Original',img1)
        cv2.imshow('Harris',img)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
