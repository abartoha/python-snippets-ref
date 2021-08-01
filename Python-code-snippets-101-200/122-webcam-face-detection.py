'''
Webcam Face detection.

source:
https://github.com/JabaHum/python/tree/master/real-time-face-detection

requires this file in current dir:
haarcascade_frontalface_alt.xml
pip3 install cv2

Edited by Steve Shambles July 2019
stevepython.wordpress.com
'''

import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# grab the reference to the webcam
vs = cv2.VideoCapture(0)

# keep looping
while True:
	# grab the current frame
	ret, frame = vs.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break

	faces = faceCascade.detectMultiScale(frame)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)

	# show the frame to our screen
	cv2.imshow("Ugly TV", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# close all windows
cv2.destroyAllWindows()
