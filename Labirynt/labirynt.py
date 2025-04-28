import keyboard as k
import time
import os
import create_labirynth as create
import random as r

#do zmiany↓
ściana = '■'
nieściana='∙'
win = 'x'
postać = '☺'
labirynt_file_save='labirynt_list.txt'
labirynt_file_load='labirynt.txt'
score_file='score1.txt'

#stałe↓
file_score_list = []
miejsce=0
size_x = 0
size_y = 0
x=0
y=0
l_ruch=0
u=0
n=[]

def print_score(): 
  global score_file
  file=open(score_file)
  scoreboard=[]
  for f in file:
    f=f.strip()
    scoreboard.append(f)
  print(*scoreboard,sep='\n')

def load_lab():
  global n, labirynt_file_load, x, y
  nazwa = input("podaj z jakiego pliku załadować labirynt(domyślnie labirynt.txt)")
  if nazwa != '':
    labirynt_file_load = nazwa
  lab_file = open(labirynt_file_load, encoding='UTF-8',mode='r')
  for f in lab_file: #tworzy listę z mapą
    f = f.strip()
    f = f.split()
    #f = f.replace('\n','')
    n.append(f)
  y,x = n[0]
  del n[0]
  gra()

def printlist(n):
  global x,y
  for i in range(len(n)):
    for j in range(len(n[i])):
      if i == y and j == x:
        print(postać, end='')
        print(' ', end='')
      else:
        print(*n[i][j], end='')
        print(' ', end='')
    print()

def check_win(n):
  global x,y
  if n[y][x] == win:
    return(1)

def ruch(n, size_y, size_x):
  global l_ruch, ściana,x,y
  w = k.read_key()
  l_ruch += 1
  while True:
    if w == 'w' and n[y - 1][x] != ściana:
      y -= 1
      if y < 0:
        y = size_y + y
    elif w == 'a' and n[y][x - 1] != ściana:
      x -= 1
      if x < 0:
        x = size_x + x
    elif w == 's' and n[(y + 1) % size_y][x] != ściana:
      y = (y + 1) % size_y
    elif w == 'd' and n[y][(x + 1) % size_x] != ściana:
      x = (x + 1) % size_x
    else:
      break
    os.system('cls')
    printlist(n)
    print(l_ruch)
    time.sleep(0.2)
  time.sleep(0.2)
  return(check_win(n))

def clear_file_score(file_score):
    file_score.close()
    file_score = open(score_file, encoding='UTF-8',mode='w')
    file_score.close()
    
def create_file_score(file_score):
    file_score.close()
    file_score = open(score_file, encoding='UTF-8',mode='a')
    file_score.close()

def save_labirynth(n,file_lab_list,start_y,start_x):  #zapisuje labirynt do pliku
  file = open(file_lab_list, encoding='UTF-8',mode='a')
  print(start_y,start_x,file=file)
  for p in n:
    print(*p,file=file)
  print('',file=file)
  file.close


def gra():
  i=0
  global u, ściana, nieściana, win, postać, score_file, labirynt_file_save, miejsce, n, x, y
  if n == []:
    size_x = int(input('podaj szerokość'))
    size_y = int(input('podaj wysokość'))
    start_x = r.randint(0,size_x-1)
    start_y = r.randint(0,size_y-1)
    x=start_x
    y=start_y
    n = create.create_labirynth(size_x,size_y,ściana,nieściana,win,x,y)
  else:
      size_x = len(n[0])
      size_y = len(n)
  printlist(n)
  czas = time.time()

  while u!=1:   #ruch i cała gra
    u = ruch(n, size_y, size_x)
  cały_czas = int(time.time()- czas) #liczenie czasu

  file_score = open(score_file, encoding='UTF-8',mode='r') #
  wynik = l_ruch * cały_czas #liczenie wyniku
  wynik = int(wynik)

  for f in file_score: #obliczanie zajętego miejsca
    f = f.strip()
    file_score_list.append(f)
    f = f.split()
    if wynik <= int(f[-1]):
      miejsce = i+1
    i += 1
  if miejsce == 0:     #obliczanie zajętego miejsca
    miejsce = i+1

  print('Wygrałeś !','wykonałeś',l_ruch,"ruchów \n i osiągnołeś czas",cały_czas,'s','\n','twój wynik to',wynik,'\n i osiągnołeś',miejsce,"miejsce") #podanie wyniku


  nick=input("podaj nick")         

  file_score_list.insert(miejsce-1, 'Nick: '+nick+' wys: '+str(size_y)+' szer: '+str(size_x)+' wynik: '+str(wynik)) #dodaje miejsce gracza do listy wyników

  clear_file_score(file_score) #czyści plik

  #zapisuje plik odnowa i dodaje miejsce gracza do niego ↓↓↓↓↓
  file_score = open(score_file, encoding='UTF-8',mode='a')

  for e in range(len(file_score_list)):
    ew= file_score_list[e]
    file_score.writelines(ew+'\n')
  #zapisuje plik odnowa i dodaje miejsce gracza do niego ↑↑↑↑↑

  if input("Czy chcesz zapisać labirynt?(T/N)").lower() == 't':
    nazwa = input('podaj pełną nazwę pliku do którego chcesz zapisać, jeżeli pozostawione puste załaduje do labirynt_list.txt')
    if nazwa != '':
      labirynt_file_save=nazwa
    save_labirynth(n,labirynt_file_save,start_y,start_x)
    

  file_score.close()

#menu
print("MENU\n[1] - Graj\n[2] - Wczytaj labirynt\n[3] - Zobacz listę wyników")
inp = int(input())
if inp == 1:
  gra()
elif inp == 2:
  load_lab()
elif inp == 3:
  print_score()

while True:
  print('',end='')
