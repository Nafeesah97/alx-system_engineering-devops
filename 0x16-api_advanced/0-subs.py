#!/usr/bin/python3
import requests
"""
a function that queries the Reddit API
returns the number of subscribers
Author: Nafeesah
"""


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.json().get("data") is None:
        return 0
    subs = r.json().get("data").get("subscribers")
    return subs
