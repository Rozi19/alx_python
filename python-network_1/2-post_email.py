""" import sys and requests 
    takes in a URL and an email address, 
    sends a POST request to the passed URL
    then display the body of the response
    """


import requests
import sys
def main():
    url1 = sys.argv[1]
    email = sys.argv[2]

    r = requests.post(url = url1, data = {'Email': email})
    r1 = r.text
    print(r1)
if __name__ == "__main__":
     main()
