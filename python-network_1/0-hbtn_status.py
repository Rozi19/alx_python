""" import requests and send request """
import requests

r = requests.get('https://alu-intranet.hbtn.io/status')
r1 = r.text
r2 = type(r.text)
print("Body response:")
                print("- type: {}".format(r2))
                print("- content: {}".format(r1))