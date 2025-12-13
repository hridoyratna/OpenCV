import cv2

# image = cv2.imread('Python_logo.png')    # If the image is stored in the same folder..
image = cv2.imread('D:/Language Practice/OpenCV/Images/Python_logo.png')   #For different folder..

if image is None:
    print("Error! Image not found.")
else:
    print("Image loaded successfully.")

