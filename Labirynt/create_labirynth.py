import random as r

def oposite_of_wsad(w):
  oposite_w=''
  if w == 'a':
    oposite_w = 'd'
  elif w == 'd':
    oposite_w = 'a'
  elif w == 'w':
    oposite_w = 's'
  elif w == 's':
    oposite_w = 'w'
  return oposite_w

def path(wall,position,win_position,n,w,nf,size_y,size_x,iteration):
  y,x = position
  iteration +=1
  posibilities = 3
  wsad = ['w','a','s','d','']
  wsad.remove(oposite_of_wsad(w)) #uniemożliwia pójście w kierunku z którego się przyszło
  for w in wsad:      #sprawdza czy nie trafił do ślepego zakontka
    if (w == 'w' and n[y - 1][x] == wall) or (w == 'a' and n[y][x - 1] == wall) or (w == 's' and n[(y + 1) % size_y][x] == wall) or (w == 'd' and n[y][(x + 1) % size_x] == wall):
      posibilities -= 1
  if posibilities == 0: #sprawdza czy nie trafił do ślepego zakontka
    return False
  nf[y][x] = 1    #oznacza miejsce jako odwiedzone
  for w in wsad: 
    ma = 0          #liczba ruchów - żeby na mapach zapętlających nie zacinał się  #wykonuje ruch dla każdego kierunku
    while True:   #pętla sumuluje ruch
      ma+=1       #zwiękrza liczbe ruchów o 1 przy przejśćiu na kolejne pole
      if w == 'w' and n[y - 1][x] != wall:
        y -= 1
        if y < 0:
          y = size_y + y
      elif w == 'a' and n[y][x - 1] != wall:
        x -= 1
        if x < 0:
          x = size_x + x
      elif w == 's' and n[(y + 1) % size_y][x] != wall:
        y = (y + 1) % size_y
      elif w == 'd' and n[y][(x + 1) % size_x] != wall:
        x = (x + 1) % size_x
      else:
        break
      if ma+1 >= max(size_y,size_x):
        return False
    position=y,x
    if nf[y][x]== 1:#jeżeli już to pole zostało odwiedzone przechodzi do kolejnego kierunku
      continue
    if [y,x] == win_position and iteration > 2:  #jeżeli znalazł rązwiązanie dla labiryntu, które zajmuje ponad 2 ruchy, mówi że to odpowiedni labirynt
      return True
    elif path(wall,position,win_position,n,w,nf,size_y,size_x,iteration) == True: #jeżeli kolejna w kolejnej iteracji została znaleziona wygrana przekazujo to aż do 0 iteracji
      return True
  return False      #jak coś nie wyszło to mówi zły labirynt

def create_labirynth(size_x,size_y,wall,nonwall,win,x,y):
  while True: #tworzy labirynty dopuki nie zostanie znaleziony pasujący
    n=[]      #pusta lista labiryntu
    win_position = [r.randint(0,size_y-1) , r.randint(0,size_x-1)] #losuje pozycje wygranej
    for i in range(size_y):   #spaja linie w całość
      m=[]
      for j in range(size_x): #tworzy linie labiryntu
        if [i,j] == win_position:
          m.append(win)
        elif r.randint(0,2) == 0:
          m.append(nonwall)
        else:
          m.append(wall)
      n.append(m)
    if n[y][x] != wall: #sprawdza czy labirynt jest do przejścia
      #ustalanie zmiennych
      position=y,x
      w = ''
      iteration = 0
      nf = []        #lista miejsc odwiedzonych
      for i in range(size_y):
        nf.append([0]*size_x)
      if path(wall,position,win_position,n,w,nf,size_y,size_x,iteration) == True:  #jeśli znaleziono labirynt returnuje go
        return n