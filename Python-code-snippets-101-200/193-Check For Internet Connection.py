"""
Python code snippets vol 39:
stevepython.wordpress.com

193-Check For Internet Connection
requirements: None

https://gist.github.com/jarvisrob/dbf6a6ad098102c0a290a567625b9634
"""
import socket

def check_internet(host="8.8.8.8", port=53, timeout=3):
    # Checks for internet connection by testing to see if it can
    # make a socket connetion to (host, port)
    # Host: 8.8.8.8 (google-public-dns-a.google.com)
    # Port: 53/tcp
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        return True
    except:
        return False
print(check_internet())
