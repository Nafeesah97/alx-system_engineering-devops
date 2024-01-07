#!/usr/bin/python3
"""Importing necessary libraries"""
import json
import requests
import sys

"""



This is a python script using REST API to get
information about his/her TO DO list progress
Author: Nafeesah
"""


if __name__ == "__main__":
    json_file = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/"
    userurl = f"https://jsonplaceholder.typicode.com/users?"
    user = requests.get(userurl).json()
    tasks = requests.get(url + "todos").json()

    for users in user:
        for task in tasks:
            task_list = []
            if users["id"] == task['userId']:
                json_obj = {}
                task_dic = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": users["username"],
                    }
            task_list.append(task_dic)
        json_obj = {users["id"]: task_list}

    with open(json_file, 'w') as f:
        json.dump(json_obj, f)
