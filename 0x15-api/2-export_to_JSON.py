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
    employee_id = sys.argv[1]
    json_file = f"{employee_id}.json"
    url = "https://jsonplaceholder.typicode.com/"
    userurl = f"https://jsonplaceholder.typicode.com/users?id={employee_id}"
    user = requests.get(userurl).json()[0]
    tasks = requests.get(url + "todos", params={"userId": employee_id}).json()

    task_list = []
    task_dic = {}
    json_obj = {}
    for task in tasks:
        task_dic["task"] = task['title']
        task_dic["completed"] = task['completed']
        task_dic["username"] = user['username']
        task_list.append(task_dic)
        json_obj[f"{employee_id}"] = task_list

    with open(json_file, 'w') as f:
        json.dump(json_obj, f)
