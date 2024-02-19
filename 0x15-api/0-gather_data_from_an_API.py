#!/usr/bin/python3
""" Returns todos list progress of a given employee"""
import requests
import sys


def get_todo_progress(employee_id):
    """ Return info about TODO list progress
    Display format of script TODO list to standard output:

    First line:
        Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS
        /TOTAL_NUMBER_OF_TASKS):
    Second and N next lines:
        Title of completed tasks: TASK_TITLE(1 tabulation and space preceding)
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_data = requests.get(user_url).json()
    employee_name = user_data['name']

    todos_data = requests.get(todos_url).json()
    complete_tasks = [t['title'] for t in todos_data if t['completed']
                      is True]

    print(f"Employee {employee_name} is done with tasks({len(complete_tasks)}"
          f"/{len(todos_data)}):")
    for title in complete_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_todo_progress(int(employee_id))
