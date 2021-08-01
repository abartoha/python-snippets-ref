"""
Python code snippets vol 39:
stevepython.wordpress.com

194-Centre Text On Image

requirements:
pip3 install python-opencv
pip3 install numpy

source
https://gist.github.com/xcsrz/8938a5d4a47976c745407fe2788c813a
"""
import cv2
import numpy as np

# create blank image - y, x
img = np.zeros((600, 1000, 3), np.uint8)

# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text = "stevepython.wordpress.com"

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]

# get coords based on boundary
textX = int((img.shape[1] - textsize[0]) / 2)
textY = int((img.shape[0] + textsize[1]) / 2)

# add text centered on image
cv2.putText(img, text, (textX, textY), font, 1, (255, 255, 255), 2)

# display image
cv2.imshow('image', img)

# wait so you can see the image
cv2.waitKey(0)

# cleanup
cv2.destroyAllWindows()
