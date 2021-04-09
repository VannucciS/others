from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text = 'hello world!').grid(row=0, column=0)
myLabel2 = Label(root, text = 'Hello sky!').grid(row=1, column=91)

# Showing it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=91)

root.mainloop()
