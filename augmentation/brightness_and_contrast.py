# This file will using image processing to increase brightness and contrast the image by the factor of 1.5 and 1.2. 
# This will create new set of images used for augmentation.

from PIL import Image, ImageEnhance
import os

input_folder = ''
output_folder = ''

os.makedirs(output_folder, exist_ok=True)

brightness_factor = 1.5  # Increase brightness
contrast_factor = 1.2    # Increase contrast

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpg'):
        img = Image.open(os.path.join(input_folder, filename))

        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)

        output_filename = os.path.splitext(filename)[0] + '_adjusted.jpg'
        img.save(os.path.join(output_folder, output_filename))

        img.close()
