import tkinter as tk

root = tk.Tk()
root.title('Edytor txtxtxtxttxtt')
root.geometry('500x350')
root.minsize(300,200)
    
menubar = tk.Menu(root)
x = lambda : print(2)
menubar.add_command(label = 'Otwórz', command = x)

t = tk.Text(root, height = 5, width = 25, bg = "light cyan")
t.place(x = 20, y =20)
t.insert(tk.END, 'TESTTTTTTTTTTTTTTTTTTTTTS')

root.mainloop()