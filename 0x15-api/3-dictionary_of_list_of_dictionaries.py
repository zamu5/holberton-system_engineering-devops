#!/usr/bin/python3
# Returns information about his/her TODO list progress.

import json
import requests
import sys


if __name__ == "__main__":
    user = 1
    new_dic = {}
    url1 = "https://jsonplaceholder.typicode.com/users/"
    url = "https://jsonplaceholder.typicode.com/todos?userId="
    name = requests.get("{}{}".format(url1, user)).json()
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as json_file:
        while name:
            json_res = requests.get("{}{}".format(url, user)).json()
            tasks = []
            for task in json_res:
                new_task = {}
                new_task["task"] = task.get("title")
                new_task["completed"] = task.get("completed")
                new_task["username"] = name.get("username")
                tasks.append(new_task)
            new_dic[user] = tasks
            user += 1
            name = requests.get("{}{}".format(url1, user)).json()
        json_file.write(json.dumps(new_dic))
