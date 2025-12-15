import cv2

image = cv2.imread("400X400.jpg")

if image is None:
    print("Could not load image.")
else:
    flipped_horizontally = cv2.flip(image, 1)
    flipped_vertically = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Horizontally", flipped_horizontally)
    cv2.imshow("Flipped Vertically", flipped_vertically)
    cv2.imshow("Flipped Both Axes", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
