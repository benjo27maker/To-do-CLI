print("i'm now gonna make a fire to-do list")

import sys
import json




tasks=[{}]



def add_task(task):
    tasks.append({'task':task,'completed':False})
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)

def delete_task(task):
    for t in tasks:
        if t.get('task')==task:
            tasks.remove(t)
    with open("tasks.json","w") as file:
        json.dump(tasks,file,indent=4)
           
            

#add_task('make a to-do list')

delete_task("make a to-do list")

