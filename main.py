import pygame
import sys

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 40
y= 40
c1 = 0 
c2 = 0
width = 50
height = 50
vel = 15
CLOCK = pygame.time.Clock()
pos = pygame.mouse.get_pos()
img = pygame.image.load("img/menu.png").convert_alpha()
img = pygame.transform.scale(img , (1920 , 1080))
bruh =pygame.image.load("img/dingus.jpg").convert_alpha()
bruh = pygame.transform.scale(bruh , (50 , 50))
class Rect(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.c1 = c1
        self.c2 = c2
        self.canShoot=True

    def update(self):
        self.rect.x -= 5
        if self.type == 2:
            if self.rect.x < 2000 and self.canShoot:
                self.canShoot = False
        if self.rect.x+5 < 0-self.rect.width:
            self.kill()
def __init__(self,type):
        super().__init__()
        self.type = type
        self.x = 50
        self.y = 50
        self.Alive = True
        self.cooldown = False
        if self.type == 1: #Eagle
            self.player_surf0 = pygame.image.load("img/pitie.png").convert()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/3)
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
            self.windwall_surf = pygame.image.load("img/goomba.png").convert()
            self.windwall_rect = self.windwall_surf.get_rect(topleft = (self.player_rect.x,self.player_rect.y))
        if self.type == 2:#Oiseau 2
            self.player_surf0 = pygame.image.load("img/pitie.png").convert()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/4)
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 3:#Oiseau 3
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 4:#Oiseau 4
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 5:#Oiseau 5
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()

        def update(self):
            if self.type == 1:
                self.windwall_rect.x = self.player_rect.x+self.player_rect.width
                self.windwall_rect.y = self.player_rect.y
                if keys[pygame.K_SPACE]:
                    if self.cooldown == False:
                        self.timer = pygame.time.get_ticks()
                        self.cooldown = True
                    if pygame.time.get_ticks() - self.timer > 3000:
                        self.cooldown = False
level1_surf = pygame.image.load("img/goomba.png").convert()
level1_rect = level1_surf.get_rect(topleft = (x,y))
level3_surf = pygame.image.load("img/goomba.png").convert()
level3_rect = level3_surf.get_rect(topleft = (x+500,y))
rect1 = Rect(2,1500,700)
while run:
    map = img.get_rect(topleft = (0,0))
    dingus = bruh.get_rect(topleft = (x,y))
    pygame.time.delay(1)
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
    if menu:
        while(menu):
            point = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and level1_rect.collidepoint(point):
                        menu = False
                        level_selected = 0
                    if event.button == 1 and level3_rect.collidepoint(point):
                        menu = False
                        level_selected = 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
                menu = False
            win.blit(level1_surf,level1_rect)
            win.blit(level3_surf,level3_rect)
            pygame.display.update()
    win.fill((0,0,0))
    win.blit(img, map)
    rect  = pygame.draw.rect(win,color=(156,0,36), rect=(800,800,50,50))
    win.blit(bruh , dingus)
    CLOCK.tick(60)
    pygame.display.update()
pygame.quit()