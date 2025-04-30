import pygame as p
import sys

betaicon = p.image.load('resources/icons/betaicon.png')
player = p.image.load('resources/player/stand.png')
p_w = p.image.load('resources/player/walk.png')
p_x = 450
p_y = 450
speed = 5
clock = p.time.Clock()

p.init()

screen = p.display.set_mode((1000, 600))
p.display.set_caption('Annonencening - Closed Beta (0.1 build)')
p.display.set_icon(betaicon)


def draw():
    screen.fill((153, 247, 247))


run = True
while run:
    for e in p.event.get():
        if e.type == p.QUIT:
            run = False

    keys = p.key.get_pressed()
    if keys[p.K_a] and p_x > 50:
        p_x -= speed
    elif keys[p.K_d] and p_x < 900:
        p_x += speed
    elif keys[p.K_SPACE] and p_y > 50:
        p_y -= speed
    elif keys[p.K_s] and p_y < 450:
        p_y += speed

    draw()
    screen.blit(player, (p_x, p_y))
    p.display.flip()
    p.display.update()
    clock.tick(60)

p.quit()
