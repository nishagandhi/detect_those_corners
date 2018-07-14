# detect_those_corners

This repo is the implementation of this blog post : 
The code implements Harris Corner Detector and Shi-Tomasi Corner Detector.

[Alt Text](/output/gif)

## Requirements : 
OpenCV 3.4.1
Python 3.6.5


## Sample command-line usage:

### For image/webcam/video (respectively)
```
python detect_corners.py --input_type=0
python detect_corners.py --input_type=1
python detect_corners.py --input_type=2
```
You can also give the image path, folder path using --img_path and --folder_path respectively. You can change the camera number using --camera. You can save the output by setting --save = True.

