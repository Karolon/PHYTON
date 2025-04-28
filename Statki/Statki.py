import os, time
board_size = 10
ship = 'S'
shipsLenght = [5,4,3,3,2]
shot = 'X'
miss = 'x'


#creates board list
def create_board():
  board = []
  for b in range(board_size + 1):
    board.append(['·']*(board_size + 1))
  return board


#print board to terminal
def print_board(board):
  
  #print letter for each collumn
  for i in range(board_size):
    print(chr(65 + i) + ' ', end = '')
  print()

  #prints rest of the board
  for y in range(board_size):
    for x in range(board_size):
      print(board[y][x]+' ', end = '')
    print((y + 1), end = '')
    print()
 

#copies board
def copy_board(board):
  return board[:]


#gets and turns coordinates into for readable by python
#returns in form [y,x]
def get_coordinates():
  global board_size

  coordinates = input('(przykład \"A 2\")\n')
  coordinates = coordinates.split()

  #Checks if cordinates are in valuid format7
  if len(coordinates) != 2:
    print('Podano w złym formacie, podaj jeszcze raz')
    return get_coordinates()
  
  #Turns letters into numbers
  try:
    coordinates[0] = ord(coordinates[0].upper()) - 65
    coordinates[1] = int(coordinates[1]) - 1
  except:
    print('Mylą ci się litery i liczby, podaj jeszcze raz')
    return get_coordinates()

  #Checs if location is valid on board
  if (coordinates[0] or coordinates[1]) > board_size or (coordinates[0] or coordinates[1]) < 0:
    print('Podana lokacja poza planszą, podaj jeszcze raz')
    return get_coordinates()
  return coordinates


def set_ship(ship_length, board):
  Mistackes = True

  #while there is some mistake in input
  while Mistackes:
    facing = ''
    Mistackes = False
    print("Podaj lokalizcję rufy statku( długoś -",ship_length,")")
    x,y = get_coordinates()
    newBoard = copy_board(board)
    
    while facing.lower() not in ['lewo', 'góra']:
      print("Podaj kierunek w którym statek ma być skierowany (lewo/góra)")
      facing = input()

    #sets ship facing left
    if facing == 'lewo':
      for i in range(ship_length):
        #checks if ship is out of bounds or if collides with another ship
        if x - i < 0 or board[y-1][x-i] == ship or board[y][x-i] == ship or board[y+1][x-i] == ship:
          print('statek koliduje, jeszcze raz')
          Mistackes = True
          break
        newBoard[y][x-i] = ship
      #checs if corners colide with another ship
      if board[y-1][x-i-1] == ship or board[y][x-i-1] == ship or board[y+1][x-i-1] == ship or board[y-1][x+1] == ship or board[y][x+1] == ship or board[y+1][x+1] == ship:
          print('statek koliduje, jeszcze raz')
          Mistackes = True

    #sets ship facing up
    elif facing == 'góra':
      for i in range(ship_length):
        #checks if ship is out of bounds or if collides with another ship
        if y - i < 0 or board[y-i][x-1] == ship or board[y-i][x] == ship or board[y-i][x+1] == ship:
          print('statek koliduje, jeszcze raz')
          Mistackes = True
          break
        newBoard[y-i][x] = ship
      #checs if corners colide with another ship
      if board[y-i-1][x-1] == ship or board[y-i-1][x] == ship or board[y-i-1][x+1] == ship or board[y+1][x-1] == ship or board[y+1][x] == ship or board[y+1][x+1] == ship:
          print('statek koliduje, jeszcze raz')
          Mistackes = True

     #if someone has a skill issue it makes it repeat  
#    if Mistackes:
#      continue
#    break
  return newBoard


#sets the ships on the board for the game
def game_setUp(board1, board2):

  #sets the board for player 1
  print_board(board1)
  for i in shipsLenght:
    board1 = set_ship(i, board1)
    print_board(board1)

  #sets the board for player 2
  print('Jeżeli skończyłeś to naciśnij enter, żeby przekazać planszę drugiemu graczowi')
  input()
  for i in shipsLenght:
    board2 = set_ship(i)
    print_board(board2)

  return board1, board2


#checks for win
def isWin(board_shot):
  #counts how many tiles have ships on them
  shipsAmount = 0
  for e in shipsLenght:
    shipsAmount += e
  #counts how many tiles you shot
  shots = 0
  for i in board_size:
    for j in board_size:
      if board_shot[i][j] == shot:
        shots += 1
  #if the amounts are the same it returns True - meaning there is a win
  if shots == shipsAmount:
    return True
  else:
    return False


#turn
def turn(board, board_shot, winner = ''):
  while True:
    os.system('cls')
    print_board(board_shot)
    print('Podaj kordynaty strzału')
    y, x = get_coordinates()
    #if you shot this sqare you must choose another
    if board[y][x] in [shot, miss]:
      print('Już tu strzelałeś, jescze raz')
      input('enter')
      pass
    #checks if you succesfuly shot a ship if yes, you may try again
    elif board[y][x] == ship:
      board_shot[y][x] = shot
      if isWin(board_shot):
        win = True
        break
    else:
      board_shot[y][x] = miss
      break
  return board_shot, win




board1, board2, board1_shots, board2_shots = [create_board()]*4

board1, board2 = game_setUp(board1, board2)

winner = ''
win = False
while win:  
  #signilises next palyer turn
  time.sleep(2)
  os.system('csl')
  input('Tura gracza 2, kiedy gotowy naciśnij enter')

  #player 1 turn
  board1_shots, win = turn(board1, board1_shots)
  if win:
    time.sleep(1)
    os.system('cls')
    print('Gracz 1 wygrał!')
    break

  #signilises next palyer turn
  time.sleep(2)
  os.system('csl')
  input('Tura gracza 2, kiedy gotowy naciśnij enter')

  #player 2 turn
  board2_shots, win = turn(board2, board2_shots)
  if win:
    time.sleep(1)
    os.system('cls')
    print('Gracz 2 wygrał!')