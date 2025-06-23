

import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry('500x500')

inputVar = tk.StringVar()
outputVar = tk.StringVar()
selected_index = None  # to keep track of which item is being edited

# --- Input Label & Entry ---
inputLabel = tk.Label(root, text='Please enter a todo:')
inputLabel.pack(pady=5)

inputEntry = tk.Entry(root, textvariable=inputVar)
inputEntry.pack(pady=5)

# --- Output Label for feedback ---
resultLabel = tk.Label(root, textvariable=outputVar, font=('arial', 12))
resultLabel.pack(pady=5)

# --- To-Do Listbox ---
toDoList = tk.Listbox(root, width=40, height=10)
toDoList.pack(pady=10)


# --- Function to Add a Task ---
def addTodo():
    user_input = inputVar.get()
    if user_input:
        toDoList.insert(tk.END, user_input)
        inputVar.set('')
        outputVar.set("Todo added!")
    else:
        outputVar.set("Please enter a task.")


# --- Function to Delete Selected Task ---
def deleteToDo():
    selected = toDoList.curselection()
    if selected:
        toDoList.delete(selected[0])
        outputVar.set("Todo deleted.")
    else:
        outputVar.set("Please select a task to delete.")


# --- Function to Start Editing a Task ---
def editTodo():
    global selected_index
    selected = toDoList.curselection()
    if selected:
        selected_index = selected[0]
        current_text = toDoList.get(selected_index)
        inputVar.set(current_text)
        outputVar.set("Now editing selected task.")
    else:
        outputVar.set("Please select a task to edit.")


# --- Function to Update Edited Task ---
def updateTodo():
    global selected_index
    new_text = inputVar.get()
    if new_text and selected_index is not None:
        toDoList.delete(selected_index)
        toDoList.insert(selected_index, new_text)
        inputVar.set("")
        outputVar.set("Todo updated!")
        selected_index = None
    else:
        outputVar.set("Nothing to update.")


# --- Function to Clear All Tasks ---
def clearAll():
    toDoList.delete(0, tk.END)
    inputVar.set("")
    outputVar.set("All todos cleared.")


# --- Buttons ---
addBtn = tk.Button(root, text='Add TODO', command=addTodo)
addBtn.pack(pady=3)

deleteBtn = tk.Button(root, text='Delete TODO', command=deleteToDo)
deleteBtn.pack(pady=3)

editBtn = tk.Button(root, text='Edit Selected', command=editTodo)
editBtn.pack(pady=3)

updateBtn = tk.Button(root, text='Update Selected', command=updateTodo)
updateBtn.pack(pady=3)

clearBtn = tk.Button(root, text='Clear All', command=clearAll)
clearBtn.pack(pady=3)

# --- Run App ---
root.mainloop()

