import cv2
import numpy as np

def parse_yolo_data_from_file(file_path):
    parsed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line_data = line.split()
            class_id = int(line_data[0])
            points = [(float(line_data[i]), float(line_data[i+1])) for i in range(1, len(line_data[1:]), 2)]
            parsed_data.append((class_id, points))
    return parsed_data

def calculate_euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

def find_closest_segment(segmented_data, ground_truth_point):
    min_distance = float('inf')
    closest_segment = None
    for class_id, points in segmented_data:
        for point in points:
            distance = calculate_euclidean_distance(point, ground_truth_point)
            if distance < min_distance:
                min_distance = distance
                closest_segment = (class_id, point)
    return closest_segment, min_distance

def get_image_dimensions(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    return width, height

def compare_yolo_data(segmented_data, ground_truth_data, image_path):
    image_width, image_height = get_image_dimensions(image_path)
    total_distance = 0
    total_pixel_deviation = 0
    for ground_truth_item in ground_truth_data:
        closest_segment, distance = find_closest_segment(segmented_data, ground_truth_item[1])
        print("Ground truth:", ground_truth_item)
        print("Closest segment:", closest_segment)
        print("Euclidean distance:", distance)
        pixel_deviation = distance * max(image_width, image_height)
        print("Pixel deviation:", pixel_deviation)
        total_distance += distance
        total_pixel_deviation += pixel_deviation
        print("-----------------------------")
    average_distance = total_distance / len(ground_truth_data)
    average_pixel_deviation = total_pixel_deviation / len(ground_truth_data)
    print("Average Euclidean distance:", average_distance)
    print("Average pixel deviation:", average_pixel_deviation)

# Example usage
image_path = ''  # Replace with your image path

segmented_yolo_file = ''
ground_truth_yolo_file = ''

segmented_data = parse_yolo_data_from_file(segmented_yolo_file)
ground_truth_data = parse_yolo_data_from_file(ground_truth_yolo_file)

compare_yolo_data(segmented_data, ground_truth_data, image_path)
