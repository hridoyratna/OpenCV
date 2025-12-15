import cv2

image = cv2.imread("Python_logo.png")

if image is None:
    print("Could not load image.")
else:
    (h,w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("Original Image", image)
    cv2.imshow("Rotate 90 degree of the image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
