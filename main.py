import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Heheheha', False, (255, 0, 0))
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
run = True
x= 40
y= 40
width = 50
height = 50
vel = 15
class Enemy():
    def __init__(self,type,x,y):
        self.type = type
        self.x = x
        self.y = y
        if self.type == 1:
            self.enemy_surf = pygame.image.load("img/goomba.png").convert()
            self.enemy_rect = self.enemy_surf.get_rect(topleft = (x,700))

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
enemy1 = Enemy(1,5000,5000)
enemyList = [enemy1]
alive = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    while alive:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            alive = False
        if keys[pygame.K_LEFT] and player1.player_rect.x > 0:
            player1.player_rect.x-=vel
        if keys[pygame.K_RIGHT] and player1.player_rect.x < 200:
            player1.player_rect.x+=vel
        if keys[pygame.K_UP] and player1.player_rect.y > 0:
            player1.player_rect.y -= vel
            for i in range(len(enemyList)):
                if player1.player_rect.colliderect(enemyList[i].enemy_rect):
                    player1.player_rect.y += vel
        if keys[pygame.K_DOWN]and player1.player_rect.y < 1080 - player1.height:
            player1.player_rect.y += vel
            for i in range(len(enemyList)):
                if player1.player_rect.colliderect(enemyList[i].enemy_rect):
                    player1.player_rect.y -= vel
        for i in range(len(enemyList)):
            if player1.player_rect.colliderect(enemyList[i].enemy_rect):
                alive=False
        win.fill((0,0,0))
        enemy1.enemy_rect.x -= 50
        win.blit(enemy1.enemy_surf,enemy1.enemy_rect)
        win.blit(player1.player_surf,player1.player_rect)
        pygame.display.update()
    
pygame.quit()