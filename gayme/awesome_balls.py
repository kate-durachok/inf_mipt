import pygame
from pygame.draw import *
from random import randint
from LIB_colors import *
import time
from time import sleep
import numpy as np

pygame.init()
pygame.font.init()

rng = np.random.default_rng(int(time.time()))
FPS = 60
WIDTH = 1000
HEIGHT = 600
W_WIDTH = 1300
W_HEIGHT = 700
points = 0
c_timer = 0
c_points = 300
dc_points = 300
counter = 120
color_t = PERFUME

screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))

f1 = pygame.font.SysFont('micro', 48)
f_p = pygame.font.SysFont('micro', 40)
font = pygame.font.SysFont('micro', 40)
f_sc = pygame.font.SysFont('micro', 35)

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

name = str(input('Name your fighter(No more than 8 symbols): \n'))
name = name[:8]


class Leaderboard:
    """ таблица лидеров """

    def __init__(self, fileName):
        try:
            with open(fileName, 'r') as file:
                self.data = [user.strip('\n').split(';') for user in file.readlines()]
        except FileNotFoundError:
            with open(fileName, 'w') as file:
                pass
            self.data = []

        self.data = dict([[user[0], int(user[1])] for user in self.data])

        self.fileName = fileName

    def fillToLim(self, txt, limit):
        return txt + ' '*(limit - len(txt))

    def get(self, points):
        try:
            del self.data['---YOU---']
        except Exception:
            pass

        board = self.data
        board['---YOU---'] = points
        board = sorted(board.items(), key=lambda item: item[1], reverse=True)

        return board

    def set(self, nick, points):
        try:
            del self.data['---YOU---']
        except Exception:
            pass

        nick = self.fillToLim(nick, 8)
        if nick in self.data:
            self.data[nick] = max(self.data[nick], points)
        else:
            self.data[nick] = points

        self.data = dict(sorted(self.data.items(), key=lambda item: item[1], reverse=True))

    def save(self):
        self.data = [user + ';' + str(self.data[user]) + '\n' for user in self.data]

        with open(self.fileName, 'w') as file:
            file.writelines(self.data[:5])


class Ball:

    """ главная мишень шарик, просто существует,
        шарик появляется, когда другой шарик исчезает """

    def __init__(self):
        self.color = COLORS[np.random.randint(len(COLORS))]
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(10, 100)
        self.v_x = randint(350, 500) / FPS
        self.v_y = randint(250, 400) / FPS

    def draw_ball(self):
        circle(screen, self.color, (self.x, self.y), self.r)

    def update(self):
        self.x += self.v_x
        self.y += self.v_y
        if self.y >= 100 + HEIGHT - self.r:
            self.y = 100 + HEIGHT - self.r
            self.v_y *= -1

        if self.y <= 100 + self.r:
            self.y = 100 + self.r
            self.v_y *= -1

        if self.x >= WIDTH - self.r:
            self.x = WIDTH - self.r
            self.v_x *= -1

        if self.x <= 0 + self.r:
            self.x = 0 + self.r
            self.v_x *= -1


class Circle:

    """ дополнитеьная мишень, замедляет шарики на 3 секунды
        пояявляется каждые 300 очков, на поле такой нет """

    def __init__(self):
        self.color = COLORS1[np.random.randint(len(COLORS1))]
        self.x = randint(100, 1100)
        self.y = randint(100, 900)
        self.r = randint(30, 70)
        self.w = randint(4, 8)
        self.v_x = randint(650, 700) / FPS
        self.v_y = randint(650, 700) / FPS

    def draw_circle(self):
        circle(screen, self.color, (self.x, self.y), self.r, self.w)

    def update(self):
        self.x += self.v_x
        self.y += self.v_y
        if self.y >= 100 + HEIGHT - self.r - self.w:
            self.y = 100 + HEIGHT - self.r - self.w
            self.v_y *= -1

        if self.y <= 100 + self.r + self.w:
            self.y = 100 + self.r + self.w
            self.v_y *= -1

        if self.x >= WIDTH - self.r - self.w:
            self.x = WIDTH - self.r - self.w
            self.v_x *= -1

        if self.x <= 0 + self.r + self.w:
            self.x = 0 + self.r + self.w
            self.v_x *= -1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = [Ball() for _ in range(10)]
circles = [Circle() for _ in range(1)]
lb = Leaderboard('lb.txt')

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mp = pygame.mouse.get_pos()
            for i in range(len(balls) - 1, -1, -1):
                if (mp[0] - balls[i].x) ** 2 + (mp[1] - balls[i].y) ** 2 <= balls[i].r ** 2:
                    balls.remove(balls[i])
                    balls.append(Ball())
                    points += 1000 // balls[i].r
                    break
            if len(circles) != 0:
                if (mp[0] - circles[0].x) ** 2 + (mp[1] - circles[0].y) ** 2 <= circles[0].r ** 2:
                    circles.remove(circles[0])
                    c_timer = time.time()
                    for i in range(len(balls) - 1, -1, -1):
                        balls[i].v_x /= 3
                        balls[i].v_y /= 3
                    break
        elif event.type == timer_event:
            counter -= 1
            text2 = font.render(str(counter), True, (0, 128, 0))
            if 10 >= counter > 5:
                color_t = SWEETPINK
            if counter <= 5:
                color_t = RADICALRED

            if counter < 0:
                counter = 0
                pygame.time.set_timer(timer_event, 0)
                finished = True
                sleep(2)

    if time.time() - c_timer >= 1.5 and c_timer != 0:
        for i in range(len(balls) - 1, -1, -1):
            balls[i].v_x *= 3
            balls[i].v_y *= 3
        c_timer = 0

    if points >= c_points:
        c_points += dc_points
        if len(circles) == 0:
            circles.append(Circle())

    text = f_p.render("YOUR SCORE: " + str(points), True, PERFUME)
    screen.blit(text, (50, 25))

    text1 = f1.render("leaderboard:", True, MOONRAKER)
    screen.blit(text1, (1050, 25))

    text2 = font.render("TIME LEFT: " + str(counter), True, color_t)
    screen.blit(text2, (700, 25))

    data = lb.get(points)

    for i in range(len(data)):
        if data[i][0] == '---YOU---':
            text3 = f_sc.render(data[i][0], True, PEACH)
            text4 = f_sc.render(str(data[i][1]), True, PEACH)
        else:
            text3 = f_sc.render(data[i][0], True, WHITE)
            text4 = f_sc.render(str(data[i][1]), True, WHITE)
        screen.blit(text3, (1050, 100 + i * 50))
        screen.blit(text4, (1200, 100 + i * 50))


    for ball in balls:
        ball.update()
        ball.draw_ball()

    for obj in circles:
        obj.update()
        obj.draw_circle()

    pygame.display.update()

    screen.fill(DARKMINSK)
    rect(screen, MINSK, (0, 100, WIDTH, HEIGHT))

lb.set(name, points)
lb.save()
pygame.quit()
