import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
white = [255, 255, 255]
screen.fill(white)
pygame.display.set_caption("My program")
pygame.display.flip()

circle(screen, (240, 240, 60), (250, 200), 100)
circle(screen, (0, 0, 0), (250, 200), 100, 1)

circle(screen, (255, 217, 224), (290, 190), 30)
circle(screen, (255, 217, 224), (210, 190), 30)
circle(screen, (191, 126, 139), (290, 190), 30, 1)
circle(screen, (191, 126, 139), (210, 190), 30, 1)

pygame.draw.line(screen, (0, 0, 0), (260, 160), (310, 140), 12)
pygame.draw.line(screen, (0, 0, 0), (240, 160), (190, 140), 12)

circle(screen, (0, 0, 0), (290, 190), 17)
circle(screen, (0, 0, 0), (210, 190), 17)

pygame.draw.rect(screen, (0, 0, 0), ((230, 250), (70, 10)))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
