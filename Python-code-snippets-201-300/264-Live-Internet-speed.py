"""Code snippets vol-53
   264-Live Internet speed.

   Download all snippets so far:
   https://wp.me/Pa5TU8-1yg

   Blog: stevepython.wordpress.com

pip3 install psutil
https://pypi.org/project/psutil/

Origin:
https://gist.github.com/b3rkaydem1r/e8e365e38bd7e7ca48cf35cfff147b16
"""
import math
import time

import psutil

def main():
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value
        time.sleep(1)

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '{} {}'.format(s, size_name[i])

def send_stat(value):
    print(convert_size(value))

main()
