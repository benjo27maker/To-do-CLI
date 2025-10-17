
""" to-do cli project, this project serves as a simple to-do list that keeps track
of tasks as well as their status """

#importing relevant libraries
import sys
import json
import os
from datetime import datetime 




# checking if the json file to store tasks in already exits
if os.path.exists('tasks.json'):
    
    # creates an array of dictinaries for tasks with the contents of the json file
    # returns an empty array if json file doesnt exist or is empty
    with open("tasks.json", 'r') as file:
        try:
            tasks=json.load(file)
        except json.JSONDecodeError:
            tasks=[]
else:
    tasks=[]


def add_task(task):
    
    """" this function adds tasks to the to do list

    args: task (string)

    returns: a statement confirming its addition or to say it is already on the to-do list
    
       """

    # checks if task is already in to-do list
    for t in tasks:
        if t.get('task')==task:
            print(f'{task} is already in to-do list')
            return

    # adds task to to-do list if it is not already on there
    tasks.append({'task':task,'status':'to-do','ID':len(tasks)+1,'createdAt':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'updatedAt':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
        print(f'{task} successfully added ID:{len(tasks)}')

def delete_task(ID):
    ''' this function delets a task from the to-do list 
    
    args: ID (int)

    returns: None
    
    '''


    # checks if the task is in to-do list 
    is_task=False

    # removes task
    for t in tasks:
        if t.get('ID')==ID:
            is_task=True
            tasks.remove(t)
    
    # if task is not in to-do list returns a statement saying so
    if is_task==False:
        print(f"{ID} is not a valid task ID")
        return

    # updates json file
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
         
def mark_task(ID, mark):
   
    ''' this function changes the status of a task to either to-do in-progress or done

    args: ID (int), mark (string)

    returns: None
    
    '''


    # finds the index of the task to be marked
    index=0
    is_task=False
    for t in range(len(tasks)):
        if tasks[t].get('ID')==ID:
            index=t
            is_task=True

    # if the task is not in the list returns a statement saying so
    if is_task==False:
        print(f'{ID} is not a valid task ID')
        return
    
    # changes the status of the task to the desired status
    if mark=='in-progress':
        tasks[index]['status']='in-progress'
    if mark=='to-do':
        tasks[index]['status']='to-do'
    if mark=='done':
        tasks[index]['status']='done'

    # if the new status is not a valid status returns a statement saying so
    if mark!='in-progress' and mark!='done' and mark!='to-do':
        print(f'{mark} is not an accepted status')
        return
    # saves update to json file
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file,indent=4)


def update_task(ID,update):

    ''' this function can update the task name to something different

    args: ID (int), update (string)

    returns: None

    '''
    # finds the index of the task to be updated
    index=0
    is_task=False
    for t in range(len(tasks)):
        if tasks[t].get('ID')==ID:
            index=t
            is_task=True

    
    # if task is not in to-do list returns a statement saying so
    if is_task==False:
        print(f'{ID} is not a valid task ID')
        return
    
    # updates the task as well as the last updated time
    tasks[index]['task']=update
    tasks[index]['updatedAt']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # saves the change to the json file
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file,indent=4)

    
def list_tasks(status=None):
    ''' this fnction lists tasks according to their status or can list all tasks

    args: status (string or None)

    returns: Tasks (string), ID (int)
    
    
    '''

    
    count=0
    
    # if the status passed is not an accepted input returns a statement saying so
    if status!='to-do' and status!= 'in-progress' and status!='done' and status!='None':
        print(f'{status} is not a valid status')
        return
    
    # if there are no tasks in to-do list returns a statement saying so
    if len(tasks)==0:
        print('There are no tasks in this to-do list')

    # lists tasks by status
    # if there are no tasks with the stats returns a statement saying so
    if status!='None':
        for t in range(len(tasks)):
            if tasks[t].get('status')==status:
                print(tasks[t]['task'],tasks[t]['ID'])
                count+=1
        if count==0:
            print(f'There are no tasks {status}')

    # if no status was passed function just lists all tasks   
    else:
        for t in range(len(tasks)):
            print(tasks[t]['task'],tasks[t]['ID'])


# tells the program where to find the add function arguments from the command line
# passes function arguments
if sys.argv[1]=='add':
    add_task(sys.argv[2])

# tells the program where to find the delete function arguments from the command line
# passes function arguments
if sys.argv[1]=='delete':
    delete_task(int(sys.argv[2]))

# tells the program where to find the update function arguments from the command line
# passes function arguments
if sys.argv[1]=='update':
    update_task(int(sys.argv[2]),sys.argv[3])

# tells the program where to find the mark function arguments from the command line
# passes function arguments
if sys.argv[1]=='mark':
    mark_task(int(sys.argv[3]),str(sys.argv[2]))

# tells the program where to find the list function arguments from the command line
# passes function arguments
if sys.argv[1]=='list':
    arg3 = sys.argv[2] if len(sys.argv) > 2 else None
    list_tasks(str(arg3))

