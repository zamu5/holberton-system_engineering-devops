#!/usr/bin/python3
# Returns information about his/her TODO list progress.

import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    json_res = requests.get(url).json()
    tasks = []
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])).json()
    file_name = "{}.json".format(sys.argv[1])
    with open(file_name, 'w') as json_file:
        for task in json_res:
            new_task = {}
            new_task["task"] = task.get("title")
            new_task["completed"] = task.get("completed")
            new_task["username"] = name.get("username")
            tasks.append(new_task)
        new_dic = {"{}".format(sys.argv[1]): tasks}
        json_file.write(json.dumps(new_dic))
