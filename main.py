import pygame

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 40
y= 40
width = 10
height = 10
vel = 5
image = pygame.image.load("image/rat.jpg")
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x < 800:
        x+=vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((200,0,0))
    win.blit(image,(x,y))
    pygame.draw.rect(win,(0,180,255),(x,y,width,height))
    pygame.display.update()
pygame.quit()
