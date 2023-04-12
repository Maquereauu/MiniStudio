import pygame

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 40
y= 40
width = 50
height = 50
vel = 15
enemy_surf = pygame.image.load("img/goomba.png").convert()
enemy_rect = enemy_surf.get_rect(topleft = (x,700))
class Enemy():
    def __init__(self,type,x,y):
        self.type = type
        self.x = x
        self.y = y
        if self.type == 1:
            pygame.draw.rect(win,(255,0,0),(100,100,width,height))
class Player():
    def __init__(self,type):
        self.type = type
        self.x = 50
        self.y = 50
        if self.type == 1:
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 2:
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 3:
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 4:
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 5:
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
player1 = Player(1)
player2 = Player(2)
player3 = Player(3)
player4 = Player(4)
player5 = Player(5)
playerList = [player1,player2,player3,player4,player5]
enemy1 = Enemy(1,500,500)
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT] and player1.player_rect.x > 0:
        player1.player_rect.x-=vel
    if keys[pygame.K_RIGHT] and player1.player_rect.x < 200:
        player1.player_rect.x+=vel
    if keys[pygame.K_UP] and player1.player_rect.y > 0:
        player1.player_rect.y -= vel
    if keys[pygame.K_DOWN]and player1.player_rect.y < 1080 - player1.height:
        player1.player_rect.y += vel
    win.fill((0,0,0))
    win.blit(enemy_surf,enemy_rect)
    win.blit(player1.player_surf,player1.player_rect)
    pygame.display.update()
pygame.quit()