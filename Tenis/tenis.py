import tkinter as tk

root = tk.Tk()
root.title('Tenis')
root.geometry('700x350')
root.minsize(700,200)
root.columnconfigure(index=1,weight=2)
root.rowconfigure(index=2, weight=1)

menubar = tk.Menu(root)
root.config(menu=menubar)


#Player UI

player1 = ''
player2 = ''
score = [0,0]

def name1():
    global player1
    player1 = player1_entry.get()
    label_name_1 = tk.Label(text=player1, master=root, font=('',20))
    label_name_1.grid(row=0, column=0, rowspan=2)
    player1_entry.destroy()
    enter1.destroy()
    root.update()
    refresh_socore_label()

def name2():
    global player2
    player2 = player2_entry.get()
    label_name_2 = tk.Label(text=player2, master=root, font=('',20))
    label_name_2.grid(row=0, column=2, rowspan=2)
    player2_entry.destroy()
    enter2.destroy()
    root.update()
    refresh_socore_label()
    
Label_score = tk.Label(root, text=f'{score[0]} : {score[1]}', font=('',32))
Label_score.grid(row=0, column=1, rowspan=3)

player1_entry = tk.Entry(root)
player1_entry.grid(row=0,column=0)
enter1 = tk.Button(text="Potwierdz", master=root, command=name1)
enter1.grid(row=1 ,column=0)

player2_entry = tk.Entry(root)
player2_entry.grid(row=0,column=2)
enter2 = tk.Button(text="Potwierdz", master=root, command=name2)
enter2.grid(row=1,column=2)

#
#everything socre related
#

def serve_calculator(n):
    global player1, player2
    if n % 4 in [0,1]:
        return player1
    else:
        return player2
    
def refresh_socore_label():
    Label_score.config(text=f'{score[0]} : {score[1]}')
    label_serve.config(text=f'Serwis:\n{serve_calculator(score[0]+score[1])}')
    
def scored1():
    global score
    score[0] += 1
    refresh_socore_label()
    
def scored2():
    global score
    score[1 ] += 1
    refresh_socore_label()

def descored1():
    global score
    score[0] -= 1
    refresh_socore_label()
    
def descored2():
    global score
    score[1 ] -= 1
    refresh_socore_label()

#Frame for score buttons
Score_buttons = tk.Frame(root)
Score_buttons.grid(row=4, column=0, columnspan=3)

#remove score buttons
score_menu = tk.Menu(menubar, tearoff= False)
menubar.add_cascade(label="Wynik", menu=score_menu)
score_menu.add_command(label="-1 gracz 1 (po lewej)", command=descored1)
score_menu.add_command(label="-1 gracz 2 (po prawej)", command=descored2)

#add score buttons
score1 = tk.Button(text='Player 1', master=Score_buttons, width= 50, height=10, command=scored1)
score1.grid(row=0,column=0)

score2 = tk.Button(text='Player 2', master=Score_buttons, width= 50, height=10, command=scored2)
score2.grid(row=0,column=1)


#Serve buttons
#

label_serve = tk.Label(root, text = f'Serwis:\n{serve_calculator(score[0]+score[1])}')
label_serve.grid(row=3, column=1)


while root.state() != 'closed':
  root.update()
  root.update_idletasks()
exit()