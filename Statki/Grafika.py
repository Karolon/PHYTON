import tkinter as tk

root = tk.Tk()
root.title('Fajny program')
root.geometry('500x350')
root.minsize(300, 200)
root.maxsize(1000,700)

icon_shot = 'X'
icon_water = ' '
icon_miss = 'x'

label_1 = tk.Label(root, text='Input word:')
label_1.place(x=50, y=50)

entry_1 = tk.Entry(root, width=50)
entry_1.place(x=50, y=70)

label_2 = tk.Label(root, text='Input key:')
label_2.place(x=50, y=100)

entry_2 = tk.Entry(root, width=50)
entry_2.place(x=50, y=120)


def button_sypher_clicked():
  pass


def button_desypher_clicked():
  pass




button_1 = tk.Button(root, width=0, text=icon_water, command=button_sypher_clicked)
button_1.place(x=50, y=150)

button_1 = tk.Button(root, width=2, text=icon_water, command=button_desypher_clicked, height=1)
button_1.place(x=140, y=150)
button_1.config(text='x')
print(button_1)


root.mainloop()
