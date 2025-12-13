import cv2

image = cv2.imread('Python_logo.png')   

if image is not None:
    cv2.imshow("Display Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image.")

