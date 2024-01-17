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
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                     allow_redirects=False)
    print(r)
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
