import cv2
import numpy as np
from PIL import Image

# Load image using OpenCV
img = cv2.imread('/Users/zola/Desktop/Projects/summer/images/190412_102_AD100/2019_102_001_Left_R2_0.bmp')

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Brightness Calculation (mean pixel value)
brightness = np.mean(gray_img)

# Contrast Calculation (Standard deviation of pixel values)
contrast = np.std(gray_img)

# Alternative Contrast Calculation (Michelson Contrast)
I_max = np.max(gray_img)
I_min = np.min(gray_img)
michelson_contrast = (I_max - I_min) / (I_max + I_min)

# Print Results
print(f"Brightness: {brightness}")
print(f"Standard Deviation Contrast: {contrast}")
print(f"Michelson Contrast: {michelson_contrast}")

