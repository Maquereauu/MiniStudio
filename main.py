import pygame

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((800,800))
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()