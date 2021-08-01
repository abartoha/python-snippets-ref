'''
Python code snippets vol 38:
186-Get local IP address
stevepython.wordpress.com

requirements:None

source:
https://gist.github.com/MattWoodhead/541f23ecd9b464adf2b2e1598aa9261d
'''
import socket

def ip_check():
    """ uses the sockets module to find the local IP address """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Ping Google DNS server
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

print(ip_check())
