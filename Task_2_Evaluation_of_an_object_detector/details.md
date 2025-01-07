## Project Details

### Introduction
This project evaluates a YOLO-based object detection system using BEV images from the KITTI dataset. It assesses the system's ability to accurately detect and classify objects by comparing ground truth labels with model predictions across 20 scenes.

### Methodology
1. **Data Loading:** Load BEV images and associated labels and predictions.
2. **Bounding Box Processing:** Convert labels and predictions to Shapely objects for geometric operations.
3. **IoU and Metric Calculation:**
   - IoU: Ratio of the intersection area to the union area of two bounding boxes.
   - Precision: Measures prediction accuracy.
   - Recall: Measures the model's completeness.
4. **Visualization:** Annotate BEV images with bounding boxes and metrics.

### Observations
- **Strong Performance:** Simple scenes with distinct objects (e.g., scenes 006037, 006042).
- **Challenges:** Complex scenes with overlapping or ambiguous objects (e.g., scenes 006048, 006206).
- **Metrics:** Precision and recall are reported for each scene, enabling targeted model improvements.

### Conclusion
The analysis highlights the model's strengths in clear environments and identifies challenges in crowded scenarios. This insight is pivotal for refining object detection algorithms.
