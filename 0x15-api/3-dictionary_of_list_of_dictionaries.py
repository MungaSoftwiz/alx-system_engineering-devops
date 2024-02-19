#!/usr/bin/python3
""" Export data of all users in json format """
import json
import requests


def export_to_json_file():
    """ Export data in JSON format

    Requirements:
        Records all tasks that are owned by this employee
        Format must be:
            { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS},...]
            "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS},...]}
        File name must be:
            todo_all_employees.json
    """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users"

    user_data = requests.get(user_url).json()

    all_tasks = {}
    for user in user_data:
        user_id = user['id']
        username = user['username']

        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_data = requests.get(todos_url).json()

        user_tasks = []
        for todo in todos_data:
            user_tasks.append({
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed'],
            })

        all_tasks[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    export_to_json_file()
