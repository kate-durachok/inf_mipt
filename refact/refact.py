import pygame
import pygame.draw as pgd
from math import sin, cos, pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode((910, 600))


def sun(x, y, n, r1, r2, color):
    """
    :param x: положение центра солнца по x
    :param y: положение центра солнца по y
    :param n: количество лучиков
    :param r1: внешний радиус (по концам лучиков)
    :param r2: внутренний радиус (по основаниям лучиков)
    :param color: цвет солнца
    :return: изображение солнца
    """
    spt = []
    for i in range(n * 2):
        a = 2 * pi * i / (2 * n)
        if i % 2 == 0:
            xt = int(r1 * cos(a))
            yt = int(r1 * sin(a))
        else:
            xt = int(r2 * cos(a))
            yt = int(r2 * sin(a))
        xt += x
        yt += y
        spt.append((xt, yt))
    pgd.polygon(screen, color, spt, 0)
    pgd.polygon(screen, (0, 0, 0), spt, 1)


def cloud(x, y, r, color):
    """
    :param x: положение верхнего левого угла прямоугольника в который вписано облако по x
    :param y: положение верхнего левого угла прямоугольника в который вписано облако по y
    :param r: радиус круга составяющего облако
    :param color: цвет облака
    :return: изображение облака
    """
    pgd.circle(screen, color, (x + r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + r, y + 2 * r), r, 1)
    pgd.circle(screen, color, (x + 2 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 2 * r, y + 2 * r), r, 1)
    pgd.circle(screen, color, (x + 3 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 3 * r, y + 2 * r), r, 1)
    pgd.circle(screen, color, (x + 4 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 4 * r, y + 2 * r), r, 1)
    pgd.circle(screen, color, (x + 3 * r, y + r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 3 * r, y + r), r, 1)
    pgd.circle(screen, color, (x + 2 * r, y + r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 2 * r, y + r), r, 1)


def tree(x, y, s, c_trunk, c_leaves):
    """
    :param x: положение верхнего левого угла прямоугольника в который вписано дерево по x
    :param y: положение верхнего левого угла прямоугольника в который вписано дерево по x
    :param s: размер дерева
    :param c_trunk: цвет ствола
    :param c_leaves: цвет листьев
    :return: изображение дерева
    """
    k = 0.8
    pgd.rect(screen, c_trunk, (x + s * 3 // 7, int(y + s * k), s // 7, s))
    pgd.circle(screen, c_leaves, (x + s // 2, int(y + s * k // 4)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s // 2, int(y + s * k // 4)), s // 4, 1)
    pgd.circle(screen, c_leaves, (x + s // 4, int(y + s * k // 2)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s // 4, int(y + s * k // 2)), s // 4, 1)
    pgd.circle(screen, c_leaves, (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 1)
    pgd.circle(screen, c_leaves, (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 1)
    pgd.circle(screen, c_leaves, (x + s // 4, int(y + s * k)), s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s // 4, int(y + s * k)), s // 4, 1)
    pgd.circle(screen, c_leaves, (x + s * 3 // 4, int(y + s * k)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s * 3 // 4, int(y + s * k)), s // 4, 1)


def house(x, y, s, c_house, c_roof, c_roofpattern):
    """
    :param x: положение верхнего левого угла прямоугольника в который вписан дом по x
    :param y: положение верхнего левого угла прямоугольника в который вписан дом по y
    :param s: размер дома
    :param c_house: цвет основания дома
    :param c_roof: цвет крыши
    :param c_roofpattern: цвет рисунка на крыше
    :return: изображение дома
    """
    pgd.rect(screen, c_house, (x, y + s, 2 * s, int(1.5 * s)))               # основание дома
    pgd.rect(screen, (0, 0, 0), (x, y + s, 2 * s, int(1.5 * s)), 1)
    pgd.rect(screen, (150, 150, 255), (x + s * 3 // 4, y + int(1.5 * s), s // 2, s // 2))          # окно
    pgd.rect(screen, (190, 100, 34), (x + s * 3 // 4, y + int(1.5 * s), s // 2, s // 2), 5)
    pgd.polygon(screen, c_roof, [(x, y + s), (x + s, y), (x + 2 * s, y + s)], 0)      # крыша
    pgd.polygon(screen, (0, 0, 0), [(x, y + s), (x + s, y), (x + 2 * s, y + s)], 1)
    kt = 13
    for i in range(kt + 1):                                                           # рисунок на крыше сверху вниз
        pgd.polygon(screen, c_roofpattern, [(x + s - i * int(s // kt), y + i * int(s // kt)),
                                            (x + s - (i + 1) * int(s // kt), y + (i + 1) * int(s // kt)),
                                            (x + s - i * int(s // kt), y + (i + 1) * int(s // kt))], 0)
    for i in range(kt + 1):                                                           # рисунок на крыше снизу вверх
        pgd.polygon(screen, c_roofpattern, [(x + s + i * int(s // kt), y + i * int(s // kt)),
                                            (x + s + (i + 1) * int(s // kt), y + (i + 1) * int(s // kt)),
                                            (x + s + i * int(s // kt), y + (i + 1) * int(s // kt))], 0)


pgd.rect(screen, (139, 174, 217), (0, 0, 910, 300))
pgd.rect(screen, (109, 145, 100), (0, 300, 910, 300))
sun(50, 50, 20, 40, 38, (200, 200, 50))
cloud(150, 40, 35, (200, 200, 200))
tree(320, 210, 140, (46, 28, 27), (51, 89, 41))
house(100, 230, 100, (209, 132, 50), (69, 57, 61), (133, 78, 96))
house(500, 230, 80, (166, 139, 111), (82, 92, 59), (47, 48, 42))
tree(700, 200, 110, (46, 28, 27), (51, 89, 41))
cloud(430, 100, 25, (255, 255, 255))
cloud(700, 60, 37, (230, 230, 230))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
