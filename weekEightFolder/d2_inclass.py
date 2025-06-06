# **Demonstration: Bind Return key to a function**

# import tkinter as tk

# # Create the main application window
# root = tk.Tk()
# root.title("Event Binding")         # Set the title of the window
# root.geometry("300x200")            # Set the window size

# # Create a StringVar to store the user's input
# entry_var = tk.StringVar()

# # Create an Entry widget where the user can type text
# entry = tk.Entry(root, textvariable=entry_var)
# entry.pack(pady=10)                 # Add padding for better spacing

# # Create a Label to display output messages
# output_label = tk.Label(root, text="Type something and press Enter")
# output_label.pack(pady=5)

# # Define a function to run when the user presses the Enter key
# def on_enter(event):
#     text = entry_var.get()                        # Get the input from the Entry
#     output_label.config(text=f"You typed: {text}")# Update the Label with the input

# # Bind the <Return> (Enter key) event to the Entry widget
# entry.bind("<Return>", on_enter)

# # Additional example: Clear the entry when the user presses Escape
# def on_escape(event):
#     entry_var.set("")                                   # Clear the input field
#     output_label.config(text="Input cleared!")          # Notify the user

# entry.bind("<Escape>", on_escape)

# # Additional example: Display a message when the mouse enters the Entry box
# def on_hover(event):
#     output_label.config(text="You're hovering over the input!")

# entry.bind("<Enter>", on_hover)

# # Additional example: Reset the message when the mouse leaves the Entry box
# def on_leave(event):
#     output_label.config(text="Type something and press Enter")

# entry.bind("<Leave>", on_leave)

# # Run the application's main event loop
# root.mainloop()



# **Demonstration: Change color on mouse hover**

# import tkinter as tk

# # Create the main application window
# root = tk.Tk()
# root.title("Mouse Events")          # Set the window title
# root.geometry("300x200")            # Set the window size (width x height)

# # Create a Label widget with initial text and font styling
# label = tk.Label(
#     root, 
#     text="Hover over me!", 
#     font=("Arial", 14)
# )
# label.pack(pady=30)      # Place the Label in the window with padding

# # Define a function that runs when the mouse enters the label
# def on_enter(event):
#     label.config(fg="blue")         # Change the text color to blue
#     label.config(text="You're hovering!")  # Optional: change the label text

# # Define a function that runs when the mouse leaves the label
# def on_leave(event):
#     label.config(fg="black")        # Reset the text color to black
#     label.config(text="Hover over me!")    # Reset the label text

# # Bind mouse enter and leave events to the label
# label.bind("<Enter>", on_enter)# When the mouse enters the label area
# label.bind("<Leave>", on_leave)# When the mouse leaves the label area

# # BONUS: You can also respond to clicks on the label
# def on_click(event):
#     label.config(text="Label clicked!", fg="green")

# label.bind("<Button-1>", on_click)  # Left mouse click triggers the on_click function

# # Start the Tkinter event loop (keeps the window open and responsive)
# root.mainloop()



