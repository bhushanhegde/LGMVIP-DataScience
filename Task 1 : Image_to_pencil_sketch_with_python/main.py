'''

Steps:

1] Take the  an image in the form of RGB as input.
2] Resize that image to 480,480 for data manipulation
3] Convert the resized image into Gray image
4] Convert the Gray Image into Inverted image.
5] Convert the Inverted Image to Blur image.
6] Convert blur Image to Final sketch by division.

'''

#impor opencv module which is used for image processing

import cv2


#take an image as input

image = cv2.imread('Original_Image.jpg')

# resize the original image
original_image = cv2.resize(image, (480,480))
cv2.imshow('Original Image', original_image)

#Convert the resized image into Gray image
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)

#Convert the Gray Image to Inverted image.
inverted_image = cv2.bitwise_not(gray_image)
cv2.imshow('Inverted Image', inverted_image)

# Convert the Inverted Image to Blur image.
blur_image = cv2.GaussianBlur(inverted_image, (21,21), 0)
cv2.imshow('Blur Image', blur_image)

# Convert Blur Image to Final Sketch
sketch = cv2.divide(gray_image, 255-blur_image, scale=256.0)
cv2.imshow('Sketch', sketch)

cv2.waitKey(0)
