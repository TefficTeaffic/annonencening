import pygame as p

betaicon = p.image.load('resources/icons/betaicon.png')
player = p.image.load('resources/player/stand.png')
p_w = p.image.load('resources/player/walk.png')
bg = p.image.load('resources/backgrounds/big_hotel_outside.png')

p.init()

screen = p.display.set_mode((1000, 900), p.FULLSCREEN)
p.display.set_caption('Annonencening - Closed Beta (0.1 build)')
p.display.set_icon(betaicon)

run = True
while run:
    screen.blit(bg, (0, 0))
    screen.blit(player, (500, 900))
    p.display.update()
    for e in p.event.get():
        if e.type == p.QUIT:
            run = False

p.quit()
