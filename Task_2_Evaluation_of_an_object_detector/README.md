# Task 2: Evaluation of an object detector

## Overview

This project, "Task 2: Evaluation of an Object Detector," focuses on assessing the performance of a YOLO-based object detection model using Bird's Eye View (BEV) images from the KITTI dataset. By leveraging Intersection over Union (IoU), Precision, and Recall metrics, the project provides a comprehensive evaluation of the model's ability to identify and classify objects accurately across diverse scenes. Visualized outputs further aid in analyzing strengths and areas of improvement in the object detection system.

## Authors
- **Vardhan Vinodbhai Mistry**  & **Vishrut Kakadiya** 
- **Guided by:** Prof. Dr. Stefan Elser  

## KITTI_Selection Repository

This repository contains a project focused on evaluating an object detection model applied to the KITTI dataset, specifically leveraging Bird's Eye View (BEV) images. The project calculates key performance metrics, such as Intersection over Union (IoU), Precision, and Recall, to analyze the model's performance across multiple scenes.

### Repository Structure

```
KITTI_Selection/
├── bev/                 # BEV images for each scene
├── images/              # Optional: Additional visualization images
├── labels/              # Ground truth labels in CSV format
├── predictions/         # Model predictions in CSV format
├── readme.md/           # Overview of the dataset
```

```
Output/              # Processed outputs with visualization
main.ipynb           # Main Python notebook for processing scenes
README.md            # Overview of the repository
details.md           # Detailed description of the project
LICENSE              # Licensing information
```

### Getting Started

1. **Setup Dependencies:**
   - Install Python (3.7 or later).
   - Required libraries: OpenCV, NumPy, Matplotlib, and Shapely. Install them using:
     ```bash
     pip install numpy opencv-python matplotlib shapely
     ```

2. **Dataset Structure:**
   - Ensure the following structure within `KITTI_Selection`:
     - `bev/`: Contains BEV images for scenes.
     - `labels/`: Ground truth labels as CSV files.
     - `predictions/`: Prediction CSV files. Missing predictions will default to empty.

3. **Run the Notebook:**
   - Use `main.ipynb` to process scenes. Outputs are saved in the `Output/` directory.

### Key Features

- **IoU Calculation:** Measures overlap between ground truth and predicted bounding boxes.
- **Precision & Recall:** Evaluates detection performance with visualized results.
- **Visualization:** Outputs BEV images annotated with bounding boxes and metrics.

### Results Summary

The model exhibits high accuracy in straightforward scenes but struggles in complex ones, highlighting areas for future improvement.

## Acknowledgments

I would like to express my gratitude to the following resources and individuals for their invaluable support and guidance during this project:

- **Prof. Dr. Stefan Elser** for his expert guidance and mentorship throughout the project.
- **KITTI Dataset Contributors:** This project uses the KITTI dataset, a widely recognized benchmark for computer vision research. All rights and credits for the dataset belong to its original creators.

This acknowledgment ensures respect for intellectual property and proper attribution to all contributors.

I would like to express my gratitude to the following resources and individuals for their invaluable support and guidance during this project:
