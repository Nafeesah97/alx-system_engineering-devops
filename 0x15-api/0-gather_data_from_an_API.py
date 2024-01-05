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
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "/user{}".format(employee_id)).json()
    tasks = requests.get(url + "todos", params=("userId": employee_id)).json()

    completed = []
    for tas in tasks:
        if tas.get("completed") is True:
            completed.append(tas)
    
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(completed), len(tasks)))
    for t in completed:
        print("\t {}".format(t))
