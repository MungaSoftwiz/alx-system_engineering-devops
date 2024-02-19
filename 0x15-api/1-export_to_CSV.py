#!/usr/bin/python3
""" Export data in CSV format """
import csv
import requests
import sys


def export_to_csv_file(employee_id):
    """ Export data in CSV format

    Requirements:
        Records all tasks that are owned by this employee
        Format must be:
            "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        File name must be:
            USER_ID.csv
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_data = requests.get(user_url).json()
    username = user_data['username']

    todos_data = requests.get(todos_url).json()

    csv_data = []
    for todo in todos_data:
        csv_data.append([todo['userId'], username, todo['completed'],
                         todo['title']])

    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_data)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    export_to_csv_file(int(employee_id))
