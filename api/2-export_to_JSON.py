"""
extend Python script to export data in the JSON format.
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, 
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    api_request1 = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
    data = api_request.text
    pjson = json.loads(data)
    data1 = api_request1.text
    pjson1 = json.loads(data1)

    name_info = pjson['username']

    filename = "{}.json".format(employee_id)

    # Create the dictionary structure
    result = {
        employee_id: [{
            "task": item["title"],
            "completed": item["completed"],
            "username": name_info
        } for item in pjson1]
    }

    # export data to json file

    with open(filename, "w") as outfile:
        json.dump(result, outfile)