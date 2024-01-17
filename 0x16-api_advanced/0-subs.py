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
    headers = {"User-Agent": "My-User-Agent"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code >= 300:
        return 0
    subs = r.json().get("data").get("subscribers")
    return subs
