import pygame
import sys

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 40
y= 40
width = 50
height = 50
vel = 15
CLOCK = pygame.time.Clock()
pos = pygame.mouse.get_pos()
img = pygame.image.load("img/menu.png").convert_alpha()
bruh =pygame.image.load("img/dingus.jpg").convert_alpha()
img = pygame.transform.scale(img , (1920 , 1080))
while run:
    map = img.get_rect(topleft = (0,0))
    dingus = bruh.get_rect(topleft = (x,y))
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] or keys[pygame.KMOD_ALT] and keys[pygame.K_F4]:
                run = False
    if keys[pygame.K_LEFT] and x > 5:
                x-=vel
    if keys[pygame.K_RIGHT] and x < 1915:
                x+=vel
    if keys[pygame.K_UP] and y > 5:
                y -= vel
    if keys[pygame.K_DOWN] and y < 1075:
                y += vel
    win.fill((0,0,0))
    win.blit(img, map)
    win.blit(bruh, dingus)
    if event.type == pygame.MOUSEBUTTONDOWN:
        run = False
    CLOCK.tick(165)
    pygame.display.update()
pygame.quit()