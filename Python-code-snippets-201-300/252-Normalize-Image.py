"""Code snippets vol-51.
   Snippet 252-Normalize an Image.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements: pip3 python-opencv, pip3 install numpy.

Origin:
https://www.codespeedy.com/normalizing-an-image-in-opencv-python/
"""
import cv2 as cv
import numpy as np

img = cv.imread('foxtrots.png')
norm_img = np.zeros((800, 800))
final_img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)

cv.imshow('Original Image', img)
cv.imshow('Normalized Image', final_img)
cv.imwrite('normalized.jpg', final_img)

cv.waitKey(0)
cv.destroyAllWindows()
