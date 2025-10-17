# To-do CLI Project

https://github.com/benjo27maker/To-do-CLI

https://roadmap.sh/projects/task-tracker

This project is a simple command-line to-do list application written in Python. The to-do list stores tasks in a seperate json file and updates that file everytime a change is made  
It allows you to keep track of tasks that need to be done using simple terminal commands.

I created this as my first larger-scale Python project to gain experience building something practical and useful.

---

## Features

- Add new tasks  
- Delete tasks  
- Update task descriptions  
- Mark tasks as **to-do**, **in-progress**, or **done**  
- List all tasks or filter by status  
- Each task includes:
  - A unique ID number  
  - Creation time  
  - Last updated time  
  - Current status  

---

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/benjo27maker/To-do-CLI.git
   cd To-do-CLI

2. Run the CLI using python:

    ```bash
    python3 Todo.py add 'walk the dog'

3. create and update your to-do list using the following commands:

| Action | Command | Example Output |
|--------|----------|----------------|
| Add a new task | `python3 Todo.py add "buy food"` | `'buy food' added to to-do list` |
| List all tasks | `python3 Todo.py list` | `'buy food' 1` |
| Mark a task as in progress | `python3 Todo.py mark in-progress 1` | *(no output)* |
| List in-progress tasks | `python3 Todo.py list in-progress` | `'buy food' 1` |
| Update a task | `python3 Todo.py update 1 "buy food and drinks"` | *(no output)* |
| Delete a task | `python3 Todo.py delete 1` | *(no output)* |
| List again (after deleting) | `python3 Todo.py list` | `There are no tasks in the to-do list.` |



