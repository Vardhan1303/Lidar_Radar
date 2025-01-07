# ComplexYOLO

**ComplexYOLO** is an advanced object detection system based on the Complex YOLO architecture. It combines the strengths of YOLO (You Only Look Once) with complex-valued neural networks to achieve state-of-the-art object detection performance.

## KITTI Subset File Structure

KITTI
├── bev
│ ├── 006037.png
│ ├── 006037.png
│ └── ...
├── images
│ ├── 006037.png
│ ├── 006037.png
│ └── ...
├── labels
│ ├── 006037.png
│ ├── 006037.png
│ └── ...
└── predictions
  ├── 006037.png
  ├── 006037.png
  └── ...
  
bev - contains the Bird's eye view images
images - contains the camera images
labels - contains the ground truth labels
                class - The class id of the ground truth object (1 - 'Car', 2 - 'Pedestrian', 3 - 'Cyclist')
                (x,y) - Center Point
                (w,l) - Dimension
                (im,re) - Rotation in polar coordinates
predictions - contains the object list from ComplexYOLO
                (x,y) - Center Point
                (w,l) - Dimension
                (im,re) - Rotation in polar coordinates
                object_conf - The confidence that a recognized object actually exists.
                class_score - The confidence that the recognized object belongs to a certain class or category.
                class_pred - The predicted class id of the detected object. (1 - 'Car', 2 - 'Pedestrian', 3 - 'Cyclist')
                
## Evaluation
The trained network was evaluated @IoU>0.5 on a seperate evalaution split of 1414 frames from the KITTI Dataset. 
    >>>	 Class 0 (Car): precision = 0.8913, recall = 0.9803, AP = 0.9728, f1: 0.9337
	>>>	 Class 1 (Ped): precision = 0.5957, recall = 0.9259, AP = 0.7522, f1: 0.7250
	>>>	 Class 2 (Cyc): precision = 0.7213, recall = 0.9670, AP = 0.9157, f1: 0.8263

mAP: 0.8802573901477059

