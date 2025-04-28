import pygame as p

p.init()

size = (500, 300)

screen = p.display.set_mode(size)
screen.fill((0, 255, 0))
p.display.set_caption('DA')

font = p.font.SysFont('freesanbold.ttf', 50)
text = font.render('TEXT', True, (255,0,0))
textBox = text.get_rect()
textBox.center = (size)
screen.blit(text, textBox)


p.display.flip()  



while True:
  x=1
  