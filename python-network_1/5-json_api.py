""" 
    Takes in a letter and sends a POST request 
    To http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import sys
import requests

url = "http://0.0.0.0:5000/search_user"
q = sys.argv[1] if len(sys.argv) > 1 else ""

r = requests.get(url, data = {'q': q})
try:
    r1 = r.json()

    if r1:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

if __name__ == "__main__":
     main()

