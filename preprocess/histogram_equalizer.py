# This file will enhance images by using histogram equalizer to brighten the dark area and darken the bright area by making it equally distributed.

import cv2
import os

def histogram_equalization(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Add more supported formats if needed
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            img_eq = cv2.equalizeHist(img)

            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_histeq{os.path.splitext(filename)[1]}")
            cv2.imwrite(output_path, img_eq)

            print(f"{filename} processed and saved as {os.path.basename(output_path)}")


input_folder = ""
output_folder = ""

histogram_equalization(input_folder, output_folder)
