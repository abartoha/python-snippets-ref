'''
Python Code Snippets - stevepython.wordpress.com

154-Combine two images

source, based on code from:
https://stackoverflow.com/questions/7589012/combining-two-images-with-opencv
'''

import cv2
import numpy as np

img1 = cv2.imread("watermark-400x266.jpg")
img2 = cv2.imread("me-jack-400x266.jpg")

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

#create empty matrix
vis = np.zeros((max(h1, h2), w1+w2, 3), np.uint8)

#combine 2 images
vis[:h1, :w1, :3] = img1
vis[:h2, w1:w1+w2, :3] = img2
cv2.imshow("Join imgs", vis)

# Save image
cv2.imwrite('joined-images.png', vis)

cv2.waitKey()
