""" 
    import sys and requests
    sends a request to the URL and 
    displays the value of the variable X-Request-Id
"""


import sys
import requests

r = requests.get("https://intranet.hbtn.io")
r1 =  r.headers['X-Request-Id']
print(r1)