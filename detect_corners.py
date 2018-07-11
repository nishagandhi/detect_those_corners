import numpy as np
import cv2
import sys
import copy as cp
import matplotlib.pyplot as plt
import argparse
import os
import random

def harris_corners(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_img = np.float32(gray_img)
    
    corners_img = cv2.cornerHarris(gray_img,3,3,0.04)

    image[corners_img>0.001*corners_img.max()] = [255,255,0]

    return image

def shi_tomasi(image):

    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    corners_img = cv2.goodFeaturesToTrack(gray_img,2000,0.01,10)
    corners_img = np.int0(corners_img)
    
    blank_img = np.zeros((image.shape[0],image.shape[1],3),np.uint8)

    for corners in corners_img:

        x,y = corners.ravel()
        cv2.circle(image,(x,y),3,[255,255,0],-1)
        cv2.circle(blank_img,(x,y),2,[255,255,0],-1)

    return image,blank_img

def main():

    if len(sys.argv) < 2:
        print('ERROR: Please check  https://github.com/nishagandhi/detect_those_corners for sample usage of this script or run : python detect_corners.py --help')
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_type',default=2,required=True,type=int,help='Specify input type : 0-Image, 1-Video, 2-Webcam, 3-Image Folder')
    parser.add_argument('--img_path',default='images/test.jpg',type=str,help='Specify image path (OPTIONAL)')
    parser.add_argument('--vid_path',default='videos/test.avi',type=str,help='Specify video path (OPTIONAL)')
    parser.add_argument('--camera',default=0,type=int,help='Specify the camera you want to use (OPTIONAL)')
    parser.add_argument('--folder_path',default='images/',type=str,help='Specify folder path (OPTIONAL)')
    parser.add_argument('--output_path',default='output/',type=str,help='Specify output path (OPTIONAL)')
    args = parser.parse_args()

    if args.input_type==0:
        
        if not os.path.exists(args.img_path):
            print('ERROR: Please give correct image path!')
            sys.exit(0)

        image = cv2.imread(args.img_path)
        image_dup = cp.copy(image)
        image_dup1 = cp.copy(image)

        harris_img = harris_corners(image)
        shitomasi_img,blank_img = shi_tomasi(image_dup)

        h_s = np.concatenate((harris_img,shitomasi_img),axis=1)
        concat = np.concatenate((image_dup1,blank_img),axis=1)

        cv2.imshow('Left: Harris, Right: Shi-Tomasi',h_s)
        cv2.imshow('Important points',concat)
        cv2.imwrite(args.output_path+'HarrisShiTomasi_'+str(random.randint(1,101))+'.jpg',h_s)
        cv2.imwrite(args.output_path+'Silhoutte_'+str(random.randint(1,101))+'.jpg',concat)
        cv2.waitKey(0)

    elif args.input_type==1:

        if not os.path.exists(args.vid_path):
            print('ERROR: Please give correct video path!')
            sys.exit(0)

        cap = cv2.VideoCapture(args.vid_path)

        while(cap.isOpened()):

            ret,frame = cap.read()
            frame_dup = cp.copy(image)

            harris_frame = harris_corners(frame)
            shitomasi_frame,blank_img = shi_tomasi(frame_dup)

            cv2.imshow('After detecting Harris corners',harris_frame)
            cv2.imshow('After detecting Shi-Tomasi corners',shitomasi_frame)
        cap.release()
    else:
    
        cap = cv2.VideoCapture(args.camera)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4)) 
        out = cv2.VideoWriter(args.output_path+'out_'+str(random.randint(1,101))+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (2160,800))
        while(True):

            ret,img = cap.read()
            cv2.imshow('Original Image',img)
    
            img1 = cp.copy(img)
            img2 = cp.copy(img)

            harris = harris_corners(img)
            shitomasi,blank_img = shi_tomasi(img1)
       
            h_s = np.concatenate((harris,shitomasi),axis=1)
            concat = np.concatenate((img2,blank_img),axis=1)
            cv2.imshow('Left: Harris, Right: Shi-Tomasi',h_s)
            cv2.imshow('Important points',concat)
            out.write(concat)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
