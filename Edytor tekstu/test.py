import tkinter as tk


root = tk.Tk()
root.title('test')
root.geometry('500x350')
root.minsize(300,200)

for y in range(6):
  for x in range(6):
    cell = tk.Entry(root).grid(row=y, column=x)
 
#some loop that makes it work
while root.state() != 'closed':
  root.update()
  root.update_idletasks()