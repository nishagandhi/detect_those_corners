# detect_those_corners

This repo is the implementation of this blog post : https://medium.com/pixel-wise/detect-those-corners-aba0f034078b
<br/><br/>
The code implements Harris Corner Detector and Shi-Tomasi Corner Detector. Detecting important corners in an image or a video is the most important and basic task in Computer Vision. It is important for applications such as panaroma creation (stitching of images together), object recognition, motion tracking etc. Read the above blog to know more about how corner detection works in practise.

<br/>

<img src="https://github.com/nishagandhi/detect_those_corners/raw/master/output/sample_output.gif" width="500" height="350" />

<br/><br/>

## Requirements : 
OpenCV 3.4.1 <br/>
Python 3.6.5


## Sample command-line usage:

### For image/webcam/video (respectively)
```
python detect_corners.py --input_type=0 --img_path=path/to/image.jpg
python detect_corners.py --input_type=1 --camera=0
python detect_corners.py --input_type=2 --folder_path=path/to/folder
```
You can save the output by setting --save=True.
