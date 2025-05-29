# Image Segmentation and Classification for Spondylolisthesis using Deep Learning Models

## Abstract
Spondylolisthesis, a prevalent spinal condition marked by vertebral slippage, often leads to pain and functional limitations. This thesis investigated the potential of deep learning technique for improved detection of the lumbar spine. We introduced a new approach in employing YOLOv8 for image segmentation onto the dataset of 400 X-ray images (AP and LA views) of patients’ vertebrae. This refined detection could contribute to advancements in spondylolisthesis diagnosis and potentially earlier intervention, even with limited data. Our methodology used provided ground truth data from BUU-LSPINE converted into YOLO format . We enhanced x-ray images by using various image processing techniques to increase the quantity of the images. We processed both ground truth data and x-ray image using instance segmentation from YOLOv8 to segment each of vertebrae which be used in our medical application in finding the spondylolisthesis.
	The experiments demonstrated the effectiveness of YOLOv8 image segmentation for spondylolisthesis detection. The model achieved the highest precision of 94.7% for 5 classes in AP images without augmentation and 96.3% for 6 classes in LA images without augmentation. Additionally, the model yielded a peak mean average precision (mAP50) of 97.1% for 5 classes in AP images without augmentation and 98.24% for 6 classes in LA images with augmentation. Furthermore, the model achieved a minimum euclidean distance of 0.1852 in 5 classes AP images without augmentation and 0.1458 in 6 classes LA images with augmentation. Finally, the model exhibited a best intersection over union (IoU) of 95.78% in 5 classes AP images without augmentation and 93.77% in 6 classes LA images with augmentation.

## Background
Spondylolisthesis is the condition located in vertebra, most commonly in the lumbar spine where the it slips forward onto the one below. 
The causes are from various factors:
* Stress fracture – Weaken interarticularis, commonly found among young athletes range from gymnastics, football or weightlifting. 
* Age-related (After the age of 50) – As individuals age, intervertebral discs deteriorate, loss the ability to absorb shock
* Congenital defects – Malformations of the spine present from birth.
* Trauma – Car accidents or other injuries that lead to vertebral fractures and displacement.

