#!/usr/bin/python3

import operator
import re
import requests


def count_words(subreddit, counter, after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers={'user-agent': 'Mozilla/5.0'},
                       allow_redirects=False,
                       params={'after': after})
    if type(counter) is list:
        dic = {}
        for word in counter:
            dic[word] = 0
        counter = dic
    if req.status_code != 200:
        return None
    json_req = req.json()
    for word in counter.keys():
        for post in json_req["data"]["children"]:
            regex = re.compile("^{}$".format(word), re.I)
            for w in post["data"]["title"].split():
                if regex.findall(w):
                    counter[word] += 1
    if json_req["data"]["after"] is not None:
        count_words(subreddit, counter, json_req["data"]["after"])
    else:
        values_sort = sorted(counter.items(), key=operator.itemgetter(1),
                             reverse=True)
        for value in enumerate(values_sort):
            if counter[value[1][0]] != 0:
                print("{}: {}".format(value[1][0], counter[value[1][0]]))
