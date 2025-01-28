import tkinter as tk

#window options
root = tk.Tk()
root.title('Edytor txtxtxtxttxtt')
root.geometry('500x350')
root.minsize(300,200)
    
t = tk.Text(root,bg = "light cyan", font=20)
t.place(x = 20, y =20, height = root.winfo_height()-40, width = root.winfo_width()-40)
t.insert(tk.END, 'TESTTTTTTTTTTTTTTTTTTTTTS')

def NEW():
  t.delete('1.0',tk.END)  
  
def test():
  print(t.index())
  
#menu setup
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label = 'New', command = NEW)
file_menu.add_command(label = 'Open', command = test)
file_menu.add_command(label = 'Save', command = lambda : print(3))
root.update_idletasks()




while root.state() != 'closed':
  root.update()
  root.update_idletasks()
  t.place(height = root.winfo_height()-40, width = root.winfo_width()-40)
  