## Lumber Vertebrae Structure
| AP (5 Classes) | LA (6 Classes) |
| :---: | :---: |
|![image](https://github.com/user-attachments/assets/74f58c2d-74ee-4084-bd47-04e87dead8a1)|![image](https://github.com/user-attachments/assets/ea43a47f-162c-4289-9ed9-265faee06c7d)|

## Scope
* Dataset – The dataset will be collected from publicly available BUU-LSPINE.
* Preprocessing – Applying various augmentation techniques to enhance the image and increase quantity of the image
* Image Segmentation – Introduce new approach in detecting vertebral position using YOLOv8 segmentation model.
* Model Evaluation – Evaluate each of the method comparing both YOLOv5 from BUU-LSPINE, YOLOv5 OBB from our run and new approach using YOLOv8 Segmentation, and training duration for each version.
* Medical Application – Real world diagnostics using Meyerding classification applied with our approach.

## Hardware
* CPU – Ryzen 9 5900X
* RAM – 32GB DDR4 3600MHz
* GPU – RTX 3080Ti 12GB

## Software
* Windows 11 Pro
* Google Colab
* Jupyter Notebook
* Python 3.10.9
* Tensorflow 2.10.0 (for GPU acceleration on native Windows systems).

## Methodology
![image](https://github.com/user-attachments/assets/15b8c6a1-fe3f-4c56-8822-7655cd1b384c)

## Data Source
The data was provided by [BUU Spine Dataset](https://services.informatics.buu.ac.th/spine/)

## Dataset Information
| Name | Description |
| :---: | :---: |
| Image Type | X-ray |
| Image View | AP and LA |
| Body Part | Lumbar Spine (LSPINE) |
| Number of Patients | 400 |
| Number of Images | 800 |
| Number of Spondylolisthesis | 69 |
| Dataset Storage Size | 885MB |
| Ground Truth | Vertebral position, Spondylolisthesis Diagnosis |
| Lumbar vertebral position targets | Coordinate points of L1 to L5 |
| Spondylolisthesis diagnosis targets | Left Laterolisthesis, Right Laterolisthesis, Anterolisthesis, Retrolisthesis |
| File Types | Images: .jpg, Ground truth: .csv |
| Sources | Burapha University Hospital, Thailand |
| Year | 2000 - 2021 |
| Age | 6 - 97 Years old |
| Image Dimension | Height: 1434 - 3408 pixels, Width: 860 - 3040 pixels |

## Image Enhancement & Augmentation
### Challenges
* Various x-ray image quality 
* Machine brands and configurations
### Solutions
* Histogram Equalization – Ensure a uniform contrast distribution across all x-rays image.
* Image processing techniques
  * Blurring – mimic patient motion
  * Brightness/Contrast Adjustments – mimic machine configurations
  * Negative Color – replicate radiologist specific viewing reference
  * Noise Addition – mimic artifacts like machine malfunction or object in patient’s pocket
  * Power Law Transformations – mimic patient improper positioning or machine configurations
* Dataset expansion: Increased training data from 280 to 1,960 images.
### Why is it crucial
* Increase number of limited dataset
* Improve robustness to variations in real-world variability such as patient factors and machine malfunctions or configurations.
* We choose to not applying augmentations to validation and test because we want to evaluate the model’s performance on images as close to real-world examples as possibles
* We also include original image during training to ensure that model doesn’t become too reliant on the enhanced images.

![image](https://github.com/user-attachments/assets/5c7d3889-8e26-40b6-8088-bdb2cc04e8f3)

## Model Configuration
| Architecture | YOLOv5 OBB | YOLOv8 Segmentation |
| :---: | :---: |  :---: |
|Input Size|640 x 640|640 x 640|
|Batch Size|4|4|
|Epoch|100|100|
|Type|Object Detection|Image Segmentation|
|Weights|yolov5s.pt|yolov8-seg.pt|
|Training Time - 5 Classes (AP Vanilla)|22m 16s|17m 23s|
|Training Time - 5 Classes (AP Augmentation)|38m 38s|37m 13s|
|Training Time - 6 Classes (LA Vanilla)|24m 19s|17m 1s|
|Training Time - 6 Classes (LA Augmentation)|31m 16s|31m 53s|

## Training Duration
![image](https://github.com/user-attachments/assets/db1ec270-89ab-4367-b261-69ff1c7bc687)

## Experimental Results
### 5 Classes AP Images
| Model | Training Set | Data | View | Precision | Recall | F1-Score | mAP50 | mAP95 |
| :---: | :---: |  :---: | :---: | :---: |  :---: | :---: | :---: |  :---: |
|YOLOv5 (BULL-LSPINE)|2880|Original|AP|N/A|95.82|N/A|96.68|81.93|
|YOLOv5 OBB|280|Original|AP|94.50|93.32|93.91|96.38|77.28|
|YOLOv8 Segmentation|280|Original|AP|94.72|92.74|93.72|97.08|77.76|
|YOLOv8 Segmentation|1960|Original|AP|92.40|95.38|93.87|96.60|77.68|

### 6 Classes LA Images
| Model | Training Set | Data | View | Precision | Recall | F1-Score | mAP50 | mAP95 |
| :---: | :---: |  :---: | :---: | :---: |  :---: | :---: | :---: |  :---: |
|YOLOv5 (BULL-LSPINE)|2880|Original|LA|N/A|95.72|N/A|96.83|83.45|
|YOLOv5 OBB|280|Original|LA|94.75|95.03|94.89|96.93|78.73|
|YOLOv8 Segmentation|280|Original|LA|96.00|94.34|95.16|97.98|83.62|
|YOLOv8 Segmentation|1960|Original|LA|95.98|96.00|95.99|98.24|84.58|

## Heatmap
This heatmap is provided by [EigenCam](https://github.com/jacobgil/pytorch-grad-cam/blob/master/tutorials/EigenCAM%20for%20YOLO5.ipynb) and modified to make it work with YOLOv8 segmentation.

![image](https://github.com/user-attachments/assets/9a18cb5f-a1b8-4741-a4d4-e5c3b64adadd)

## Results
### AP Images Segmentation Results
![image](https://github.com/user-attachments/assets/8cf4c151-85fe-48b7-a445-cd3dac5fea56)

### LA Images Segmentation Results
![image](https://github.com/user-attachments/assets/c73d3159-7ea7-4b68-9f5a-21ae5af0df7e)

## Medical Application (Rudimentary)
We introduced the Meyerding Classification for grading the severity of spondylolistheis.
* Grade I: 0-25%
* Grade II: 26-49%
* Grade III: 50-74%
* Grade IV: 75-99%
* Grade V (spondylolisthesis): > 100%

![image](https://github.com/user-attachments/assets/999ad08d-7822-4185-82d0-e79ab43b7831)

Our approach to spondylolisthesis severity assessment leverages newly acquired segmented images and annotated lumbar vertebrae corner points. This data allows for a more in-depth analysis of individual lumbar positioning. We commenced by plotting all corner points onto the X-ray image. Yellow dots represent vertebrae corner points, while green lines connect opposing points to visualize the lumbar structure.
For anteroposterior (AP) images, we categorize the vertebrae into four pairs: L1-L2 (Pair 1), L2-L3 (Pair 2), L3-L4 (Pair 3), and L4-L5 (Pair 4). Lateral (LA) images include five pairs, with the first four identical to the AP view. The fifth LA pair comprises L5 and S1.
Subsequently, we calculate the width of each vertebra by subtracting the x-coordinate of its left corner point from the x-coordinate of its right corner point. For the first pair (L1-L2), L1 serves as the reference vertebra. We quantify slippage by subtracting the x-coordinate of the superior vertebra's left corner point from the x-coordinate of the inferior vertebra's left corner point. This calculation reflects the displacement of the inferior vertebra relative to the superior one. Finally, we calculate the percentage of slippage using the following formula:

![image](https://github.com/user-attachments/assets/e51de7f8-c464-4f9c-88d1-0f29871f0349)

![image](https://github.com/user-attachments/assets/5a7d902e-e3b8-48f1-a122-1a1a86911e8a)

Following the calculations for each pair of lumbar vertebrae, we output the results in four distinct categories: slip direction (indicating left or rightward slippage), grading (based on the Meyerding classification), percentage of slip, and condition (assessing the potential risk of spondylolisthesis).
For anteroposterior (AP) images, the potential conditions include normal, left laterolisthesis, and right laterolisthesis. These conditions represent different patterns of vertebral displacement. Left laterolisthesis occurs when the vertebra slips to the left side, while right laterolisthesis indicates slippage to the right side. Normal refers to a lack of significant displacement. For lateral (LA) images, the potential conditions are normal, anterolisthesis, and retrolisthesis. Anterolisthesis signifies anterior slippage of the vertebra, while retrolisthesis indicates posterior displacement. Normal again indicates a lack of significant slippage.
The visualization of these results for AP and LA images. This figure provides a visual representation of the calculated slip direction, grading, percentage of slip, and condition for each pair of lumbar vertebrae, facilitating a comprehensive understanding of the spondylolisthesis severity. 

![image](https://github.com/user-attachments/assets/ee4296e3-d017-4a7b-8e85-0bcc7ccdf885)

## Discussion
* YOLOv8 Segmentation is faster in training compared to YOLOv5 in almost every classes.
* YOLOv8 Segmentation is the best overall model due to high recall and overall balance in medical imaging.
* Enhanced version has the highest recall and very strong F1-score.
* Enhanced dataset improves the performance of the model.
* Compared to the work of [Podchara Klinwichit et al. (2023)](https://www.mdpi.com/2076-3417/13/15/8646), we achieved better results and performance quite competitively despite the smaller dataset.
* Meyerding classification using coordinate points facilitates preliminary assessment of spondylolisthesis.
* BUU-LSPINE dataset demonstrates potential for advancing object detection and segmentation techniques.
* Increased public availability of lumbar spine datasets is crucial for further research and development.

## Future Works
* Revolutionize patient care: Integrate model into medical equipment to streamline diagnosis, minimize misdiagnosis, and improve outcomes.
* Expand capabilities: Develop comprehensive tool to detect and diagnose various spinal conditions (scoliosis, fractures, spinal traumas).
* Enhance model: Conduct research on data augmentation, model architecture optimization, and integration with other imaging modalities.
* Different model: Test out more powerful or more sophisticated segmentation model combine with our data.
* Prioritize user-friendliness: Develop intuitive interfaces and workflows for seamless clinical integration.



