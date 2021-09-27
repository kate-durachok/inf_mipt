import pygame
from pygame.draw import *
from random import *
import math


def igolki(x, y):
    c = randint(0, 50)
    pygame.draw.polygon(screen, (c, c, c), [(x, y), (x + randint(2, 20), y - randint(20, 35)), (x + randint(2, 20), y)])


pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill([44, 77, 50])
pygame.display.set_caption("My program")

# пол
pygame.draw.rect(screen, (89, 74, 40), ((0, 500), (500, 200)))

# деревья
pygame.draw.rect(screen, (105, 60, 55), ((0, 0), (75, 650)))
pygame.draw.rect(screen, (125, 80, 75), ((0, 0), (25, 650)))
pygame.draw.rect(screen, (84, 60, 70), ((200, 0), (70, 550)))
pygame.draw.rect(screen, (135, 101, 124), ((200, 0), (20, 550)))
pygame.draw.rect(screen, (135, 82, 76), ((430, 0), (50, 700)))
pygame.draw.rect(screen, (157, 109, 93), ((430, 0), (15, 700)))

# листва
pygame.draw.rect(screen, (92, 105, 68), ((0, 0), (500, 150)))
for i in range(100):
    pygame.draw.circle(screen, (randint(90, 159), randint(110, 170), randint(60, 90)),
                       (randint(-100, 500), randint(-10, 200)), randint(5, 60))

# ежик
pygame.draw.ellipse(screen, (61, 59, 56), (110, 500, 90, 50))

for i in range(50):
    x = randint(110, 170)
    y = randint(500, 530)
    igolki(x, y)
# собрать одну функцию ежик



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
