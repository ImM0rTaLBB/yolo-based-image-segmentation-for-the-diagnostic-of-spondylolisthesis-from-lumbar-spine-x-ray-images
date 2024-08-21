# This file is for rename muktiple files.

import os
import shutil

# Define the folder containing the text files
input_folder = './datasets_LA_Augment/valid/labels'

# Define the folder to save the copied and renamed text files
output_folder = './datasets_LA_Augment/valid/labels'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through the input folder and process each text file
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):  # Adjust the file extension as needed
        # Generate the new filename with "" appended
        new_filename = os.path.splitext(filename)[0] + 'CHANGE NAME HERE'

        # Create the full paths for the input and output files
        input_filepath = os.path.join(input_folder, filename)
        output_filepath = os.path.join(output_folder, new_filename)

        # Copy and rename the text file
        shutil.copy2(input_filepath, output_filepath)

print("Text files copied and renamed successfully.")
