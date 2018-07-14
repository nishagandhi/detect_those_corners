import numpy as np
import cv2
import sys
import copy as cp
import matplotlib.pyplot as plt
import argparse
import os
import random
from corners import harris_corners,shi_tomasi

#Checks if the path exists
def check_path(path):

    if not os.path.exists(path):
        print('ERROR! The given path does not exist.')
        sys.exit(0)

#Finds corners : harris and shitomasi
def find_corners(img):

    img_dup = cp.copy(img)
    img_dup1 = cp.copy(img)

    harris = harris_corners(img)
    shitomasi,silhouette = shi_tomasi(img_dup)
    
    #Display different corner detection methods side by side
    
    out1 = np.concatenate((harris,shitomasi),axis=1)
    out2 = np.concatenate((img_dup1,silhouette),axis=1)

    out3 = np.concatenate((out1,out2),axis=0)    
    #cv2.imshow('Left: Harris, Right: Shi-Tomasi',out1)
    #cv2.imshow('Important points',out2)
    cv2.imshow('Corners',out3)
    return harris,shitomasi,silhouette,out3

def main():

    if len(sys.argv) < 2:
        print('ERROR: Please check  https://github.com/nishagandhi/detect_those_corners for sample usage of this script or run : python detect_corners.py --help')
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_type',default=2,required=True,type=int,help='Specify input type : 0-Image, 1-Webcam, 2-Image Folder')
    parser.add_argument('--img_path',default='./images/eagle.jpeg',type=str,help='Specify image path (OPTIONAL)')
    parser.add_argument('--folder_path',default='./images/',type=str,help='Specify folder path (OPTIONAL)')
    parser.add_argument('--camera',default=0,type=int,help='Specify the camera you want to use (OPTIONAL)')
    parser.add_argument('--save',default=False,type=bool,help='Specify True for saving the output (OPTIONAL)')
    parser.add_argument('--output_path',default='output/',type=str,help='Specify output path if you want to save(OPTIONAL)')
    args = parser.parse_args()

    #Image
    if args.input_type==0:
        
        check_path(args.img_path)   
        img = cv2.imread(args.img_path)
        
        harris,shitomasi,silhoutte,out3 = find_corners(img)

        #Save the output
        if args.save==True:

            temp = str(random.randint(1,101))

            #Uncomment these to save all outputs
            '''
            cv2.imwrite(args.output_path+'Harris_'+temp+'.jpg',harris)
            cv2.imwrite(args.output_path+'shitomasi_'+temp+'.jpg',shitomasi)
            cv2.imwrite(args.output_path+'silhouette_'+temp+'.jpg',silhouette)
            '''
            cv2.imwrite(args.output_path+'corners'+temp+'.jpg',out3)
            

        cv2.waitKey(0)


    #Webcam
    elif args.input_type==1:
    
        cap = cv2.VideoCapture(args.camera)
        width = int(cap.get(3))
        height = int(cap.get(4)) 
        temp = str(random.randint(1,101))
        writer1 = cv2.VideoWriter(args.output_path+'out_'+temp+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30,(width,height))
        writer2 = cv2.VideoWriter(args.output_path+'out_'+temp+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30,(width,height))
       
        while(True):

            ret,frame = cap.read()
            frame1 = cp.copy(frame)
            harris,shitomasi,silhouette,out3= find_corners(frame)

            if args.save==True:

                #To write out3, please provide proper height and width. You can add more writers.
                writer1.write(frame1)
                writer2.write(silhouette)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        cap.release()

    #Folder of images
    else:

        check_path(args.folder_path)

        for img in os.listdir(args.folder_path):

            img = cv2.imread(args.folder_path+img)
            harris,shitomasi,silhouette,out3 = find_corners(img)

            temp = str(random.randint(1,101))

            if args.save==True:

                #Uncomment these to save all outputs
                '''
                cv2.imwrite(args.output_path+'Harris_'+temp+'.jpg',harris)
                cv2.imwrite(args.output_path+'shitomasi_'+temp+'.jpg',shitomasi)
                cv2.imwrite(args.output_path+'silhouette_'+temp+'.jpg',silhouette)
                '''
                cv2.imwrite(args.output_path+'corners'+temp+'.jpg',out3)
                
                
            cv2.waitKey(0)



    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
