"""Code snippets vol-46-snippet-226
   Blur part of image.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements: pip3 install Pillow

source:
https://stackoverflow.com/questions/9701515/filter-part-of-image-using-pil-python

Image:
https://pixabay.com/photos/model-woman-conceptual-fashion-2614569/
"""
import webbrowser
from PIL import Image, ImageFilter

image = Image.open('model.jpg')

# Position and size of blur box.
box = (210, 100, 340, 230)
crop_img = image.crop(box)

# You can change the amount of blur by changing the radius value.
blur_image = crop_img.filter(ImageFilter.GaussianBlur(radius=15))
image.paste(blur_image, box)

img = 'model_blur.jpg'
image.save(img)
webbrowser.open(img)
