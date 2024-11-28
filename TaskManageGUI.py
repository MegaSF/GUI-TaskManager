#Evan Rhea
# Task manager but with a new GUI!
import tkinter as GUI



# Start of Functionality

task_list = [("Tasks: ")]

def NewTask():
    NewBoi = NTask.get()
    task_list.append(NewBoi)
    Tasks.config(text=task_list)
    print(task_list)


def DeleteTask():
    DelBoi = DTask.get()
    if DelBoi in task_list:
        task_list.remove(DelBoi)
        Tasks.config(text=task_list)
        print(task_list)

def EditTask():
    def NewEditTask():
            FinalNewTask = AdjustedTask.get()
            task_list.append(FinalNewTask)
            task_list.remove(EdTask)
            Tasks.config(text=task_list)
    EdTask = ETask.get()
    if EdTask in task_list:
        EdIndex = task_list.index(EdTask)
        print(EdIndex)
        AdjustTaskText = GUI.Label(Manager, text="Create a new task to replace original").grid(row=4, column=0)
        AdjustedTask = GUI.Entry(Manager)
        AdjustedTask.grid(row=4, column = 2)
        CreateFinalNewTask = GUI.Button(Manager, text="Generate new task", command=NewEditTask)
        CreateFinalNewTask.grid(row=5,column=1)

# End of functions and functionality      


# Graphical Interface section

Manager = GUI.Tk()

NewButton = GUI.Button(Manager, text="Create New task", command=NewTask)
NewButton.grid(row=0, column=0)

NTask = GUI.Entry(Manager)
NTask.grid(row = 1, column=0)

DeleteButton = GUI.Button(Manager, text="Delete task", command=DeleteTask)
DeleteButton.grid(row=0, column=1)

DTask = GUI.Entry(Manager)
DTask.grid(row = 1, column=1)



EditButton = GUI.Button(Manager, text="Edit task", command=EditTask)
EditButton.grid(row=0, column=2)

ETask = GUI.Entry(Manager)
ETask.grid(row = 1, column=2)

Tasks = GUI.Label(Manager, text=task_list, font='Impact')
Tasks.grid(row=2, column=1)

QuitApplication = GUI.Button(Manager, text="QUIT", command = Manager.destroy)
QuitApplication.grid(row=8, column=1)

Manager.mainloop()