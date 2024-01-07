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
    user = requests.get(userurl).json()[0]
    tasks = requests.get(url + "todos").json()
    print(user)
    print("--------")
    print(tasks)

    """task_list = []
    json_obj = {}
    for i in 
    for task in tasks:
        task_dic = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"],
            }
        task_list.append(task_dic)
    json_obj = {employee_id: task_list}

    with open(json_file, 'w') as f:
        json.dump(json_obj, f)"""
