
#!/usr/bin/env python3

import sys
import json
import os
from datetime import datetime




if os.path.exists('tasks.json'):
    
    with open("tasks.json", 'r') as file:
        try:
            tasks=json.load(file)
        except json.JSONDecodeError:
            tasks=[]
else:
    tasks=[]


def add_task(task):
    for t in tasks:
        if t.get('task')==task:
            print(f'{task} is already in to-do list')
            return

    tasks.append({'task':task,'status':'to-do','ID':len(tasks)+1,'createdAt':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'updatedAt':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
        print(f'{task} successfully added ID:{len(tasks)}')

def delete_task(ID):
    is_task=False

    for t in tasks:
        if t.get('ID')==ID:
            is_task=True
            tasks.remove(t)
    
    if is_task==False:
        print(f"{ID} is not a valid task ID")
        return

    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
         
def mark_task(ID, mark):
    index=0
    is_task=False
    for t in range(len(tasks)):
        if tasks[t].get('ID')==ID:
            index=t
            is_task=True
    if is_task==False:
        print(f'{ID} is not a valid task ID')
        return
    if mark=='in-progress':
        tasks[index]['status']='in-progress'
    if mark=='to-do':
        tasks[index]['status']='to-do'
    if mark=='done':
        tasks[index]['status']='done'
    if mark!='in-progress' and mark!='done' and mark!='to-do':
        print(f'{mark} is not an accepted status')
        return
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file,indent=4)


def update_task(ID,update):
    index=0
    is_task=False
    for t in range(len(tasks)):
        if tasks[t].get('ID')==ID:
            index=t
            is_task=True

    if is_task==False:
        print(f'{ID} is not a valid task ID')
        return
    
    tasks[index]['task']=update
    tasks[index]['updatedAt']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file,indent=4)

    
def list_tasks(status=None):
    count=0
    
    if status!='to-do' and status!= 'in-progress' and status!='done' and status!='None':
        print(f'{status} is not a valid status')
        return
    if len(tasks)==0:
        print('There are no tasks in this to-do list')

    if status!='None':
        for t in range(len(tasks)):
            if tasks[t].get('status')==status:
                print(tasks[t]['task'],tasks[t]['ID'])
                count+=1
        if count==0:
            print(f'There are no tasks {status}')
        
    else:
        for t in range(len(tasks)):
            print(tasks[t]['task'],tasks[t]['ID'])

if sys.argv[1]=='add':
    add_task(sys.argv[2])

if sys.argv[1]=='delete':
    delete_task(int(sys.argv[2]))

if sys.argv[1]=='update':
    update_task(int(sys.argv[2]),sys.argv[3])

if sys.argv[1]=='mark':
    mark_task(int(sys.argv[3]),str(sys.argv[2]))

if sys.argv[1]=='list':
    arg3 = sys.argv[2] if len(sys.argv) > 2 else None
    list_tasks(str(arg3))

