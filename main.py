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
class Boss(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.hp = 3
        self.canShoot=True
        if self.type == 1:
            self.test = True
            self.surf = pygame.image.load("img/boss.png").convert()
            self.rect = self.surf.get_rect(topleft = (x,y))
    def update(self):
        if self.rect.x > 1920-self.rect.width:
            self.rect.x -= 50
        else:
            if self.test:
                self.timer = pygame.time.get_ticks()
                self.test = False
        if self.type == 1:
            if self.rect.x < 1920-self.rect.width and self.canShoot:
                bullet = Bullet(4,self.rect.x,self.y)
                bullet_group.add(bullet)
                self.canShoot = False
            if self.test == False:
                if pygame.time.get_ticks() - self.timer >10000:
                    self.canShoot = True
                    self.timer = pygame.time.get_ticks()
        if self.hp == 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.canShoot=True
        if self.type == 1:#mur
            self.surf = pygame.image.load("img/goomba.png").convert()
            self.rect = self.surf.get_rect(topleft = (x,y))
        if self.type == 2:#chasseur
            self.surf = pygame.image.load("img/chasseur.png").convert()
            self.rect = self.surf.get_rect(topleft = (x,y))
        if self.type == 3:#volant
            self.surf = pygame.image.load("img/volant.png").convert()
            self.rect = self.surf.get_rect(topleft = (x,y))
    def update(self):
        self.rect.x -= 50
        if self.type == 2:
            if self.rect.x < 2000 and self.canShoot:
                for i in range(1,4,1):
                    bullet = Bullet(i,self.rect.x,self.y)
                    bullet_group.add(bullet)
                self.canShoot = False
        if self.rect.x < 0-self.rect.width:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        if self.type != 4:
            self.image0 = pygame.image.load("img/goomba.png").convert()
            self.image = pygame.transform.scale_by(self.image0,1/4)
            self.rect = self.image.get_rect(topleft = (x,y))
        else:
            self.image = pygame.image.load("img/goomba.png").convert()
            self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        if self.type == 1:
            self.rect.x -= 75
            self.rect.y -= 25
        if self.type == 2 or self.type == 4 :
            self.rect.x -= 75
        if self.type == 3:
            self.rect.x -= 75
            self.rect.y += 25
        if self.rect.x < 0-self.rect.width or (player1.windwall_rect.colliderect(self.rect) and keys[pygame.K_SPACE]):
            self.kill()
        if player1.player_rect.colliderect(self.rect):
            player1.Alive = False
        
class Player(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.x = 50
        self.y = 50
        self.Alive = True
        if self.type == 1: #Eagle
            self.player_surf0 = pygame.image.load("img/pitie.png").convert()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/3)
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
        if self.type == 2:#Oiseau 2
            self.player_surf = pygame.image.load("img/pitie.png").convert()
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
        self.windwall_surf = pygame.image.load("img/goomba.png").convert()
        self.windwall_rect = self.windwall_surf.get_rect(topleft = (self.player_rect.x+self.player_rect.width,self.player_rect.y))
player1 = Player(1)
player2 = Player(2)
player3 = Player(3)
player4 = Player(4)
player5 = Player(5)
playerList = [player1,player2,player3,player4,player5]
enemy1 = Enemy(2,1500,700)
enemy2 = Enemy(1,4000,0)
enemy3 = Enemy(2,6000,1400)
enemy3 = Enemy(3,8000,700)
enemyList = [enemy1,enemy2,enemy3]
boss1 = Boss(1,10000,500)
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
player_group.add(player1)
for i in range(len(enemyList)):
    enemy_group.add(enemyList[i])
boss_group.add(boss1)
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    while player1.Alive:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                player1.Alive = False
        player_group.update()
        bullet_group.update()
        enemy_group.update()
        boss_group.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            player1.Alive = False
            run = False
        if keys[pygame.K_LEFT] and player1.player_rect.x > 0:
            player1.player_rect.x-=vel
        if keys[pygame.K_RIGHT] and player1.player_rect.x < 200:
            player1.player_rect.x+=vel
        if keys[pygame.K_UP] and player1.player_rect.y > 0:
            player1.player_rect.y -= vel
            for i in range(len(enemyList)):
                if player1.player_rect.colliderect(enemyList[i].rect):
                    player1.player_rect.y += vel
        if keys[pygame.K_DOWN]and player1.player_rect.y < 1080 - player1.height:
            player1.player_rect.y += vel
            for i in range(len(enemyList)):
                if player1.player_rect.colliderect(enemyList[i].rect):
                    player1.player_rect.y -= vel
        win.fill((0,0,0))
        for i in range(len(enemyList)):
            if player1.player_rect.colliderect(enemyList[i].rect):
                player1.Alive=False
            win.blit(enemyList[i].surf,enemyList[i].rect)
        win.blit(player1.player_surf,player1.player_rect)
        if player1.type == 1 and keys[pygame.K_SPACE]:
            win.blit(player1.windwall_surf,player1.windwall_rect)
        win.blit(boss1.surf,boss1.rect)
        bullet_group.draw(win)
        pygame.display.update()
    
pygame.quit()
#