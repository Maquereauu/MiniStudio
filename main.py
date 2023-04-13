from curses import getmouse
import pygame

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 0
y= 0
width = 50
height = 50
vel = 15
CLOCK = pygame.time.Clock()
img = pygame.image.load("img/menu.png").convert_alpha()
img = pygame.transform.scale(img , (1920 , 1080))
while run:
    dingus = img.get_rect(topleft = (x,y))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    win.fill((0,0,0))
    win.blit(img, dingus)
    if event.type == pygame.MOUSEBUTTONDOWN:
        run = False
    CLOCK.tick(165)
    pygame.display.update()
pygame.quit()