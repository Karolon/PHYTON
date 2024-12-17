import tkinter as tk

root = tk.Tk()
root.title('Fajny program')
root.geometry('500x350')
root.minsize(300,200)
root.maxsize(1000,700)
    
def sypher_cesar(password, key):
  key = key % 26
  syphon = ''
  for letter in password:
    letter_number = ord(letter.upper()) + key
    if letter_number > 90:
      letter_number -= 26
    if letter.isupper():
      syphon += chr(letter_number)
    else:
      syphon += chr(letter_number).lower()
  return syphon


def desypher_cesar(syphon, key):
  key = key % 26
  password = ''
  for letter in syphon:
    letter_number = ord(letter.upper()) - key
    if letter_number < 65:
      letter_number += 26
    if letter.isupper():
      password += chr(letter_number)
    else:
      password += chr(letter_number).lower()
  return password


def veneger_sypher(word, key):
  sy = ''
  for i in range(len(word)):
    sy += sypher_cesar(word[i], ord(key.upper()) - ord('A'))
  return sy

label_1 = tk.Label(root, text='Input word:')
label_1.place(x=50, y=50)

entry_1 = tk.Entry(root, width = 50)
entry_1.place(x=50, y=70)

label_2 = tk.Label(root, text='Input key:')
label_2.place(x=50, y=100)

entry_2 = tk.Entry(root, width = 50)
entry_2.place(x=50, y=120)

def button_sypher_clicked():
    word = entry_1.get()
    key = entry_2.get()
    if key.isnumeric():
        key = int(key)
        sypher = sypher_cesar(word, key)
    else:
        sypher = veneger_sypher(word, key)
    label_3.config(text=sypher)

def button_desypher_clicked():
    pass

button_1 = tk.Button(root, width=0, text='Sypher', command = button_sypher_clicked)
button_1.place(x=50, y=150)

button_1 = tk.Button(root, width=0, text='Desypher', command = button_desypher_clicked)
button_1.place(x=140, y=150)

label_3 = tk.Label(root, text='')
label_3.place(x=50, y=180)

root.mainloop()

