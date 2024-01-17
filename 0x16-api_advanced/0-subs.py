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
    r = requests.get(f"http://www.reddit.com/r/{subreddit}/about.json",
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'})
    print(r)
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
