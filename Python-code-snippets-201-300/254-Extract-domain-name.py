"""Code snippets vol-51.
   Snippet 254-Extract domain name.

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

pip3 install tldextract

Origin:
https://pydeep.com/get-domain-name-from-url-python-snippet/
"""
import tldextract

url = 'https://www.pydeep.com/how-to-install-python'
info = tldextract.extract(url)

print("Details:", info)
print()
print("Domain Name: ", info.domain)
print("Subdomain: ", info.subdomain)
print("Suffix: ", info.suffix)
print("Domain with suffix: ", info.registered_domain)
print("Full Domain: ", '.'.join(info))
