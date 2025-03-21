import tkinter as tk
import sqlite3 as sq
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox
from tkinter import PhotoImage 
from functools import partial
import PIL
import PIL.Image
import PIL.ImageGrab

font_name='Arial'
font_size=10
#window options
root = tk.Tk()
root.title('Edytor txtxtxtxttxtt')
root.geometry('500x350')
root.minsize(300,200)

txt = tk.Text(root,bg = "light cyan", font=20)
txt.place(x = 20, y =20, height = root.winfo_height()-40, width = root.winfo_width()-40)
txt.insert(tk.END, 'TESTTTTTTTTTTTTTTTTTTTTTS') 

def pop_message(s = 'error'):
  popup = tk.Tk()
  popup.title('Wiadomość')
  popup.minsize(400,400)
  popup.update()
  txt_mssg = tk.Text(popup, border=0, font=10, )
  txt_mssg.place(x = 2, y =2, height = popup.winfo_height()-60, width = popup.winfo_width()-4)
  txt_mssg.insert(tk.END, s)
  butt = tk.Button(popup, bg = "light cyan", font=30, text='OK', command=popup.destroy)
  butt.place(x=20, y=popup.winfo_height()-50 )
  popup.mainloop()

def NEW_F():
  ask = msgbox.askyesnocancel('Zapis', 'Czy chcesz zapisać obecny plik?')
  if ask:
    SAVE_F()
    txt.delete('1.0',tk.END)
  elif ask == None:
    pass
  else:
    txt.delete('1.0',tk.END)
  
def OPEN_F():
  def openFile():
    tk.Tk().withdraw()
    file_path = fd.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    file = open(file_path, 'r')
    txt.delete('1.0',tk.END)  
    txt.insert(tk.END, file.read())
    file.close()
  ask = msgbox.askyesnocancel('Zapis', 'Czy chcesz zapisać obecny plik?')
  if ask:
    SAVE_F()
    openFile()
  elif ask == None:
    pass
  else:
    openFile()

def SAVE_F():
  tk.Tk().withdraw()
  file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
  file = open(file_path, 'w')
  file.write(txt.get('1.0',tk.END))
  file.close()

def run_sql():
  connect_sql = sq.connect('txt.db') 
  cursor = connect_sql.cursor()

  def execute_sql(s = str()):
    try:
      for cmd in s.split(';'):
        cursor.execute(cmd)
      connect_sql.commit()
    except sq.OperationalError as err:
      pop_message(err)

  if txt.tag_ranges('sel'):
    execute_sql(txt.selection_get())
  else:
    execute_sql(txt.get('1.0',tk.END))

  message = cursor.fetchall()
  if len(message) > 0:
    pop_message(message)

  connect_sql.commit()

def change_size(n):
  global font_name, font_size
  font_size = n
  txt.config(font=(font_name,font_size))
  print(f'test{n}')

def change_color(color):
  txt.config(fg=color)


#menu setup
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label = 'New', command = NEW_F)
file_menu.add_command(label = 'Open', command = OPEN_F)
file_menu.add_command(label = 'Save', command = SAVE_F)

menubar.add_command(label='SQL', command = run_sql)
root.update_idletasks()

format_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Format", menu=format_menu)
size_menu = tk.Menu(format_menu)
format_menu.add_cascade(label="Font size", menu=size_menu)
color_menu = tk.Menu(format_menu)
format_menu.add_cascade(label="Color", menu=color_menu)

font_sizes_list = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
for i in font_sizes_list:
  size_menu.add_command(label=f"{i}", command=partial(change_size, i), font=(font_name, i))

canva = tk.Canvas(root, height=15, width=15)
canva.create_oval(5, 5, 15, 15, fill='black')
canva.place(x=0, y=0)
canva.pack()
img = PIL.ImageGrab.grab(bbox=(canva.winfo_rootx(),canva.winfo_rooty(),canva.winfo_rootx() + canva.winfo_width(),canva.winfo_rooty() + canva.winfo_height()))
img.save("img.png")

colors_list=["Blue", "Lime", "Aqua", "Navy", "Green", "Teal", "Maroon", "Purple", "Olive", "Gray", "Silver", "Red", "Fuchsia", "Yellow", "White"]
#for c in colors_list:
  #color_menu.add_command(label=f"{c}", command=partial(change_color, c), image=img)




while root.state() != 'closed':
  root.update()
  root.update_idletasks()
  try:
    txt.place(height = root.winfo_height()-40, width = root.winfo_width()-40)
  except:
    exit()
exit()