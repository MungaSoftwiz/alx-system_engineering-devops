#!/usr/bin/python3
""" Module queries the Reddit API """

import requests


def top_ten(subreddit):
    """ Queries the reddit API for top 10 hot topics """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyUserAgent1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        for field in children:
            print(field.get('data').get('title'))
    else:
        print(None)
