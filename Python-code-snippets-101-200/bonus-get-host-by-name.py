import socket

ghbn = socket.gethostbyname('google.com')
print(ghbn)

ghba = socket.gethostbyaddr('216.58.204.78')
print(ghba)
