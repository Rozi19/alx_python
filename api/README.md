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