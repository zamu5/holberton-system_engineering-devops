#!/usr/bin/python3
# Returns information about his/her TODO list progress.

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    req = requests.get(url)
    json_res = req.json()
    tasks = []
    task_done = 0
    task_count = len(json_res)
    for task in json_res:
        if task.get("completed") is True:
            tasks.append("\t " + task.get("title"))
            task_done += 1
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1]))
    json_res = req.json()
    print("Employee {} is done with tasks({}/{})".format(json_res.get("name"),
                                                         task_done,
                                                         task_count))
    for row in tasks:
        print(row)
