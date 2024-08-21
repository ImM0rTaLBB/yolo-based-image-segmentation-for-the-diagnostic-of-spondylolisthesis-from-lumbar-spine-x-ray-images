## Convert CSV File to YOLO Format for LA Lumbar Spine.

import os
import pandas as pd
import cv2

# Specify the folder paths
image_folder = ''  # Replace with the actual path to your image folder
csv_folder = ''  # Replace with the actual path to your CSV folder
yolo_format_output_folder = '' # Output folder for YOLO format data

# Create the output folder if it doesn't exist
os.makedirs(yolo_format_output_folder, exist_ok=True)

# Iterate through image files
for image_filename in os.listdir(image_folder):
    if image_filename.endswith(('.jpg', '.jpeg', '.png')):
        # Load the image to get its dimensions
        image_path = os.path.join(image_folder, image_filename)
        image = cv2.imread(image_path)
        height, width = image.shape[:2]

        # Corresponding CSV file
        csv_filename = os.path.splitext(image_filename)[0] + '.csv'
        csv_path = os.path.join(csv_folder, csv_filename)

        if os.path.exists(csv_path):
            # Read data from CSV file
            df = pd.read_csv(csv_path, header=None, usecols=[0, 1, 2, 3])

            # Initialize a list to hold YOLO formatted data
            yolo_data = []

                      # Iterate over the dataframe, two rows at a time
            for i in range(0, len(df), 2):
                # Check if this is the last row (i.e., index i + 1 is within bounds)
                if i + 1 < len(df):
                    # Define class index (L1 to L5 converted to 0 to 4)
                    class_index = i // 2

                    # Get coordinates and normalize them for the current and next row
                    row1 = [df.iloc[i, j] / width if j % 2 == 0 else df.iloc[i, j] / height for j in range(4)]
                    row2 = [df.iloc[i + 1, j] / width if j % 2 == 0 else df.iloc[i + 1, j] / height for j in range(4)]

                    # Swap items in row2 as requested
                    row2 = [row2[2], row2[3], row2[0], row2[1]]

                    normalized_coordinates = row1 + row2
                else:
                    # If this is the last row, set class_index to 5 (S1)
                    class_index = 5
                    # You can choose how to handle the coordinates for the last row
                    # For example, you can set row2 to be the same as row1 or skip it
                    row1 = [df.iloc[i, j] / width if j % 2 == 0 else df.iloc[i, j] / height for j in range(4)]
                    row2 = row1  # Setting row2 the same as row1 for the last row
                    normalized_coordinates = row1 + row2

                # Format the line as per YOLO requirements and append to yolo_data list
                yolo_line = f"{class_index} " + " ".join(map(str, normalized_coordinates))
                yolo_data.append(yolo_line)

            # Save to a new text file in YOLO format
            yolo_output_path = os.path.join(yolo_format_output_folder, os.path.splitext(image_filename)[0] + '.txt')
            with open(yolo_output_path, 'w') as file:
                for line in yolo_data:
                    file.write(line + '\n')
