# This file will using image processing to darken the image with technique of powerlaw.
# This will create new set of images used for augmentation.

import cv2
import numpy as np
import os

def power_law_transform(image, gamma):
    image = image.astype(np.float32)

    transformed_image = np.power(image, gamma)

    transformed_image = (transformed_image / np.max(transformed_image)) * 255.0

    transformed_image = transformed_image.astype(np.uint8)

    return transformed_image

def process_images(input_folder, output_folder, gamma):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            result_image = power_law_transform(image, gamma)

            base_name, ext = os.path.splitext(filename)
            output_filename = base_name + "_powerlaw" + ext

            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, result_image)

if __name__ == "__main__":
    input_folder = ""
    output_folder = ""

    gamma = 4

    process_images(input_folder, output_folder, gamma)
