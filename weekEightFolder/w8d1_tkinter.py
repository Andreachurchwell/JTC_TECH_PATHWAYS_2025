# import tkinter as tk 

# # this code is from a youtube tutorial neuralNine

# root = tk.Tk()

# root.geometry('800x500')
# root.title('GUI Tutorial NeuralNine')

# label = tk.Label(root, text='HelloWorld!', font=('Arial', 18))
# label.pack(padx=20,pady=20)

# textbox = tk.Text(root, height=3,font=('Arial', 16))
# textbox.pack(padx=10,pady=10)

# # button = tk.Button(root, text='CLick Me!', font=('Arial',18))
# # button.pack(padx=10,pady=10)

# # myentry = tk.Entry(root)
# # myentry.pack()

# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonframe, text=1, font=('Arial',18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

# btn2 = tk.Button(buttonframe, text=2, font=('Arial',18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

# btn3 = tk.Button(buttonframe, text=3, font=('Arial',18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

# btn4 = tk.Button(buttonframe, text=4, font=('Arial',18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

# btn5 = tk.Button(buttonframe, text=5, font=('Arial',18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

# btn6 = tk.Button(buttonframe, text=6, font=('Arial',18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# buttonframe.pack(fill='x')

# anotherbutton = tk.Button(root, text='TESt')
# anotherbutton.place(x=200, y=200, height=100,width=100)


# root.mainloop()



import tkinter as tk
from tkinter import messagebox
class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        
        self.filemenu.add_command(label='Close', command=self.onclosing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close Without Question', command=exit)

        self.actionmenu = tk.Menu(self.menubar,tearoff=0)
        self.actionmenu.add_command(label='Show Message', command=self.showMsg)


        self.menubar.add_cascade(menu=self.filemenu,label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')



        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text='YOUR MESSAGE',font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height=5, font=('Arial',16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()


        self.check = tk.Checkbutton(self.root, text='SHOW MESSAGE TEXTBOX', font=('Arial',16), variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text='SHOW MESSAGE',font=('Arial',16), command=self.showMsg)
        self.button.pack()

        self.clearbtn = tk.Button(self.root, text='Clear', font=('Arial',18),command=self.clear)
        self.clearbtn.pack(padx=10,pady=10)


        self.root.protocol('WM_DELETE_WINDOW', self.onclosing)
        self.root.mainloop()

    def showMsg(self):
        # print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self,event):
        # print(event.keysym)
        # print(event.state)
        if event.state == 12 and event.keysym == "Return":
            # print(self.showMsg())
            self.showMsg()

    def onclosing(self):
        # print('Goodbye WOrld')
        if messagebox.askyesno(title='Quit?', message='Really wanna quit?'):

            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0',tk.END)

MyGUI()