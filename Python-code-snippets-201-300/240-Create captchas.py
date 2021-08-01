"""Code snippets vol-48-snippet-240
    Create captcha image.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

Requirements:
pip3 install captcha
pip3 install Pillow

origin:
https://www.code-learner.com/generate-graphic-verification-code-using-python-captcha-module/
https://github.com/lepture/captcha
"""

# Import ImageCaptcha class.
from captcha.image import ImageCaptcha

# Create a new ImageCaptcha instance.
IMG = ImageCaptcha()

# Generate image with the text python.
IMAGE = IMG.generate_image('Y5WH8X')

# Save the image to a file.
IMAGE.save('captcha.jpg')

# Display the image
IMAGE.show()
