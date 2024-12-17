import pygame as p

p.init()

screen = p.display.set_mode((800, 600))
screen.fill((0, 255, 0))
p.display.set_caption('DA')



p.display.flip()



while True:
  x=1
  
# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing RGB Color
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()
