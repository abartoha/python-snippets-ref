'''
   66-Convert image to greyscale
   pip install opencv-python
   taken from this brilliantly written blog post:
   https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/
   slightly shambleized by moi.
'''
import cv2

# Load a image.
image = cv2.imread('test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display orig and grey versions of image in windows.
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)

# Save converted image.
cv2.imwrite('conv_gray.jpg', gray)

# Wait until a key press, or user closes both windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
