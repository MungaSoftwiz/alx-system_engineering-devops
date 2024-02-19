#!/usr/bin/python3
""" Export data in json format """
import json
import requests
import sys


def export_to_json_file(employee_id):
    """ Export data in JSON format

    Requirements:
        Records all tasks that are owned by this employee
        Format must be:
            { "USER_ID": [{"task": "TASK_TITLE", "completed":
            TASK_COMPLETED_STATUS, "username": "USERNAME"},
            {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,} ...]
        File name must be:
            USER_ID.json
    """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_data = requests.get(user_url).json()
    username = user_data['username']

    todos_data = requests.get(todos_url).json()

    if todos_data:
        json_data = {
                employee_id: [{
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": username
                } for todo in todos_data]
        }

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    export_to_json_file(int(employee_id))
