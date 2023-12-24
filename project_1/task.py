# Task management system

# - invoke user to input task
# - unvoke the user to input the task until user inputs 'exit' string
# - once user exit the task input, print the task items

tasks = []

while True:
    task = input("Enter task name:")

    if task == 'exit':
        break

    tasks.append(task)

for item in tasks:
    print(item)