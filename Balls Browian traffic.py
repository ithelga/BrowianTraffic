import pygame
import random
import math
from os import path

def sqr(x):
    return x**2

SIZE = WIDTH, HEIGHT = 450, 450

FPS = 60
R = 25

D = 2*R
D2 = sqr(D)

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("шарики")
clock = pygame.time.Clock()

img_dir = path.join(path.dirname(__file__), 'img')
ball_img_list = []
for fname in 'ball1.png ball2.png ball3.png ball4.png'.split():
    ball_img_list.append(pygame.transform.scale(pygame.image.load(path.join(img_dir, fname)), (D,D)))
background = pygame.image.load(path.join(img_dir, "background.png")).convert()
background = pygame.transform.scale(background, SIZE)
background_rect = background.get_rect()



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed

    @property
    def dx(self):
        return self.speed[0]

    @property
    def dy(self):
        return self.speed[1]

    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0:
            self.speed[0] = abs(self.speed[0])
        elif self.rect.right > WIDTH:
            self.speed[0] = -abs(self.speed[0])
        if self.rect.top < 0:
            self.speed[1] = abs(self.speed[1])
        elif self.rect.bottom > HEIGHT:
            self.speed[1] = -abs(self.speed[1])


all_sprites = pygame.sprite.Group()
balls_list = []

def addBall(b):
    print(b.dx, b.dy)
    all_sprites.add(b)
    #balls.add(b)
    balls_list.append(b)

def setBalls4_3_1(sY):
    for i in range(4):
        addBall(Ball((2 * i + 1)*WIDTH//8, R + (3-i)*R, [sY[i], 2*i+1], ball_img_list[i]))
    for i in range(1,4):
        addBall(Ball(i*WIDTH//4, HEIGHT-2*R, [sY[i-1], -1-2*i], ball_img_list[3-i]))
    addBall(Ball(WIDTH//2, HEIGHT//2, [0, 0], ball_img_list[0]))


#def setBalls2():
    #addBall(Ball(WIDTH//3, 2*R, [0, 4], ball_img_list[0]))
    #addBall(Ball(WIDTH//3, HEIGHT-5*R, [0, 0], ball_img_list[1]))


setBalls4_3_1([-6, -6, 0, 6])


img_num = 1
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    for i, b1 in enumerate(balls_list[:-1]):
        for b2 in balls_list[i+1:]:
            a = b1.rect.centerx-b2.rect.centerx
            b = b1.rect.centery-b2.rect.centery
            dist = sqr(a) + sqr(b)
            # если расстояние меньше диаметра, значит есть факт соударения
            if dist < D2:
                dist = math.sqrt(dist) # расстояние между центрами шаров
                p1 = a * b / sqr(dist)
                p2 = sqr(a / dist)
                p3 = sqr(b / dist)
                d1 = b1.dy * p1 + b1.dx * p2 - b2.dy * p1 - b2.dx * p2
                d2 = b1.dx * p1 + b1.dy * p3 - b2.dx * p1 - b2.dy * p3
                # меняем значение приращения координаты шаров при движении
                b1.speed = [round(b1.dx - d1), round(b1.dy - d2)]
                b2.speed = [round(b2.dx + d1), round(b2.dy + d2)]
                # при соударении шары всегда "проникают" друг в друга, поэтому раздвигаем их
                p3 = (D - dist)/2
                p1 = p3 * (a / dist)
                p2 = p3 * (b / dist)
                b1.rect.centerx += round(p1)
                b2.rect.centery += round(p2)
                b2.rect.centerx -= round(p1)
                b2.rect.centery -= round(p2)



    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()


pygame.quit()
