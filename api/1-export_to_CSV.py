
#Gather Data From an API

import csv
import json
import requests
import sys

if __name__ == "__main__":
    emplooye_id = sys.argv[1]
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(emplooye_id))
    api_request1 = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(emplooye_id))
    data = api_request.text
    pjson = json.loads(data)
    data1 = api_request1.text
    pjson1 = json.loads(data1)

    title_count = 0
    title_complete = 0
    name_info = pjson['name']

    #export data to csv data
    filename = "{}.csv".format(emplooye_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for item in pjson1:
            user_id = emplooye_id
            username = name_info
            task_completed_status = item['completed']
            task_title = item['title']
            writer.writerow([user_id, username, task_completed_status, task_title])