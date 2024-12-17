import keyboard as k
import time
import os

ściana = '■'
win = 'x'
postać = '☺'
szer = 0
wys = 0
m = []
l_ruch=0
u=0
czas = time.time()
file_lab = open('labirynt.txt', encoding='UTF-8')

for f in file_lab:
  #f = f.replace('\n','')
  f = f.strip()
  f = f.split()
  m.append(f)
szer = len(f)
wys = len(m)

n = m
x = 0
y = 0


def printlist():
  for i in range(len(n)):
    for j in range(len(n[i])):
      if i == y and j == x:
        print(postać, end='')
        print(' ', end='')
      else:
        print(*n[i][j], end='')
        print(' ', end='')
    print()

def check_win():
  global x,y,n
  if n[y][x] == win:
    return(1)


def ruch():
  global y, x, wys, szer, l_ruch
  w = k.read_key()
  l_ruch += 1
  while True:
    if w == 'w' and n[y - 1][x] != ściana:
      y -= 1
      if y < 0:
        y = wys + y
    elif w == 'a' and n[y][x - 1] != ściana:
      x -= 1
      if x < 0:
        x = wys + x
    elif w == 's' and n[(y + 1) % wys][x] != ściana:
      y = (y + 1) % wys
    elif w == 'd' and n[y][(x + 1) % szer] != ściana:
      x = (x + 1) % szer
    else:
      break
    os.system('cls')
    printlist()
    print(l_ruch)
    time.sleep(0.2)
  print ("\033[A                             \033[A")
  print(l_ruch)
  time.sleep(0.2)
  return(check_win())

#program starts
n = m
printlist()
while u!=1:
  u = ruch()
print('Wygrałeś !','twój wynik to',l_ruch,"\n a czas to",int(time.time()- czas),'s')

while True:
  print('',end='')
  
