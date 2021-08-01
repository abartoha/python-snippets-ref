'''
Python Code Snippets - stevepython.wordpress.com

146-List All Wireless Networks

source:
https://stackoverflow.com/questions/31868486/
list-all-wireless-networks-python-for-pc
'''
import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")

ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0

while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)
