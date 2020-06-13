from tkinter import *

def finish():
    root.destory()
def show():
    s1 = e1.get()
    s2 = e2.get()
    s3 = s1+" "+s2
    e3.insert(0,s3)
root = Tk()

l1 = Label(root, text = "First name: ")
l2 = Label(root, text = "Last name: ")
l3 = Label(root, width = 30, text = "Full name: ")

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

b1 = Button(root, text= "Show", command = show)
b2 = Button(root, text = "quit", command = finish)

l1.grid(row = 0,  column = 0)
l2.grid(row = 1,  column = 0)
e1.grid(row = 0,  column = 1)
e2.grid(row = 1,  column = 1)
l3.grid(row = 2,  column = 0)
e3.grid(row = 2,  column = 1)
b1.grid(row = 3,  column = 0)
b2.grid(row = 3,  column = 1)
root.mainloop()