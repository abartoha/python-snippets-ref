"""Code snippets vol-47-snippet-234
   Smoothing and blurring images.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:An image called model2.jpg
pip install opencv-python

origin:
https://gist.github.com/pknowledge/f414947872baa9b94bf5d290797fbb2d

image:
https://pixabay.com/photos/girl-model-pink-fashion-portrait-2189247/
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('model2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
