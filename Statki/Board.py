import tkinter as tk
import time  as t

root = tk.Tk()
root.title('Fajny program')
root.geometry('500x350')
root.minsize(300, 200)
root.maxsize(1000,700)



def button_clicked():
  global button_list
  button_list[0][1].config(text = 'w')



def setup_board(sizeY = 10, sizeX = 10, top_left_x = 10, top_left_y= 10):
  global button_list
  button_list=[]
  for y in range(sizeY):
    button_row = []
    for x in range(sizeX):
      #globals()[f"button_{chr(x + 65)+str(y)}"]
      button = tk.Button(root, width=2, height=1, command = button_clicked)
      button.place(x=top_left_x + (25 * x), y=top_left_y + (25 * y))
      button_row.append(button)
    button_list.append(button_row)
    

setup_board()

root.mainloop()