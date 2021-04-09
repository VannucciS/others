from tkinter import *

root = Tk()

# Make the buttons works

def myClick():
	myLabel = Label(root, text='Look! I clicked a button!')
	myLabel.pack()

# Create buttons

myButton = Button(root, text='Click me', padx=50, pady=50, command = myClick, fg = 'blue', bg = 'yellow')
myButton.pack()

root.mainloop()
