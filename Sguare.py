import pygame

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('traffic')

screen = pygame.Surface((400, 400))

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))


    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1, x2, y1, y2):
    if (x1 > x2 - 40) and (x1 < x2 + 40) and (y1 > y2 - 40) and (y1 < y2 + 40):
        return 1
    else:
        return 0

hero = Sprite(200, 350, "img/hero.png")
hero.go_right = True
hero.go_down = True

zero = Sprite(200, 10, "img/zero.png")
zero.go_right = True
zero.go_down = True

done = True

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    screen.fill((50, 50, 50))

    if hero.go_right == True:
        hero.x += 1
        if hero.x > 360:
            hero.go_right = False
    else:
        hero.x -= 1
        if hero.x < 0:
            hero.go_right = True

    if hero.go_down == True:
        hero.y += 1
        if hero.y > 360:
            hero.go_down = False
    else:
        hero.y -= 1
        if hero.y < 0:
            hero.go_down = True

    if zero.go_right == True:
        zero.x += 1
        if zero.x > 360:
            zero.go_right = False
    else:
        zero.x -= 1
        if zero.x < 0:
            zero.go_right = True

    if zero.go_down == True:
        zero.y += 1
        if zero.y > 360:
            zero.go_down = False
    else:
        zero.y -= 1
        if zero.y < 0:
            zero.go_down = True

    if Intersect(zero.x, hero.x, zero.y, hero.y) == True:
        hero.go_right = True
        zero.go_right = False
        hero.go_down = True
        zero.go_down = False

    hero.render()
    zero.render()

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
