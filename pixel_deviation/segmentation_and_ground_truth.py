# This file plot out both ground truth line and predicted segmentation line to compare how accurate the predicted line is to the ground truth in the image.
# Ground truth = Green Line
# Predicted Segmentation = Blue Line

import cv2
import numpy as np

def draw_bounding_boxes(image_path, segmented_yolo_file, ground_truth_yolo_file):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Draw segmented YOLO boxes in blue
    with open(segmented_yolo_file, 'r') as file:
        for line in file:
            # Parse YOLO format data
            line_data = line.split()
            class_id = int(line_data[0])
            points = [(float(line_data[i]), float(line_data[i+1])) for i in range(1, len(line_data[1:]), 2)]

            # Convert YOLO coordinates to pixel coordinates and create points list
            pts = [(int(x * width), int(y * height)) for x, y in points]

            # Draw polygon
            cv2.polylines(image, [np.array(pts)], isClosed=True, color=(255, 0, 0), thickness=2)

    # Draw ground truth YOLO boxes in green
    with open(ground_truth_yolo_file, 'r') as file:
        for line in file:
            # Parse YOLO format data
            line_data = line.split()
            class_id = int(line_data[0])
            points = [(float(line_data[i]), float(line_data[i+1])) for i in range(1, len(line_data[1:]), 2)]

            # Convert YOLO coordinates to pixel coordinates and create points list
            pts = [(int(x * width), int(y * height)) for x, y in points]

            # Draw polygon
            cv2.polylines(image, [np.array(pts)], isClosed=True, color=(0, 255, 0), thickness=2)

    return image

# Example usage
image_path = './Source/AP/0501-M-080Y0.jpg'  # Replace with your image path
output_image_path = './UseImage/output_image_with_segments_2.jpg'  # Path to save the output image
segmented_yolo_file = './results/AP_Vanilla/predict/labels/0501-M-080Y0.txt'
ground_truth_yolo_file = './Source/AP_YOLO/0501-M-080Y0.txt'

# Draw bounding boxes on the image
image_with_boxes = draw_bounding_boxes(image_path, segmented_yolo_file, ground_truth_yolo_file)

# Save the image as JPG
cv2.imwrite(output_image_path, image_with_boxes)

print(f"Image saved as {output_image_path}")
