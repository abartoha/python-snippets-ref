'''
Python Code Snippets - stevepython.wordpress.com

153-Watermark an image
Source image and watermark image must be same size

Source, based on code from:
https://www.geeksforgeeks.org/addition-blending-images-using-opencv-python/
'''
import cv2

# Read Image1
source_img = cv2.imread('me-jack-400x266.jpg', 1)

# Read image2
water_mark = cv2.imread('watermark-400x266.jpg', 1)

# Blending the images with 0.1 and 1.0
img = cv2.addWeighted(water_mark, 0.1, source_img, 1.0, 0)

# Show the image
cv2.imshow('image', img)

# Save image
cv2.imwrite('watermarked.png',img)
 
# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.destroyAllWindows()
