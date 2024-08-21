# This file will test out yolo predicted segmentation but draw a blue line of each class.

import cv2
import numpy as np

def plot_yolo_segments(image_path, yolo_data_path, output_path=None):
    # Load the image
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Read YOLO format data
    with open(yolo_data_path, 'r') as file:
        yolo_data = file.readlines()

    for line in yolo_data:
        # Parse YOLO format data
        line_data = line.split()
        class_id = int(line_data[0])
        points = [(float(line_data[i]), float(line_data[i+1])) for i in range(1, len(line_data[1:]), 2)]

        # Convert YOLO coordinates to pixel coordinates and create points list
        pts = [(int(x * width), int(y * height)) for x, y in points]

        # Draw polygon
        cv2.polylines(image, [np.array(pts)], isClosed=True, color=(255, 0, 0), thickness=2)

    # Save or display the image with segments
    if output_path is not None:
        cv2.imwrite(output_path, image)
    else:
        cv2.imshow('YOLO Segments', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage
image_path = ''
yolo_data_path = ''
output_image_path = ''

plot_yolo_segments(image_path, yolo_data_path, output_image_path)
