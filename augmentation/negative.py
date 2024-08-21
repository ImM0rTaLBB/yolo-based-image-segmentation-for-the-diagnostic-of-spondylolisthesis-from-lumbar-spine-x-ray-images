# This file will using image processing to make the images colour inverted or make the images negative.
# This will create new set of images used for augmentation.

from PIL import Image
import os

def convert_to_negative_grayscale(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            input_path = os.path.join(input_folder, file)

            image = Image.open(input_path)
            grayscale_image = image.convert('L')

            negative_image = Image.eval(grayscale_image, lambda x: 255 - x)

            output_filename = os.path.splitext(file)[0] + "_negative" + os.path.splitext(file)[1]
            output_path = os.path.join(output_folder, output_filename)

            negative_image.save(output_path)
if __name__ == "__main__":
    input_folder = ""
    output_folder = ""

    convert_to_negative_grayscale(input_folder, output_folder)

    print("Conversion complete.")
