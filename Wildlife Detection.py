# clone YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5  # clone repo

!pip install -r yolov5/requirements.txt

from google.colab import drive
drive.mount('/content/drive')



!python3 /content/yolov5/train.py --img +++
540 --batch 16 --epochs 50 --data '/content/drive/MyDrive/wert/data.yaml' --weights yolov5s.pt --cache

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot 2024-05-01 034742.png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot 2024-05-01 035646.png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (41).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (42).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (43).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (44).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (45).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/Screenshot (46).png'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/content/drive/MyDrive/wert/test/images'

!python /content/yolov5/detect.py --weights 'best.pt' --img 540 --conf 0.3 --source '/chinkara .jpg'

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp/thom64_jpg.rf.31b84450a210571fcfe9b1215c9d7095.jpg'):
    display(Image(filename=imageName))
    print("\n")

import glob
from IPython.display import Image, display

for imageName in glob.glob('/chinkara .jpg'):
    display(Image(filename=imageName))
    print("\n")

import glob
from IPython.display import Image, display

for imageName in glob.glob('/Screenshot 2024-04-28 173603.png'):
    display(Image(filename=imageName))
    print("\n")

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/content/yolov5/runs/train/exp/weights/best.pt' --conf 0.3 --source '/content/vid1.mp4'

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/best.pt' --conf 0.3 --source '/content/campus.mp4'

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/best.pt' --conf 0.3 --source '/(15) IIT Jodhpur Campus Tour_Deer 🦌 Wildlife at IIT _Peacock and Deer_IIT Jodhpur vlogs💛 - YouTube and 13 more pages - Personal - Microsoft​ Edge 2024-04-30 16-29-07.mp4'

"""# New Section"""

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/best.pt' --conf 0.3 --source '/IIT Jodhpur Campus Tour_Deer 🦌 Wildlife at IIT _Peacock and Deer_IIT Jodhpur vlogs💛.mp4'

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/content/yolov5/runs/train/exp/weights/best.pt' --conf 0.3 --source '/content/vid2.mp4'

# Detect objects in a video
!python /content/yolov5/detect.py --weights '/content/yolov5/runs/train/exp/weights/best.pt' --conf 0.3 --source '/videoplayback.mp4'

"""# New Section"""

import glob
from IPython.display import Video

# Display the first video found in the detection directory
video_files = glob.glob('/content/yolov5/runs/detect/exp3/*.mp4')
if len(video_files) > 0:
    display(Video(video_files[0]))
