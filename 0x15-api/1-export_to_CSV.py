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
    csv_file = f"{employee_id}.csv"
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"https://jsonplaceholder.typicode.com/users?id={employee_id}").json()[0]
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open(csv_file, 'w') as f:
        for task in tasks:
            f.write(f""""{task['userId']}","{user['username']}",\
"{task['completed']}","{task['title']}"\n""")
