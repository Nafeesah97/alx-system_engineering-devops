#!/usr/bin/python3
"""Importing necessary libraries"""
import requests
import sys

"""



This is a python script using REST API to get
information about his/her TO DO list progress
Author: Nafeesah
"""


if __name__ == "__main__":
    employee_id = sys.argv[1]
    userurl = f"https://jsonplaceholder.typicode.com/users?id={employee_id}"
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(userurl).json()[0]
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = []
    for tas in tasks:
        if tas.get("completed") is True:
            completed.append(tas)

    print("Employee {} is done with tasks({}/{}):".format(
          user['name'], len(completed), len(tasks)))
    [print("\t {}".format(c['title'])) for c in completed]
