import tkinter as tk

# # create the main window
# root = tk.Tk()
# root.title('Greet Me!')
# root.geometry('300x200')



# # Force window to be on top
# # root.attributes('-topmost', True)
# # define stringVar for input and output
# name_var = tk.StringVar()
# greet_var = tk.StringVar(value='Hello,Friend!')

# # create and pack a label for prompting input
# entry_label = tk.Label(root, text='Enter Your Name:')
# entry_label.pack(pady=5)

# # create and pack the text entry field
# name_entry = tk.Entry(root, textvariable=name_var)
# name_entry.pack()

# # create and pack the output fields
# greeting_label = tk.Label(root, textvariable=greet_var, font=('Arial',14))
# greeting_label.pack(pady=10)

# def greet():
#     name = name_var.get()
#     if name:
#         greet_var.set(f'Hello, {name}!')
#     else:
#         greet_var.set('Hello, Friend!')

# greet_button = tk.Button(root, text='Greet me', command = greet) 
# greet_button.pack(pady=10)

# root.mainloop()




# create the main window
# root = tk.Tk()
# root.title('Simple Calculator: Add 10')
# root.geometry('350x250')

# # define stringvar for user input and output

# inputVar = tk.StringVar()
# outputVar = tk.StringVar()


# # inputs
# inputLabel = tk.Label(root, text='Please enter a number')
# inputLabel.pack(pady=5)

# inputEntry = tk.Entry(root, textvariable=inputVar)
# inputEntry.pack(pady=5)

# # outputs
# resultLabel = tk.Label(root, textvariable=outputVar, font=('Arial',12), fg='blue')
# resultLabel.pack(pady=10)

# # function to add 10
# def addTen():
#     user_input = inputVar.get()

#     try:
#         number = float(user_input)
#         result = number + 10
#         outputVar.set(f'Result: {result}')
#     except ValueError:
#         outputVar.set('Please enter a valid number.')

# # add your button

# addBtn = tk.Button(root, text='Add 10', command=addTen)
# addBtn.pack(pady=5)

# # clear input and output

# def clearFields():
#     inputVar.set('')
#     outputVar.set('')

# clearBtn = tk.Button(root, text='Clear', command=clearFields)
# clearBtn.pack(pady=5)
# root.mainloop()


import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x300")

# Tkinter StringVar variables to hold input
name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
output_var = tk.StringVar()

# Create and place the widgets
tk.Label(root, text="Name:").pack(pady=(10, 0))
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Email:").pack(pady=(10, 0))
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Phone:").pack(pady=(10, 0))
tk.Entry(root, textvariable=phone_var).pack()

# Function to handle Submit
def submit_info():
    name = name_var.get()
    email = email_var.get()
    phone = phone_var.get()
    formatted = f"Name: {name}\nEmail: {email}\nPhone: {phone}"
    output_var.set(formatted)

# Function to Clear fields
def clear_fields():
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    output_var.set("")

# Buttons for submit and clear
tk.Button(root, text="Submit", command=submit_info).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack()

# Label to display output
tk.Label(root, textvariable=output_var, justify="left", font=("Arial", 10), fg="blue").pack(pady=10)

# Run the application
root.mainloop()