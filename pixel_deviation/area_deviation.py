from shapely.geometry import Polygon
import numpy as np

def parse_yolo_line(line):
    """
    Parses a line from the YOLO format file.
    Expects a class identifier followed by pairs of x,y coordinates normalized.
    Returns the class id and a list of tuples representing the polygon vertices.
    """
    parts = line.strip().split()
    class_id = int(parts[0])
    vertices = [(float(parts[i]), float(parts[i+1])) for i in range(1, len(parts)-1, 2)]
    return class_id, vertices

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices.
    """
    polygon = Polygon(vertices)
    return polygon.area

def calculate_deviation_and_iou(gt_areas, seg_areas):
    """
    Calculates the area deviation and IoU for each class based on ground truth and segmented areas.
    Returns a dictionary with class ids as keys and a tuple of (deviation percentage, IoU) as values.
    """
    results = {}
    for class_id in gt_areas:
        # Calculate mean areas for simplification
        mean_gt_area = np.mean(gt_areas[class_id])
        mean_seg_area = np.mean(seg_areas[class_id]) if class_id in seg_areas else 0
        # Calculate deviation
        deviation = ((mean_seg_area - mean_gt_area) / mean_gt_area) * 100
        # Calculate IoU approximation
        intersection = min(mean_gt_area, mean_seg_area)  # Approximation: intersection is the smaller area
        union = max(mean_gt_area, mean_seg_area)  # Approximation: union is the larger area
        iou = (intersection / union) * 100
        results[class_id] = (deviation, iou)
    return results

# Load and process the ground truth and segmented files text file (predicted files from segmentation prediction)
ground_truth_file = ''
segmented_file = ''

with open(ground_truth_file, 'r') as file:
    ground_truth_content = file.readlines()

with open(segmented_file, 'r') as file:
    segmented_content = file.readlines()

# Parse and calculate areas for ground truth
ground_truth_areas = {}
for line in ground_truth_content:
    class_id, vertices = parse_yolo_line(line)
    area = calculate_polygon_area(vertices)
    if class_id not in ground_truth_areas:
        ground_truth_areas[class_id] = []
    ground_truth_areas[class_id].append(area)

# Parse and calculate areas for segmented
segmented_areas = {}
for line in segmented_content:
    class_id, vertices = parse_yolo_line(line)
    area = calculate_polygon_area(vertices)
    if class_id not in segmented_areas:
        segmented_areas[class_id] = []
    segmented_areas[class_id].append(area)

# Calculate deviations and IoU
deviation_and_iou_results = calculate_deviation_and_iou(ground_truth_areas, segmented_areas)

# Output results
for class_id, (deviation, iou) in deviation_and_iou_results.items():
    print(f"Class {class_id}: Deviation = {deviation:.2f}%, IoU = {iou:.2f}%")
