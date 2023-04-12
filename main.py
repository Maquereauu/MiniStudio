import pygame

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((800,800))
run = True
x= 40
y= 40
width = 50
height = 50
vel = 10
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x < 200:
        x+=vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN]and y < 750:
        y += vel
    win.fill((0,0,0))
    pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    pygame.display.update()
pygame.quit()