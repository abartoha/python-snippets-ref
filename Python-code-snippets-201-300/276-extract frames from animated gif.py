"""Code snippets vol-56
   276-extract frames from an animated gif.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg
   Blog: stevepython.wordpress.com

Requirements:
pip3 install Pillow
An animated gif file named 'test-anim.gif'

Origin:
https://gist.github.com/revolunet/848913
Updated by Shambles. May 2020.
"""
import os
import webbrowser as web

from PIL import Image


def extract_frames(in_gif, out_folder):
    frame = Image.open(in_gif)
    n_frames = 0
    while frame:
        frame.save('%s/%s-%s.gif' %
                   (out_folder, os.path.basename(in_gif),
                    n_frames), 'GIF')

        n_frames += 1
        print('Extracting frame: ', n_frames)
        try:
            frame.seek(n_frames)
        except EOFError:
            break
    return True


save_dir = 'gif_frames'
chck_dir = os.path.isdir(save_dir)
if not chck_dir:
    os.makedirs(save_dir)

extract_frames('test-anim.gif', save_dir)
print('Finished.')
web.open(save_dir)
