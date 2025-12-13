import cv2

image = cv2.imread('Python_logo.png')  

if image is not None:
    success = cv2.imwrite('output.png', image)
    if success:
        print("Image saved successfully as 'output_python.png'.")
    else:
        print("Failed to save the image.")

else:
    print("Error! Could not load the image.")

