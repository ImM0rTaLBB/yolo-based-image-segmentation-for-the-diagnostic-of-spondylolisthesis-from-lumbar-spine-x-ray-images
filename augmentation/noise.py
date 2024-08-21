# This file will using image processing to add noise to the image. 
# This will create new set of images used for augmentation.

import numpy as np
from PIL import Image
import os

input_folder = ''
output_folder = ''

os.makedirs(output_folder, exist_ok=True)

noise_level = 20

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(input_folder, filename))

        img_array = np.array(img)

        noisy_img_array = img_array + np.random.normal(0, noise_level, img_array.shape).astype(np.uint8)

        noisy_img = Image.fromarray(noisy_img_array)

        output_filename = os.path.splitext(filename)[0] + '_noisy.jpg'
        noisy_img.save(os.path.join(output_folder, output_filename))

        img.close()
