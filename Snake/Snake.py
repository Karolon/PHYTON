import keyboard as k
import time
import os
import random as r

side = '▒'
background=' '
snake_head='☻'
snake_body='■'
food='♣'
n=[]

#sets the size
def set_size():
  try:
    size=int(input('Set size '))
    for i in range(size):
      n.append([' '] * size)
  except:
    print('I thougth you were smart, try again')
    size = set_size()
  return size

size = set_size()

#sets firts food position
food_pos=[size//2,size//2]
while food_pos == [size//2,size//2]:
  food_pos = [r.randint(0,size-1),r.randint(0,size-1)]

#sets starting position at the middle
snake_head_position = (size//2,size//2)
list_snake_body =[[size//2,size//2]]



#moves snake
def move():
  global food_pos, snake_head_position, list_snake_body, key, size

  #checks for win
  if len(list_snake_body) == size * size-1:
    print('You won!')
    return True
  

  #defines y,x
  y,x = snake_head_position


  #moves head
  if key == 'w':
    y -= 1
    #checks if bumped into wall or itself
    if y < 0 or [y,x] in list_snake_body[1:]:
      print('You lost')
      return True
  elif key == 'a':
    x -= 1
    if x < 0 or [y,x] in list_snake_body[1:]:
      print('You lost')
      return True
  elif key == 's':
    y += 1
    if y >= size or [y,x] in list_snake_body[1:]:
      print('You lost')
      return True
  elif key == 'd':
    x += 1
    if x >= size or [y,x] in list_snake_body[1:]:
      print('You lost')
      return True
    
  #if head is at the same tile as food makes the snake longer
  if [y,x] != food_pos:
    del list_snake_body[0]

  #adds body where the head is
  list_snake_body.append([y,x])

  #moves food when it gets eaten
  if [y,x] == food_pos:
    while food_pos == [y,x] or food_pos in list_snake_body:
      food_pos = [r.randint(0,size-1),r.randint(0,size-1)]

  snake_head_position = y,x

#prints snake, food, and background
def printlist():
  global n,food_pos,snake_head_position,snake_head,list_snake_body,snake_body,size,background,side
  #clears console
  os.system('cls')
  for i in range(size+2):
    for j in range(size+2):
      #print up and down sides
      if (i == size+1 or i == 0) and j != size+1:
        print(side*2,end='')
      #print left and right sides
      elif j == 0 or j == size+1:
        print(side,end=' ')
      #prints head
      elif (i-1,j-1) == snake_head_position:
        print(snake_head, end =' ')
      #prints body
      elif [i-1,j-1] in list_snake_body:
        print(snake_body, end =' ')
      #prints food
      elif [i-1,j-1] == food_pos:
        print(food, end=' ')
      #prints background
      else:
        print(background, end=' ')
    print()


printlist()

#recives input, then starts the game
key = k.read_key()

#sets the key when something is pressed
def change_key(k):
  global key
  key = str(k)[-5]


k.on_release(change_key)



while True:
  printlist()
  time.sleep(0.5)
  if move():
    break


while True:
  time.sleep(10000)