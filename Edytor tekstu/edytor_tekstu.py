#import needed 
import tkinter as tk
import sqlite3 as sq
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox
from tkinter import PhotoImage 
from functools import partial
import PIL
import PIL.Image
import PIL.ImageDraw
import PIL.ImageGrab

#hard setup
font_name='Arial'
font_size=10

#main window options
root = tk.Tk()
root.title('Edytor txtxtxtxttxtt')
root.geometry('500x350')
root.minsize(300,200)

txt = tk.Text(root,bg = "light cyan", font=20)  
txt.place(x = 20, y =20, height = root.winfo_height()-40, width = root.winfo_width()-40)
txt.insert(tk.END, 'TESTTTTTTTTTTTTTTTTTTTTTS') 

#create pop message window
def pop_message(s = 'error'):
  #set up window
  popup = tk.Tk()
  popup.title('Wiadomość')
  popup.minsize(400,400)
  popup.update()
  #message creation
  txt_mssg = tk.Text(popup, border=0, font=10, )
  txt_mssg.place(x = 2, y =2, height = popup.winfo_height()-60, width = popup.winfo_width()-4)
  txt_mssg.insert(tk.END, s)
  #button creation
  butt = tk.Button(popup, bg = "light cyan", font=30, text='OK', command=popup.destroy)
  butt.place(x=20, y=popup.winfo_height()-50 )
  popup.mainloop()


#create table window
def table_window(size_y=5, size_x=5):
  board = []
  def add_column():
    nonlocal size_x
    for y in range(size_y):
      t = tk.Entry(table)
      board[y].append(t)
      t.grid(row=y, column=size_x)
    frame_col.grid(row=0, column=size_x+1)
    size_x += 1
    table.update()
  
  def add_row():
    nonlocal size_y
    row = []
    for x in range(size_x):
      t = tk.Entry(table)
      row.append(t)
      t.grid(row=size_y, column=x)
    board.append(row)
    frame_row.grid(column=0, row=size_y+1)
    size_y += 1
    table.update()
    
  def remove_column():
    nonlocal size_x
    for y in range(size_y):
      board[y][-1].destroy()
      del board[y][-1]
    frame_col.grid(row=0, column=size_x-1)
    size_x -= 1
    table.update()
    
  def remove_row():
    nonlocal size_y
    for x in range(size_x):
      board[-1][x].destroy()
    del board[-1]
    frame_row.grid(row=size_y-1, column=0) 
    size_y -= 1
    table.update()
  
  def export_as_csv():
    tk.Tk().withdraw()
    file_path = fd.asksaveasfilename(defaultextension=".csv", filetypes=[("Comma-separated values", "*.csv"), ("All files", "*.*")])
    file = open(file_path, 'w')
    for y in range(size_y):
      for x in range(size_x):
        print(f'{board[y][x].get()};', file=file, end="")
      print(file=file)
    file.close()

  def import_from_csv():
    nonlocal size_x, size_y
    tk.Tk().withdraw()
    file_path = fd.askopenfilename(defaultextension=".csv", filetypes=[("Comma-separated values", "*.csv")])
    file = open(file_path, 'r')
    values = []
    
    for f in file.read().split():
      values.append(f.split(sep=";"))
    height = len(values)
    if height > size_y:
      for i in range(height-size_y):
        add_row()
        
    width = len(values[0])
    if width > size_x:   
      for i in range(width-size_x):
        add_column()
        
    for y in range(size_y):
      for x in range(size_x):
        board[y][x].delete(0,tk.END)
        board[y][x].insert(0,values[y][x])
        
    file.close()
    
  table = tk.Tk()
  table.title('Table')
  table.minsize(400,400)
  table.update()
    
  table_menu = tk.Menu(table)
  table.config(menu=table_menu)
  export_menu = tk.Menu(table)
  table_menu.add_cascade(label="Export", menu=export_menu)
  export_menu.add_command(label="Export as csv", command=export_as_csv)
  import_menu = tk.Menu(table)
  table_menu.add_cascade(label="Import", menu=import_menu)
  import_menu.add_command(label="Import from csv", command=import_from_csv)
  
  for y in range(size_y):
    row = []
    for x in range(size_x):
      t = tk.Entry(table)
      t.grid(row=y, column=x)
      row.append(t)
    board.append(row)
      
  frame_col = tk.Frame(table)
  frame_col.grid(row=0, column=size_x+1, rowspan=2)
  button_col_add = tk.Button(frame_col, text="+", command=add_column)
  button_col_add.grid(row=0, column=0)
  button_col_remove = tk.Button(frame_col, text="-", command=remove_column)
  button_col_remove.grid(row=1, column=0, sticky="S")
  
  frame_row = tk.Frame(table)
  frame_row.grid(row=size_y+1, column=0)
  button_row_add = tk.Button(frame_row, text="+", command=add_row)
  button_row_add.grid(row=0, column=0)
  button_row_remove = tk.Button(frame_row, text="-", command=remove_row)
  button_row_remove.grid(row=0, column=1)  
  table.update()
  
#new file
def NEW_F():
  ask = msgbox.askyesnocancel('Zapis', 'Czy chcesz zapisać obecny plik?')
  if ask:
    SAVE_F()
    txt.delete('1.0',tk.END)
  elif ask == None:
    pass
  else:
    txt.delete('1.0',tk.END)

#open file
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

#safe file
def SAVE_F():
  tk.Tk().withdraw()
  file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
  file = open(file_path, 'w')
  file.write(txt.get('1.0',tk.END))
  file.close()

#run sql code
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

#change font size
def change_size(n):
  global font_name, font_size
  font_size = n
  txt.config(font=(font_name,font_size))
  print(f'test{n}')

#change font color
def change_color(color):
  txt.config(fg=color)

def create_font_size_menu(font_sizes_list = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]): #size_menu = size_menu
  for i in font_sizes_list:
    size_menu.add_command(label=f"{i}", command=partial(change_size, i), font=(font_name, i))

def create_font_color_menu(colors_list=["Blue", "Lime", "Aqua", "Navy", "Green", "Teal", "Maroon", "Purple", "Olive", "Gray", "Silver", "Red", "Fuchsia", "Yellow", "White"]):
  for color in colors_list:
    color_menu.add_command(label=f"{color}", command=partial(change_color, color), foreground = color)

#menubar setup
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=False)

#file menu setup
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label = 'New', command = NEW_F)
file_menu.add_command(label = 'Open', command = OPEN_F)
file_menu.add_command(label = 'Save', command = SAVE_F)

#run sql option
menubar.add_command(label='SQL', command = run_sql)
root.update_idletasks()

#fromat menu
format_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="Format", menu=format_menu)
size_menu = tk.Menu(format_menu)
format_menu.add_cascade(label="Font size", menu=size_menu)
color_menu = tk.Menu(format_menu)
format_menu.add_cascade(label="Color", menu=color_menu)
create_font_size_menu()
create_font_color_menu()

#table menu
menubar.add_command(label='Table', command=table_window)


#some loop that makes it work
while root.state() != 'closed':
  root.update()
  root.update_idletasks()
  try:
    txt.place(height = root.winfo_height()-40, width = root.winfo_width()-40)
  except:
    exit()
exit()