# Task 1: Influence of Fog on the Sensor

## Overview
This repository contains the implementation and analysis of the project **Influence of Fog on the Sensors** as part of the "Lidar and Radar Systems" course in the Master's program in Mechatronics at the University of Applied Sciences Ravensburg-Weingarten. The primary objective of the project is to evaluate the effect of foggy conditions on the performance of three sensors: Blickfeld Cube, Velodyne Puck, and MMWAVCAS-RF-EVM Radar.

## Authors
- **Vardhan Mistry**  & **Vishrut Kakadiya**
- **Guided by:** Prof. Dr. Stefan Elser  

## Project Structure
```
CBuilding/
├── bag/               # Contains raw bag files (if applicable)
├── csv/               # Contains original sensor data in CSV format
output_clear/           # Contains processed output for clear conditions
output_fog/             # Contains processed output for foggy conditions
details.md              # Comprehensive explanation of the project
HowTORWUDataset.py      # Script to preprocess and handle dataset
LICENSE                 # Licensing information for the repository
main.ipynb              # Main Jupyter Notebook for analysis
README.md               # Project description and setup instructions
```
**Note:** The `CBuilding/` directory, including the `output_clear/`, `output_fog/`, and `HowTORWUDataset.py` file, has been removed from this repository due to the private nature of the dataset.

## Dataset
The dataset used in this project consists of sensor data for two scenarios: clear and foggy conditions. Each sensor recorded more than 500 CSV files per scenario. After merging and preprocessing, the dataset size increased significantly. These processed outputs are generated in respective folders (`output_clear/` and `output_fog/`) after running the code.

The dataset was captured using the following sensors:

1. **Blickfeld Cube**: Lidar sensor
2. **Velodyne Puck**: Lidar sensor
3. **MMWAVCAS-RF-EVM Radar**: Radar sensor

### Reference and Usage
The dataset was collected as part of an academic project under Prof. Dr. Stefan Elser's supervision. All rights to the dataset are reserved, and it is provided for academic use only. Proper attribution must be given to the authors and the University of Applied Sciences Ravensburg-Weingarten if reused. Any misuse or redistribution of the dataset without permission is strictly prohibited.

## Implementation Details
### Key Functions:
- **`calculate_rms()`**: Computes the Root Mean Square (RMS) values for sensor data and visualizes the distribution using histograms.
- **`process_scenario()`**: Automates the merging of sensor data files, processing, and plotting for each condition (clear/fog).

### Analysis:
The project involves generating histograms to compare sensor performance in clear and foggy conditions. Histograms are plotted for the RMS values to highlight variations in data distribution caused by fog.

#### Steps:
1. Merge CSV files for each sensor using `process_scenario`.
2. Process and clean the data by removing unnecessary columns.
3. Compute RMS values for each scenario and visualize the results.

## Results
1. **Blickfeld Cube**: Displays wider distribution in foggy conditions due to scattered reflections.
2. **Velodyne Puck**: Detects objects effectively up to 5 meters in fog but faces challenges beyond 10 meters.
3. **Radar Sensor**: Maintains robust detection but exhibits limitations in dense fog.

Detailed results and comparisons are included in the `details.md` file.

## Usage Instructions
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run `main.ipynb` in Jupyter Notebook to execute the analysis.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
**Disclaimer:** This repository is for academic purposes only, and all data belongs to the University of Applied Sciences Ravensburg-Weingarten. For permissions or inquiries, please contact Prof. Dr. Stefan Elser or the authors.


