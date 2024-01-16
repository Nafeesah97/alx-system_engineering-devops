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
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = requests.get(url, allow_redirects=False)
    return data