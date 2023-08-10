""" import sys and requests 
    takes in a URL and an email address, 
    sends a POST request to the passed URL
    then display the body of the response
    """


import requests
import sys

url = sys.argv[1]
email = {'Your email is': sys.argv[2]}

r = requests.post(url = url, data = email)
r1 = r.text
print(r1)