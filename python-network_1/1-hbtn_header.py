#!/usr/bin/python3
""" 
    import sys and requests
    sends a request to the URL and 
    displays the value of the variable X-Request-Id
"""


import sys
import requests

url = sys.argv[1]
r = requests.get(url)
r1 =  r.headers['X-Request-Id']
print(r1)

if __name__ == "__main__":
     main()
