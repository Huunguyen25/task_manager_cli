# Task Manager CLI Program
## Overview
This Python script provides a command-line interface (CLI) for managing tasks stored in a JSON file (`task.json`). It allows users to create, update, list, and delete tasks while maintaining timestamps.


## File Structure
- **`task.json`**: Stores task data in JSON format.

## How to use the program
*
   ```bash
   cd task_manager_cli/
   ```
   ### create a virtual environment 
   ```bash
   python -m venv env
   Windows
   source env/Scripts/activate.bat

   Other
   source env/bin/activate
   ```
   ```bash
   python main.py -h
   ```
   #### Example of usage: [Usage section](#usage)
---


## Command-Line Arguments
| Argument | Parameters | Description |
|----------|-----------|-------------|
| `--create` | `"[Name]" "[Description]" "[Progress]"` | Creates a new task. Defaults to `"todo"` if progress is unspecified. |
| `--list` | `[PROGRESS]` | Lists all tasks or tasks matching a progress status. |
| `--update` | `"[ID]" "[New Name]"` | Updates a task name. |
| `--update-d` / `--updatedescription` | `"[ID]" "[New Description]"` | Updates a task description. |
| `--mip` / `--mark-in-progress` | `"[ID]"` | Marks a task as `"in-progress"`. |
| `--md` / `--mark-done` | `"[ID]"` | Marks a task as `"done"`. |
| `--mtodo` / `--mark-todo` | `"[ID]"` | Marks a task as `"todo"`. |
| `--delete` | `"[ID]"` | Deletes a task by its ID. |

---


## Usage:
* ### Creating a task with and without description
   ```bash
   $ python main.py --create "Do Chores"
    Created Task 1:
        Task: Do Chores
        Description: Add a description     
        Progress: todo
        Created on: March 15, 2025 06:04 PM

   $ python main.py --create "Do Chores" "Do the dishes, and do the laundry"
    Created Task 1:
        Task: Do Chores
        Description: Do the dishes, and do the laundry
        Progress: todo
        Created on: March 15, 2025 06:05 PM
   ```
* ### Update a task name and description
    ```bash
    --update

    $ python main.py --update 1 "Do homework"
    Updated task 1
        new name: "Do homework"
        on March 15, 2025 06:06 PM

    --update-d

    $ python main.py --update-d 1 "Finish stats homework"
    Updated task "Do homework":
        new description: "Finish stats homework"
        on March 15, 2025 06:07 PM
    ```

* ### Listing tasks
    #### Listing with no parameter
    ```bash
    $ python main.py --list

            Task 1
            ----------------------
            Task:        Do homework
            Description: Finish stats homework
            Progress:    in-progress
            Created on:  March 15, 2025 06:05 PM
            Updated on:  March 15, 2025 06:11 PM


            Task 2
            ----------------------
            Task:        Do chores
            Description: Do the dishes
            Progress:    todo
            Created on:  March 15, 2025 06:10 PM
            Updated on:
    ```
    #### Listing with parameters

    ```bash
        $ python main.py --list in-progress
            Task 1
            ----------------------
            Task:        Do homework
            Description: Finish stats homework  
            Progress:    in-progress
            Created on:  March 15, 2025 06:05 PM
            Updated on:  March 15, 2025 06:11 PM
    ```
* ### Update progress
    ```bash 
    $ python main.py --mark-in-progress 1
            Task Do homework
            ----------------------
            Task:        Do homework
            Description: Finish stats homework  
            Progress:    in-progress
            Created on:  March 15, 2025 06:05 PM
            Updated on:  March 15, 2025 06:20 PM

    $ python main.py --mark-todo 1
            Task Do homework
            ----------------------
            Task:        Do homework
            Description: Finish stats homework  
            Progress:    todo
            Created on:  March 15, 2025 06:05 PM
            Updated on:  March 15, 2025 06:20 PM

    $ python main.py --mark-done 1
            Task Do homework
            ----------------------
            Task:        Do homework
            Description: Finish stats homework
            Progress:    done
            Created on:  March 15, 2025 06:05 PM
            Updated on:  March 15, 2025 06:21 PM

* ### delete
    ```bash
    $ python main.py --delete 1
    ```

## Functions

### Utility Functions
- **`get_time()`**  
  - Returns the current date and time in a readable format.

- **`read_json()`**  
  - Reads `task.json` and returns its content as a dictionary.
  - Returns an empty dictionary if the file does not exist.

### Task Management Functions
- **`create_task(name, description, progress)`**  
  - Creates a new task dictionary with a name, description, and progress status.
  - Ensures the `progress` parameter is not set to `"done"` initially.

- **`append_task_to_json(new_task)`**  
  - Adds a new task to `task.json`, ensuring a gapless ID sequence.
  - If the file doesn’t exist, it creates a new JSON file.

- **`update_task(id, new_task_name)`**  
  - Updates the task name by its ID and records the update time.

- **`update_task_description(id, new_description)`**  
  - Updates the task description and records the update time.

- **`update_progress(id, progress_type)`**  
  - Changes a task’s progress status using a mapped integer value:
    - `1`: `"in-progress"`
    - `2`: `"done"`
    - `3`: `"todo"`

- **`list_tasks(id)`**  
  - Lists all tasks if `id = -1`.
  - Lists tasks filtered by a specific progress type if `id` matches a progress state.

- **`main()`**  
  - Parses CLI arguments and calls appropriate functions.

---
