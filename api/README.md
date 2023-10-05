<h1>API</h1>
<h1>0. Gather data from an API</h1>
<br>
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
<br>
NB: The endpoint for access specific TODO items for an employee with ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will be https://jsonplaceholder.typicode.com/users/1
<br>
Requirements:
<br>
You must use urllib or requests module
<br>
The script must accept an integer as a parameter, which is the employee ID
<br>
The script must display on the standard output the employee TODO list progress in this exact format:
<br>
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
<br>
where:
<br>
EMPLOYEE_NAME: name of the employee
<br>
NUMBER_OF_DONE_TASKS: number of completed tasks
<br>
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
<br>
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
<br>

<h1>1. Export to CSV</h1>
<br>
Using what you did in the task #0, extend your Python script to export data in the CSV format.
<br>
Requirements:
<br>
Records all tasks that are owned by this employee<br>
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"<br>
File name must be: USER_ID.csv<br>
<h1>2. Export to JSON</h1>
<br>
Using what you did in the task #0, extend your Python script to export data in the JSON format.
<br>
Requirements:
<br>
Records all tasks that are owned by this employee<br>
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}<br>
File name must be: USER_ID.json<br>
<h1>3. Dictionary of list of dictionaries</h1>
<br>
Using what you did in the task #0, extend your Python script to export data in the JSON format.
<br>
Requirements:
<br>
Records all tasks from all employees<br>
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json