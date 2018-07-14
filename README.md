# detect_those_corners

This repo is the implementation of this blog post : 
The code implements Harris Corner Detector and Shi-Tomasi Corner Detector.

<br/>

<img src="https://github.com/nishagandhi/detect_those_corners/raw/master/output/sample_output.gif" width="400" height="400" />

<br/><br/>

## Requirements : 
OpenCV 3.4.1 <br/>
Python 3.6.5


## Sample command-line usage:

### For image/webcam/video (respectively)
```
python detect_corners.py --input_type=0
python detect_corners.py --input_type=1
python detect_corners.py --input_type=2
```
You can also give the image path, folder path using --img_path and --folder_path respectively.<br/> You can change the camera number using --camera. <br/> You can save the output by setting --save = True.

