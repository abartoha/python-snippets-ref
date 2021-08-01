"""Code snippets vol-44-snip-217
217-Create thumbnails of images.

Feb 2020
stevepython.wordpress.com

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Requirements:
pip install pillow
Some jpg images in a folder called images in current directory.

source:
https://note.nkmk.me/en/python-pillow-square-circle-thumbnail/
"""
import glob
import os
from PIL import Image

thumb_width = 150
src_dir = 'images'
dst_dir = r'images\thumbnails'

chk_dir = os.path.isdir(dst_dir)
if not chk_dir:
    os.mkdir(r'images\thumbnails')

files = glob.glob(os.path.join(src_dir, '*.jpg'))

def crop_max_square(pil_img):
    """Crop image."""
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def crop_center(pil_img, crop_width, crop_height):
    """Resize."""
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
for f in files:
    im = Image.open(f)
    im_thumb = crop_max_square(im).resize((thumb_width, thumb_width), Image.LANCZOS)
    ftitle, fext = os.path.splitext(os.path.basename(f))
    print(f)
    im_thumb.save(os.path.join(dst_dir, ftitle + '_thumbnail' + fext), quality=95)
