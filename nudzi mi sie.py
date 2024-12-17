import keyboard as k
import time

wolne = '■'
wo = wolne
postać = '☺'
ss = 8
m = []
for i in range(ss):
  mr = []
  for j in range(ss):
    mr.append(wo)
  m.append(mr)

n = m
n[0][0] = postać
x = 0
y = 0
for i in range(len(n[0])):
  n[1][i] = '∙'


def printlist():
  for i in range(len(n)):
    print(*n[i], sep=' ')
  print()


def ruch():
  global y
  global x
  global ss
  w = k.read_key()
  n[y][x] = wo
  if w == 'w' and n[y - 1][x] == wo:
    y -= 1
  if w == 'a' and n[y][x - 1] == wo:
    x -= 1
  if w == 's' and n[(y + 1) % ss][x] == wo:
    y = (y + 1) % ss
  if w == 'd' and n[y][(x + 1) % ss] == wo:
    x = (x + 1) % ss

  n[y][x] = postać


while True:
  n = m
  printlist()
  while True:
    ruch()
    printlist()
    time.sleep(0.5)
#k.wait("w" or "a" or "s" or "d")

printlist()
