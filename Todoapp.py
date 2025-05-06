Todo_list=[]

#function to add a new task
def add_task():
    task = input("Enter a task:")
    Todo_list.append({"task": task, "Status":"incomplete"})
    print("new task added sucessfully!!\n")



#function to view all tasks
def view_task():
    print("Your Todo list: ")
    if len(Todo_list) == 0:
        print("No incomplete task!")
    else:
        for index, task in enumerate(Todo_list, 1):
            print(f"{index}:{task['task']} - {task['Status']}")
    print("\n")   



# function to remove a task
def remove_task():
    if len(Todo_list) == 0:
       print("List is Empty !!")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(Todo_list):
                removed_task = Todo_list.pop(search_index)
                print(f"task Removed:{removed_task}")
            else:
                print("Invalid task Number.")    

        except ValueError:
            print("Please Enter a Valid Task Number")


#Function to mark as done
def mark_done():
    if len(Todo_list) == 0:
        print("List is Empty!!")
    else:
        try:
            search_index=int(input("Enter the task number that you want to mark as complete:"))-1
            if 0 <= search_index < len(Todo_list):
                Todo_list[search_index]['Status'] = 'done'
                print(f"task {Todo_list [search_index] ['task']} has been marked as done.")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please Enter a Valid task number.")

#function to display a menu
def menu ():
    print("\n------WELCOME TO TODO LIST APPLICATION------")
    while(True):
        print("******Main Menu******")
        print("1. Add a New Task")
        print("2. View all the Task")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")


        choice = input("Enter your Choice:")
        if choice =="1":
            add_task()
        elif choice =="2":
            view_task()
        elif choice =="3":
            remove_task()
        elif choice =="4":
            mark_done()
        elif choice =="5":
            print ("Exiting the Appliction")
            exit()
        else:
            print("Invalid choice!!")

menu()