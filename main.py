import json
import argparse
import os
import datetime


def get_time():
    now = datetime.datetime.now()
    return str(now.strftime("%B %d, %Y %I:%M %p"))

def read_json():
    if os.path.exists("task.json"):
        try:
            with open("task.json", "r") as file:
                file_size = os.path.getsize("task.json")
                if file_size == 0:
                    return None
                else: 
                    return json.load(file)
        except json.JSONDecodeError:
            print("""Error with decoding task.json, please check for missing/invalid brackets or commas \nbelow is an example of the integrity of the json structure: 
{
    "1": {
        "task": "test",
        "description": "Add a description",
        "progress": "todo",
        "created on": "March 15, 2025 06:54 PM",
        "updated on": ""
    }
}""")
            return {}
    else:
        return {}

def create_task(name, description, progress):
    
    if progress != "done":
        task = {"task": name, "description": description, "progress": progress, "created on": get_time(), "updated on": ""}
        return task
    else: 
        print("Invalid parameter")
        return None

def append_task_to_json(new_task):
    init_id = 1
    #create a task.json if file doesn't exist 
    if not os.path.exists("task.json"):
        initial_task = {f"{init_id}": new_task}
        with open("task.json", "w") as file:
            json.dump(initial_task, file, indent=4)
    else:
        if new_task is not None:
            curr_task_list = read_json()
            #for loop to create gapless id
            for id in curr_task_list:
                if int(id) == init_id:
                    init_id+=1
                else:
                    break
            curr_task_list[f"{init_id}"] = new_task
            curr_task_list = dict(sorted(curr_task_list.items()))
            with open("task.json", "w") as file:
                json.dump(curr_task_list, file, indent=4)
        else: 
            print("No task created")
    print(f"""Created Task {init_id}:
        Task: {new_task['task']}
        Description: {new_task['description']}
        Progress: {new_task['progress']}
        Created on: {new_task['created on']}
        """)    
         
def update_task(id, new_task_name):
    curr_task_list = read_json()
    if str(id) in curr_task_list:
        curr_task_list[id]["task"] = new_task_name
        curr_task_list[id]["updated on"] = get_time()
        with open("task.json", "w") as file:
            json.dump(curr_task_list, file, indent=4)

        print(f"""Updated task {id}
            new name: "{new_task_name}"
            on {get_time()}""")
    else:
        print(f"No such task: {id}")
    
def update_task_description(id, new_description):
    curr_task_list = read_json()
    curr_task_list[id]["description"] = new_description
    curr_task_list[id]["updated on"] = get_time()
    with open("task.json", "w") as file:
        json.dump(curr_task_list, file, indent=4)

    print(f"""Updated task \"{curr_task_list[id]["task"]}\":
        new description: "{new_description}"
        on {get_time()}""")
    
    
def update_progress(id, progress_type):
    curr_task_list = read_json()
    #mapping the progress types to a map
    mapping_progress_type = {1: "in-progress", 2: "done", 3:"todo"}
    
    #update the current task list progress with the mapped progress type
    if str(id) in curr_task_list:
        curr_task_list[str(id)]["progress"] = mapping_progress_type.get(progress_type, "todo")
        curr_task_list[str(id)]["updated on"] = get_time()
        with open("task.json", "w") as file:
            json.dump(curr_task_list, file, indent=4)
        print(f"""
                ID: {id}
                ----------------------
                Task:        {curr_task_list[str(id)]['task']}
                Description: {curr_task_list[str(id)]['description']}
                Progress:    {curr_task_list[str(id)]['progress']}
                Created on:  {curr_task_list[str(id)]['created on']}
                Updated on:  {curr_task_list[str(id)]['updated on']}
                """)
    else:
        print(f"There is no task ID: {id}")

    
def list_tasks(id):
    tasks = read_json()
    if not tasks:
        print("No tasks found")
    #utilizing dictionary unpacking
    for task_id, task in tasks.items():
        if id == -1 or task["progress"] == id:
            print(f"""
            ID: {task_id}
            ----------------------
            Task:        {task['task']}
            Description: {task['description']}
            Progress:    {task['progress']}
            Created on:  {task['created on']}
            Updated on:  {task['updated on']}
            """)
            
def test():
    curr_task_list = read_json()
    print(curr_task_list["1"])
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--create", nargs="+", 
                        metavar=("[Name]", "Description"),
                        type=str, 
                        help="create a task enclose in quotes")
    
    parser.add_argument("--list", 
                        nargs="?", 
                        const=-1, type=str, 
                        help="--list or --list [PROGRESS]") 
    parser.add_argument("--update", 
                        nargs=2, 
                        metavar=("[ID]", "[New Name]"), type=str, 
                        help="Update task name")
    
    
    parser.add_argument("--update-d","--updatedescription",
                        nargs=2, 
                        metavar=("[ID]", "[New Description]"), type=str, 
                        help="Update descriptions")
    
    parser.add_argument("--mip", "--mark-in-progress", 
                        nargs=1, 
                        metavar=("[ID]"), type=int, 
                        help="Update progress as in progress")
    parser.add_argument("--md", "--mark-done", 
                        nargs=1, 
                        metavar=("[ID]"), type=int, 
                        help="Update progress as done")
    parser.add_argument("--mtodo","--mark-todo", 
                        nargs=1, 
                        metavar=("[ID]"), type=int, 
                        help="Update progress as todo")
    
    
    
    parser.add_argument("--delete", nargs=1, metavar=("[ID]"), type=int, help="delete a task with ID")
    
    args = parser.parse_args()
    
    if args.list:
        list_tasks(args.list)
        
            
    if args.create:
        name = args.create[0]
        description = args.create[1] if len(args.create) > 1 else "Add a description"
        progress = args.create[2] if len(args.create) > 2 else "todo"
        task = create_task(name, description, progress)
        append_task_to_json(task)
            
    if args.update:
        update_task(args.update[0], args.update[1])
        
    if args.update_d:
        update_task_description(args.update_d[0], args.update_d[1])
        
        
    if args.mip:
        update_progress(args.mip[0], 1)
    elif args.md:
        update_progress(args.md[0], 2)
    elif args.mtodo:
        update_progress(args.mtodo[0], 3)
        
    if args.delete:
        curr_task_list = read_json()
        id = args.delete[0]
        if str(id) in curr_task_list:
            del curr_task_list[str(id)] 
            with open("task.json", "w") as file:
                json.dump(curr_task_list, file, indent=4)
        else: 
            print(f"There is no task at ID: {id}")
if __name__ == "__main__":
    main()
        
    
        
