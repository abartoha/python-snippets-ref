"""
Python code snippets vol 39:
stevepython.wordpress.com

192-Face Counter

requirements: pip3 install opencv-python
Also the file haarcascade_frontalface_default.xml needs to be in the
current directory where you run the source code from.
Do a search on your computer for it

source:
https://techtutorialsx.com/2017/05/02/python-opencv-face-detection-and-counting/
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('crowd2.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grayImage)

print(type(faces))

if len(faces) == 0:
    print("No faces found")

else:
    print(faces)
    print(faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2.rectangle(image, ((0, image.shape[0] -25)),
                  (270, image.shape[0]), (255, 255, 255), -1)
    cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]),
                (0, image.shape[0] -10),
                cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

    cv2.imshow('Image with faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
