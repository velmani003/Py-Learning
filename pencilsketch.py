import cv2

image = cv2.imread("Give any image here")
cv2.waitKey(0)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray_image)
cv2.waitKey(0)

inverted_img = 255 - gray_image
cv2.imshow("Inverted", inverted_img)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_img,(21,21),0)
inverted_blur = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
cv2.imshow("Original image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
