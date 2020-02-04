#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    json_res = requests.get(url + "todos",
                            params={'userId': sys.argv[1]}).json()
    tasks = []
    task_count = len(json_res)
    for task in json_res:
        if task.get("completed") is True:
            tasks.append("\t " + task.get("title"))
    json_res = requests.get(url + "users/{}".format(sys.argv[1])).json()
    print("Employee {} is done with tasks({}/{}):".format(json_res.get("name"),
                                                          len(tasks),
                                                          task_count))
    for row in tasks:
        print(row)
