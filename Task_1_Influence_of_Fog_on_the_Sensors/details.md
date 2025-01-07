## Project Details: Influence of Fog on the Sensors

## Introduction

This project provides an in-depth analysis of the topic **Influence of Fog on the Sensors**, conducted as part of the Master's program in Mechatronics at the University of Applied Sciences Ravensburg-Weingarten. The project evaluates the performance of three different sensors under varying atmospheric conditions (clear and foggy).

### Sensors Used

1. **Blickfeld Cube (Lidar)**: A high-resolution sensor designed for precision and reliability.
2. **Velodyne Puck (Lidar)**: A robust sensor commonly used in automotive applications.
3. **MMWAVCAS-RF-EVM Radar**: A radar system capable of operating effectively in adverse weather conditions.

### Objectives

1. Analyze the effect of fog on sensor performance.
2. Compare sensor behavior in clear and foggy scenarios.
3. Visualize the differences using RMS histograms.

## Workflow

### Data Collection

Sensor data was collected for both clear and foggy conditions. The raw data files were provided in CSV format and organized into respective directories for each sensor.

### Data Processing

1. Merging of multiple CSV files for each sensor type.
2. Cleaning and preprocessing of data:
   - Dropping irrelevant columns.
   - Calculating RMS values.
3. Visualizing the processed data as histograms to observe distributions under different conditions.

### Analysis Methodology

#### Root Mean Square (RMS) Calculation

The RMS values were calculated for each row of data, representing the magnitude of the sensor readings:

$$
\text{RMS} = \sqrt{\sum_{i=1}^{n} x_i^2}
$$

#### Visualization

Histograms were generated to observe the variation in data distribution for clear and foggy conditions.

### Flowchart

The procedural steps followed in the project are illustrated in the flowchart below:

```
Start
  |
  V
[Data Collection]
  |
  V
[Merge CSV Files]
  |
  V
[Data Preprocessing]
  |
  V
[Calculate RMS Values]
  |
  V
[Generate Histograms]
  |
  V
[Analyze Results]
  |
  V
End
```

### Results

#### 1. Blickfeld Cube
- **Clear Conditions**: Sharper peaks, indicating high precision.
- **Foggy Conditions**: Wider distribution due to scattered reflections, especially beyond 15 meters.

#### 2. Velodyne Puck
- **Clear Conditions**: Accurate detection up to 10 meters.
- **Foggy Conditions**: Reduced detection capability beyond 5 meters, with minimal difference observed up to 10 meters.

#### 3. MMWAVCAS-RF-EVM Radar
- **Clear Conditions**: Capable of detecting objects up to 30 meters.
- **Foggy Conditions**: Struggles with detection beyond 20 meters but generally less affected compared to Lidar sensors.

### Key Observations

1. Lidar sensors face significant challenges in fog, particularly beyond 15 meters.
2. Radar sensors exhibit better performance in adverse weather but are still impacted at certain ranges.
3. The choice of sensor should consider environmental conditions and desired detection range.

## Conclusion
The analysis highlights the limitations and advantages of each sensor type in clear and foggy conditions. Lidar sensors provide excellent accuracy in clear weather but struggle in foggy scenarios. Radar sensors are less affected by fog but may offer lower resolution. This project emphasizes the importance of selecting the right sensor for specific applications based on environmental constraints.

## Recommendations

1. **Combination of Sensors**: Using both Lidar and Radar for complementary strengths.
2. **Improved Fog Mitigation**: Research on algorithms or hardware modifications to enhance Lidar performance in foggy conditions.

## Acknowledgments

This project was supervised by **Prof. Dr. Stefan Elser**, University of Applied Sciences Ravensburg-Weingarten. The dataset and resources were provided as part of the academic curriculum.

## References

- [Blickfeld Cube Documentation](https://www.blickfeld.com/products/cube/)
- [Velodyne Puck Specifications](https://velodynelidar.com/products/puck/)
- [MMWAVCAS-RF-EVM Radar User Guide](https://www.ti.com/tool/MMWAVE-STUDIO)
- Academic guidelines provided by Prof. Dr. Stefan Elser