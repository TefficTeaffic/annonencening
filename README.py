import pygame as p
import sys

betaicon = p.image.load('resources/icons/betaicon.png')
player = p.image.load('resources/player/stand.png')
p_w = p.image.load('resources/player/walk.png')
x = 450
y = 450
speed = 10
clock = p.time.Clock()

p.init()

screen = p.display.set_mode((1000, 600))
p.display.set_caption('Annonencening - Closed Beta (0.1 build)')
p.display.set_icon(betaicon)


def draw():
    screen.fill((227, 130, 123))


run = True
while run:
    for e in p.event.get():
        if e.type == p.QUIT:
            run = False
            break

    keys = p.key.get_pressed()
    if keys[p.K_LEFT] and x > 50:
        x -= speed
        left = True
        right = False
    elif keys[p.K_RIGHT] and x < 900:
        x += speed
        left = False
        right = True

    draw()
    screen.blit(player, (x, y))
    p.display.flip()
    p.display.update()
    clock.tick(60)

p.quit()
