"""Code snippets vol-49-snippet-241
   Face Scraper

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:
haarcascade_frontalface_default.xml in current dir.
pip3 install opencv-python
https://pypi.org/project/opencv-python/

images:
https://pixabay.com/photos/redhead-girls-model-hair-1903320/
https://pixabay.com/photos/human-faces-man-women-eyes-head-740259/

origin:
https://www.digitalocean.com/community/tutorials/how-to-detect-and-extract-faces-from-an-image-with-opencv-and-python
"""

import cv2

imagePath = 'redheads.jpg'

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    'haarcascade_frontalface_default.xml')
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print('[INFO] Found {0} Faces.'.format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y:y + h, x:x + w]
    print('[INFO] Object found. Saving locally.')
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

status = cv2.imwrite('faces_detected.jpg', image)
print('[INFO] Image faces_detected.jpg written to filesystem: ', status)
