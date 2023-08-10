
""" 
    Takes in a letter and sends a POST request 
    To http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys

def main():
    url = 'http://0.0.0.0:5000/search_user'
    r1 = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': r1}
    r = requests.post(url, data=data)

    try:
        r2 = r.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if isinstance(r2, dict):
        if 'id' in r2 and 'name' in r2:
            print("[{}] {}".format(r2['id'], r2['name']))
        elif 'message' in r2:
            print(r2['message'])
        else:
            print("No result")
    else:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
