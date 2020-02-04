#!/usr/bin/python3
"""create a cvs file with the data"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    json_res = requests.get(url).json()
    tasks = ""
    name = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])).json()
    file_name = "{}.csv".format(sys.argv[1])
    with open(file_name, 'w') as cvs_file:
        for task in json_res:
            tasks = ",".join(['"{}"'.format(name.get("id")),
                              '"{}"'.format(name.get("username")),
                              '"{}"'.format(task.get("completed")),
                              '"{}"'.format(task.get("title"))])
            cvs_file.write(tasks + "\n")
