import torch
import numpy as np
import plotly.graph_objects as go # visualize point clouds
from scipy.spatial.transform import Rotation as R

class Object3d(object):
    '''
    Represents a 3D object label.

    This class is used to encapsulate information about a 3D object, such as
    its dimensions, position, orientation, and bounding box.

    Attributes:
        w (float): The width of the 3D bounding box (in meters).
        l (float): The length of the 3D bounding box (in meters).
        h (float): The height of the 3D bounding box (in meters).
        t (tuple): The center coordinates of the 3D bounding box as a tuple (x, y, z) (in meters).
        angle (float): The orientation angle of the object (in radiant).
        distance (float): The distance from the origin to the object's center.
        bbox (numpy.ndarray): An array containing the 3D bounding box coordinates.

    Methods:
        get_bbox(): Calculate and return the 3D bounding box points based on object
        dimensions, position, and orientation.

    Example usage:
        label_data = [x, y, z, length, width, height, angle]
        obj = Object3d(label_data)
        bbox = obj.get_bbox()
    '''
    
    def __init__(self, label):
        # Constructor for initializing an Object3d instance.
        # It takes a 'label' parameter, which is assumed to be a list
        # containing information about the 3D object label.

        # Extract and store the label, truncation, and occlusion information.
        
        # Extract 3D bounding box information from the label.
        # 'w' represents the box width.
        self.w = label[3]
        # 'l' represents the box length in meters.
        self.l = label[4]
        # 'h' represents the box height.
        self.h = label[5]
        # 't' represents the box center as a tuple of (x, y, z) coordinates.
        self.t = (label[0], label[1], label[2])
        # 'angle' represents the orientation angle of the object.
        self.angle = label[6]

        # Calculate the distance from the origin to the object's center.
        self.distance = np.sqrt(np.sum(np.square(self.t))) 
        
        # Calculate the 3D bounding box points and store them.
        self.bbox = self.get_bbox()
    
    def get_bbox(self):
        # A method to calculate and return the 3D bounding box points
        # for the object.

        # Convert the center and dimensions of the bounding box to NumPy arrays.
        center = np.array(self.t)
        dimension = np.array([self.l, self.w, self.h])

        # Adjust dimensions slightly to prevent issues.
        w = dimension[0] + 0.1
        l = dimension[1] + 0.1
        h = dimension[2] 

        # Define the eight corners of the bounding box in the local coordinate system.
        x_corners = [-w / 2, -w / 2, w / 2, w / 2, -w / 2, -w / 2, w / 2, w / 2]
        y_corners = [l / 2, -l / 2, -l / 2, l / 2, l / 2, -l / 2, -l / 2, l / 2]
        z_corners = [h / 2, h / 2, h / 2, -h / 2, -h / 2, -h / 2, -h / 2, h / 2]

        # Calculate the rotation matrix based on the object's orientation angle.
        rotation_matrix = R.from_euler("xyz", [0, 0, self.angle]).as_matrix()
        # Combine the corner coordinates and rotation to get the final bounding box.
        bbox = np.vstack([x_corners, y_corners, z_corners])
        bbox = np.dot(rotation_matrix, bbox)
        bbox = bbox + center[:, np.newaxis]

        # Transpose the bounding box points for ease of use.
        bbox = np.transpose(bbox)

        # Return the calculated 3D bounding box.
        return bbox

def make_objects(labels):
    '''
    Create a list of Object3d instances from a list of label data.

    This function takes a list of label data, where each label represents a 3D
    object, and creates a list of Object3d instances to encapsulate information
    about these objects.

    Args:
        labels (list): A list of label data, where each label is a list containing
            [x, y, z, length, width, height, angle] information about a 3D object.

    Returns:
        list: A list of Object3d instances, each representing a 3D object from the
            input label data.

    Example usage:
        label_data_list = [[x1, y1, z1, length1, width1, height1, angle1],
                           [x2, y2, z2, length2, width2, height2, angle2]]
        objects = make_objects(label_data_list)
    '''
    objects = []
    for label in labels:
        objects += [Object3d(label)]
    return objects

def visualize_data(data_list, color_list=["green"], size_list=[1]):
    '''
    Create a list of 3D scatter plot objects for data visualization.

    This function takes a list of data arrays and generates a list of 3D scatter
    plot objects using Plotly. Each data array represents 3D points, and the
    corresponding color and size can be customized.

    Args:
        data_list (list of numpy.ndarray): A list of data arrays, where each array
            contains 3D points as rows, e.g., [[x1, y1, z1], [x2, y2, z2], ...].
        color_list (list, optional): A list of color values for each data array.
            Defaults to ["green"].
        size_list (list, optional): A list of size values for each data array.
            Defaults to [1].

    Returns:
        list: A list of 3D scatter plot objects that can be used for visualization.

    Example usage:
        data_list = [numpy.array([[x1, y1, z1], [x2, y2, z2]]),
                     numpy.array([[x3, y3, z3], [x4, y4, z4]])]
        color_list = ["blue", "red"]
        size_list = [2, 2]
        scatter_plots = visualize_data(data_list, color_list, size)
    '''

    # Initialize an empty list to store the scatter plot objects.
    go_vis_list = []

    # Iterate through data arrays and corresponding colors.
    for data, color, size in zip(data_list, color_list, size_list):
        data = np.array(data)
        # Create a 3D scatter plot object using Plotly.
        scatter_plot = go.Scatter3d(
            x=data[:, 0],
            y=data[:, 1],
            z=data[:, 2],
            mode='markers',
            type='scatter3d',
            marker={
                'size': size,
                'color': color,
                'colorscale': 'rainbow',
            }
        )

        # Add the scatter plot object to the list.
        go_vis_list.append(scatter_plot)

    # Return the list of scatter plot objects for visualization.
    return go_vis_list


# Define the layout for the 3D plot with a square aspect ratio.
# This layout configuration sets the initial view ranges for the x, y, and z axes
# of the 3D scene to maintain a square aspect ratio.
layout = go.Layout(
    scene={
        'xaxis': {'range': [-25, 25]},  # Set the x-axis range from -25 to 25.
        'yaxis': {'range': [-25, 25]},  # Set the y-axis range from -25 to 25.
        'zaxis': {'range': [-25, 25]},  # Set the z-axis range from -25 to 25.
        'aspectmode': 'cube'            # Maintain a square aspect ratio.
    }
)

if __name__ == "__main__":
    # Where is the dataset saved
    root = "../"

    root_Parking = f"{root}/ParkingSlot/csv/RecordingParkingSlot/"
    dir_blickfeld = f"{root_Parking}/blickfeld/"
    dir_velodyne = f"{root_Parking}/velodyne/"
    dir_radar = f"{root_Parking}/radar/"
    dir_labels = f"{root_Parking}/labels/"

    i = 0 # Index between 0 and 999
    blickfeld_data = np.loadtxt(f"{dir_blickfeld}/{i:06d}.csv")
    velodyne_data = np.loadtxt(f"{dir_velodyne}/{i:06d}.csv")
    radar_data = np.loadtxt(f"{dir_radar}/{i:06d}.csv")
    label_data = np.loadtxt(f"{dir_labels}/{i:06d}.csv")

    objects = make_objects(label_data)

    go_data = visualize_data([velodyne_data] + [obj.bbox for obj in objects], [velodyne_data[:,3]] + ["red"]*13, [2] + [4]*13)

    fig = go.Figure(data=go_data, layout = layout)
    fig.show()
