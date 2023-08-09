""" import requests and send get request 
    then print the conent and type """


import requests

r = requests.get('https://alu-intranet.hbtn.io/status')
r1 = r.text
r2 = type(r.text)
print("Body response:\n""\t- type: {}\n""\t- content: {}".format(r3, r1))
