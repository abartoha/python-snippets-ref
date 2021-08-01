'''
Python Code Snippets - stevepython.wordpress.com

152-Bandwidth Monitor
---------------------
Reports how much bandwidth your connection is currently using

Source:
https://stackoverflow.com/questions/15616378/python-network-bandwidth-monitor
'''
import time
import psutil

def main():
    '''Detect internet activity. '''
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def convert_to_gbit(value):
    ''' Humanise the output to less digits. '''
    return value/1024./1024./1024.*8

def send_stat(value):
    ''' Output result to shell.'''
    print("%0.3f" % convert_to_gbit(value))

main()
