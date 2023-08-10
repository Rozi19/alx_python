import sys
import requests

url = sys.argv[1]
r = requests.get(url)
r1 =  r.headers['X-Request-Id']
print(r1)