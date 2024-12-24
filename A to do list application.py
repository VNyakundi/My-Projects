def display_tasks(tasks):
    print("\n your to do list: ")

    for index, task in enumerate(tasks, 1):
        print(f"{index}.{task['task']} - {'done' if task['done']else ['not done']}")
        print("\n")

def add_task(tasks,task):
    tasks.append({'task':task, 'done':False})

def mark_task_done(tasks,task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True

    else:
        print('invalid task number')

def save_tasks_to_file(tasks, filename = 'tasks.txt'):
    with open (filename,'w') as f:
        for task in tasks:
            f.write(f"{task['task']}|{task['done']}\n")

def load_tasks_from_file(filename = 'tasks.txt'):
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                task,done = line.strip().split('|')
                tasks.append({'task':task,'done':done=='True'})

    except FileNotFoundError:
        pass # No tasks yet so its okay
    return tasks

def main():
    tasks = load_tasks_from_file()

    while True:
        print("\n1.view tasks")
        print("2.add a task")
        print("3.mark task as done")
        print("4.exit")

        choice = input("choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == "2":
            task = input('enter a task: ')
            add_task(tasks,task)
            save_tasks_to_file(tasks)
        elif choice == "3":
            task_number = int(input("enter task number to mark as done: "))
            mark_task_done(task,task_number)
            save_tasks_to_file(tasks)
        elif choice == '4':
            print("goodbye")
            break
        else:
            print("invalid option, please try again")


if __name__ == "__main__":
    main()





    