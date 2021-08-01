"""Code snippets vol-54
   270-Create a gradient background.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

requirements:
pip3 install Pillow

origin:
https://gist.github.com/redjack001/169e388d031925743b83f525552565e8
"""
from PIL import Image

pixel_list = []
pixel_w = []

# set the size of the new image.
w = 500
h = 200

# Change these 3 numbers to experiment with colours.
start1 = (255, 255, 255)
s = list(start1)
pixel_list.append(start1)
end1 = (174, 15, 15)
e = list(end1)

f = 1
r = (s[0] - e[0])/w*f
g = (s[1] - e[1])/w*f
b = (s[2] - e[2])/w*f

t = ()

for j in range(0, w):
    t = pixel_list[j]

    # Convert pixel tuple to a list and recalculate.
    li = list(t)
    li[0] = int(max((li[0] - r*j), 0))
    li[1] = int(max((li[1] - g*j), 0))
    li[2] = int(max((li[2] - b*j), 0))
    z = (li[0], li[1], li[2])
    final_t = tuple(z)

    pixel_list[j] = final_t
    for i in range(0, h):
        pixel_w = []
        pixel_w.append(final_t)
        pixel_list.extend(pixel_w)

l = len(pixel_list)
del pixel_list[l-1:]

im = Image.new('RGB', (w, h))
im.putdata(pixel_list)
im.save("gradient.jpg")
im.show()
