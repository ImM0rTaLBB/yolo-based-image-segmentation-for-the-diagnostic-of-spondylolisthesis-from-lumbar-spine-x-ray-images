# This file will using image processing to blur the image by radius of 5. This will create new set of images used for augmentation.

from PIL import Image, ImageFilter
import os

# Define the folder containing the images to blur
input_folder = ''

# Define the folder to save the blurred images
output_folder = ''

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Define the blur radius (adjust as needed)
blur_radius = 5

# Loop through the input folder and process each image
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust file extensions as needed
        # Open the image
        img = Image.open(os.path.join(input_folder, filename))

        # Apply Gaussian blur
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

        # Save the blurred image
        output_filename = os.path.splitext(filename)[0] + '_blurred.jpg'
        blurred_img.save(os.path.join(output_folder, output_filename))

        # Close the image
        img.close()
