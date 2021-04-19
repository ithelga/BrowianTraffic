import pygame
import random

size = width, height = (700, 700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption('traffic')


def load_image(name):
    fullname = "img" + "\\" + name
    try:
        if name[-2:] == 'jpg':
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print("Cannot load image:", fullname)
        raise SystemExit()
    return image

class Ball(pygame.sprite.Sprite):

    image = load_image('ball.png')

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.add(ballon)
        self.image = Ball.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)


    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect((x1, y1, 1, y2 - y1))
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)



all_sprites = pygame.sprite.Group()

ballon = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)

list_of_Ball=[]
for i in range(10):
    list_of_Ball.append(Ball(random.randint(100, 500), random.randint(100, 500)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    for sprite in all_sprites:
        sprite.update()

    for i, Ball1 in enumerate(list_of_Ball[:-1]):
        for Ball2 in list_of_Ball[i+1:]:
            if (Ball1.rect.x - Ball2.rect.x) ** 2 + (Ball1.rect.y - Ball2.rect.y) ** 2 <= 70 ** 2:
                Ball1.vx, Ball1.vy = -Ball1.vx, -Ball1.vy
                Ball2.vx, Ball1.vy = -Ball2.vx, -Ball1.vy

    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()



