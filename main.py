import pygame

def __init__(self):
    pygame.init()
    pygame.display.set_caption("masterclass")
    win=pygame.display.set_mode((1920,1080))
    run = True
    x= 40
    y= 40
    width = 50
    height = 50
    vel = 15
    self.img = pygame.image.load("img/dingus.jpg").convert_alpha()
    self.dingus = self.img.get_rect()

    def render(self,x,y, win):
        
        while run:
            pygame.time.delay(100)
            win.bLit(self.img, self.dingus)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or keys[pygame.KMOD_ALT] and keys[pygame.K_F4]:
                run = False
            if keys[pygame.K_LEFT] and x > 5:
                x-=vel
            if keys[pygame.K_RIGHT] and x < 800:
                x+=vel
            if keys[pygame.K_UP] and y > 5:
                y -= vel
            if keys[pygame.K_DOWN] and y < 800:
                y += vel
            win.fill((0,0,0))
            pygame.display.update()
        pygame.quit()