#!/usr/bin/python3
""" Module queries the Reddit API """

import requests


def recurse(subreddit, hot_list=None, after=None):
    """ Function queries the reddit API for hot topics """
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyUserAgent1.0"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        for field in children:
            hot_list.append(field.get("data").get("title"))

        after = data.get('data').get('after')
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
