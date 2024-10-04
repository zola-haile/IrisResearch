import cv2

# Load the image
img = cv2.imread('/Users/zola/Desktop/Projects/IrisReseach/images/190412_102_AD100/2019_102_001_Left_L1_0.bmp')

# Check if the image was loaded successfully
if img is None:
    print("Error: Image cannot be loaded. Check the file format or path.")
else:
    # Define the brightness factor (beta)
    brightness_factor = 50  # Positive for brighter, negative for darker
    
    # Change brightness (alpha=1 means no change in contrast)
    brightened_img = cv2.convertScaleAbs(img, alpha=0.75, beta=25)
    
    # Display the original and brightened image
    cv2.imshow("Original Image", img)
    cv2.imshow("Brightened Image", brightened_img)
    
    # Wait indefinitely until a key is pressed, then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

