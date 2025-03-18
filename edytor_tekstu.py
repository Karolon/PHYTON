import tkinter as tk
import sqlite3 as sq
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox

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



while root.state() != 'closed':
  root.update()
  root.update_idletasks()
  try:
    txt.place(height = root.winfo_height()-40, width = root.winfo_width()-40)
  except:
    exit()
exit()