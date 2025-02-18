import tkinter as tk
import sqlite3 as sq

#window options
root = tk.Tk()
root.title('Edytor txtxtxtxttxtt')
root.geometry('500x350')
root.minsize(300,200)
    
txt = tk.Text(root,bg = "light cyan", font=20)
txt.place(x = 20, y =20, height = root.winfo_height()-40, width = root.winfo_width()-40)
txt.insert(tk.END, 'TESTTTTTTTTTTTTTTTTTTTTTS') 

def NEW():
  txt.delete('1.0',tk.END)  
  
def test():
  print(txt.index())

def run_sql():
  connect_sql = sq.connect('txt.db') 
  cursor = connect_sql.cursor()

  def execute_sql(s = str()):
    try:
      for cmd in s.split(';'):
        cursor.execute(cmd)
      connect_sql.commit()
    except sq.OperationalError as err:
      print(err)

  if txt.tag_ranges('sel'):
    execute_sql(txt.selection_get())
  else:
    execute_sql(txt.get('1.0',tk.END))


#menu setup
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label = 'New', command = NEW)
file_menu.add_command(label = 'Open', command = test)
file_menu.add_command(label = 'Save', command = lambda : print(3))

menubar.add_command(label='SQL', command = run_sql)
root.update_idletasks()



while root.state() != 'closed':
  root.update()
  root.update_idletasks()
  txt.place(height = root.winfo_height()-40, width = root.winfo_width()-40)
  