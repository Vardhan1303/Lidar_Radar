## Project Details: Influence of Fog on the Sensors

## Introduction

This project provides an in-depth analysis of the topic **Influence of Fog on the Sensors**, conducted as part of the Master's program in Mechatronics at the University of Applied Sciences Ravensburg-Weingarten. The project evaluates the performance of three different sensors under varying atmospheric conditions (clear and foggy).

---

### Sensors Used

1. **Blickfeld Cube (Lidar)**: A high-resolution sensor designed for precision and reliability.  
2. **Velodyne Puck (Lidar)**: A robust sensor commonly used in automotive applications.  
3. **MMWAVCAS-RF-EVM Radar**: A radar system capable of operating effectively in adverse weather conditions.

---

### Objectives

1. Analyze the effect of fog on sensor performance.  
2. Compare sensor behavior in clear and foggy scenarios.  
3. Visualize the differences using RMS histograms and fog condition photos.  

---

## Workflow

### Data Collection

Sensor data was collected for both clear and foggy conditions. Additionally, photographs of clear and foggy test conditions were captured to provide visual context. The raw data files were provided in CSV format and organized into respective directories for each sensor.

---

### Data Processing

1. **Merging** multiple CSV files for each sensor type.  
2. **Cleaning and preprocessing** data:  
   - Dropping irrelevant columns.  
   - Calculating RMS values.  
3. **Visualizing** the processed data as histograms to observe distributions under different conditions.  

---

### Analysis Methodology

#### Root Mean Square (RMS) Calculation

The RMS values were calculated for each row of data, representing the magnitude of the sensor readings:  

$$
\text{RMS} = \sqrt{\sum_{i=1}^{n} x_i^2}
$$

#### Visualization

Histograms were generated to observe the variation in data distribution for clear and foggy conditions. Images of the testing conditions were also captured to contextualize sensor performance.

---

## Results

### Sensor Histograms and Environmental Photos

#### **Blickfeld Cube (Lidar)**

**Clear and Foggy Conditions:**
<div style="display: flex; justify-content: space-around;">
  <img src="https://drive.google.com/file/d/1xhiEUqHokxLjKxtrraLYnqb8oKcj2mu1/view?usp=drive_link" alt="Blickfeld Clear Histogram" width="45%">
  <img src="https://drive.google.com/file/d/17p8pguaCtizcyMQy-c8tBYpd-qalAG_i/view?usp=drive_link" alt="Blickfeld Fog Histogram" width="45%">
</div>  

**Observation:**  
- **Clear Conditions**: Sharp peaks indicate high precision in detecting objects, with minimal scatter.  
- **Foggy Conditions**: Wider distribution due to scattering effects caused by fog, significantly affecting detection beyond 15 meters.  

#### **Velodyne Puck (Lidar)**

**Clear and Foggy Conditions:**
<div style="display: flex; justify-content: space-around;">
  <img src="https://drive.google.com/file/d/1FA76mXstreF4uOfHQZp8e3vFck_NxZ3Q/view?usp=drive_link" alt="Velodyne Clear Histogram" width="45%">
  <img src="https://drive.google.com/file/d/1GjTYCzYtwNNJwP9j9tDHgFkZNl_Fy6YG/view?usp=drive_link" alt="Velodyne Fog Histogram" width="45%">
</div>  

**Observation:**  
- **Clear Conditions**: Reliable detection up to 10 meters.  
- **Foggy Conditions**: Significant performance reduction beyond 5 meters, although near-field detection remains minimally impacted.  

#### **MMWAVCAS-RF-EVM Radar**

**Clear and Foggy Conditions:**
<div style="display: flex; justify-content: space-around;">
  <img src="https://drive.google.com/file/d/1A6-pIaxchyoeduwjUNb6ktYsj8UKYkTh/view?usp=drive_link" alt="Radar Clear Histogram" width="45%">
  <img src="https://drive.google.com/file/d/1iMsUrWLv931TROUXcNnj2FQncxyunn-R" alt="Radar Fog Histogram" width="45%">
</div>  

**Observation:**  
- **Clear Conditions**: Effective detection up to 30 meters with a narrow distribution.  
- **Foggy Conditions**: Slightly reduced accuracy beyond 20 meters but generally robust performance compared to Lidar.  

---


## Key Observations

1. **Lidar sensors** face significant challenges in fog, particularly beyond 15 meters.  
2. **Radar sensors** exhibit better performance in adverse weather but are still impacted at longer ranges.  
3. Environmental conditions and required detection ranges must guide sensor selection.  

---

## Conclusion

The analysis highlights the strengths and limitations of each sensor type under varying weather conditions.  
- **Lidar sensors**: Highly accurate in clear conditions but vulnerable to scattering in fog.  
- **Radar sensors**: More robust in fog but with lower resolution.  

This study underscores the need for tailored sensor systems in adverse environments.

---

## Recommendations

1. **Combined Systems**: Use both Lidar and Radar to leverage complementary strengths.  
2. **Fog Mitigation Research**: Develop advanced algorithms or hardware enhancements for better Lidar performance in fog.

---

## Acknowledgments

This project was supervised by **Prof. Dr. Stefan Elser**, University of Applied Sciences Ravensburg-Weingarten. The dataset, resources, and environmental photos were collected as part of the academic curriculum.
