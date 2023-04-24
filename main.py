
import pygame


pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Heheheha', False, (255, 0, 0))
run = True
x= 40
y= 40
c1 = 0 
c2 = 0
width = 50
height = 50
vel = 750
clock = pygame.time.Clock()
pos = pygame.mouse.get_pos()
img = pygame.image.load("img/menu.png").convert_alpha()
img = pygame.transform.scale(img , (1920 , 1080))
bruh =pygame.image.load("img/dingus.jpg").convert_alpha()
bruh = pygame.transform.scale(bruh , (50 , 50))
start = pygame.image.load("img/start.png").convert_alpha()
start = pygame.transform.scale(start , (200 , 200))
sky = pygame.image.load("img/Sky_1.png").convert_alpha()
sky = pygame.transform.scale(sky , (1920 , 1080))
ground = pygame.image.load("img/ground_1.png").convert_alpha()
ground = pygame.transform.scale(ground, (1920 , 1080))
hp_bar = pygame.image.load("img/ProgressBar.png").convert_alpha()
hp_bar = pygame.transform.scale(hp_bar, (850 , 500))
model_enemy1 = pygame.image.load("img/goomba.png").convert()
model_enemy2 = pygame.image.load("img/hunter.png").convert()
model_enemy3 = pygame.image.load("img/volant.png").convert()
model_bullet0= pygame.image.load("img/goomba.png").convert()
model_bullet = pygame.transform.scale_by(model_bullet0,1/4)

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = my_font.render(fps , 1, pygame.Color("RED"))
    win.blit(fps_t,(0,0))

class Boss(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.hp = 3
        self.canShoot=True
        self.dead = False
        if self.type == 1:
            self.test = True
            self.image = pygame.image.load("img/boss.png").convert()
            self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        if self.hp == 0:
            if self.dead != True:
                self.death = pygame.time.get_ticks()
            self.dead = True
            if pygame.time.get_ticks() - self.death >3000:
                self.kill()
                player1.Alive = False
        if self.rect.x > 1920-self.rect.width:
            self.x -= 300 * delta_time 
            self.rect.x = self.x
        else:
            if self.test:
                self.timer = pygame.time.get_ticks()
                self.test = False
        if self.type == 1:
            if self.rect.x <= 1920-self.rect.width and self.canShoot:
                bullet = Bullet(4,self.rect.x,self.y)
                bullet_group.add(bullet)
                self.canShoot = False
            if self.test == False:
                if pygame.time.get_ticks() - self.timer > 6000:
                    self.canShoot = True
                    self.timer = pygame.time.get_ticks()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.canShoot=True
        if self.type == 1:#mur
            self.image = model_enemy1
            self.rect = self.image.get_rect(topleft = (x,y))
        if self.type == 2:#chasseur
            self.image = model_enemy2
            self.rect = self.image.get_rect(topleft = (x,y))
        if self.type == 3:#volant
            self.image = model_enemy3
            self.rect = self.image.get_rect(topleft = (x,y))
        if self.type == 4:#sac plastique
            self.fly = True
            self.isFlying = True
            self.image = model_enemy3
            self.rect = self.image.get_rect(topleft = (x,y))
        if self.type == 5:#éolienne
            self.image = model_enemy3
            self.rect = self.image.get_rect(topleft = (x,y))


    def update(self):
        self.x -= 300 * delta_time
        self.rect.x = self.x
        if self.type == 2:
            if self.rect.x < 2000 and self.canShoot:
                for i in range(1,4,1):
                    bullet = Bullet(i,self.rect.x,self.y)
                    bullet_group.add(bullet)
                self.canShoot = False
        if self.type == 4:
            if self.rect.x < 1800:
                if self.fly:
                    self.timer = pygame.time.get_ticks()
                    self.fly = False
                if self.fly == False:
                    if self.isFlying:
                        self.y -= 500 * delta_time
                        self.rect.y = self.y
                        if pygame.time.get_ticks() - self.timer >2000:
                            self.fly = True
                            self.timer = pygame.time.get_ticks()
                            self.isFlying = False
                    else:
                        if pygame.time.get_ticks() - self.timer >2000:
                            self.fly = True
                            self.timer = pygame.time.get_ticks()
                            self.isFlying = True
        if self.type == 5:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.kill()
        if self.rect.x+5 < 0-self.rect.width:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        if self.type != 4:
            self.image = model_bullet
            self.rect = self.image.get_rect(topleft = (x,y))
        else:
            self.image = model_bullet0
            self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        if self.type == 1:
            self.x -= 800 * delta_time 
            self.y -= 400 * delta_time 
            self.rect.x = self.x
            self.rect.y = self.y
        if self.type == 2:
            self.x -= 800 * delta_time 
            self.rect.x = self.x
        if self.type == 3:
            self.x -= 800 * delta_time 
            self.y += 400 * delta_time 
            self.rect.x = self.x
            self.rect.y = self.y
        if player1.type == 1:
            if self.rect.x < 0-self.rect.width or (player1.windwall_rect.colliderect(self.rect) and keys[pygame.K_SPACE] and player1.cooldown == False and self.type != 4 and self.type != 5):
                self.kill()
        if self.type == 4:
            self.x -= 800 * delta_time 
            self.rect.x = self.x
            if player1.player_rect.y >= self.rect.y:
                self.y += 100 * delta_time 
                self.rect.y = self.y
            else:
                self.y -= 100 * delta_time 
                self.rect.y =self.y
            if player1.windwall_rect.colliderect(self.rect) and keys[pygame.K_SPACE] and player1.cooldown == False:
                boss1.hp -=1
                self.type = 5
        if self.type == 5:
            self.x += 2000 * delta_time 
            self.rect.x = self.x
            if self.rect.colliderect(boss1.rect):
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
        self.cooldown = False
        if self.type == 1: #Eagle
            self.player_surf0 = pygame.image.load("img/pitie.png").convert()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/3)
            self.player_rect = self.player_surf.get_rect(topleft = (x,y))
            self.height = self.player_surf.get_height()
            self.windwall_surf = pygame.image.load("img/Yasuo Windwall.jpg").convert()
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
                if pygame.time.get_ticks() - self.timer > 2000:
                    self.cooldown = False
map = img.get_rect(topleft = (0,0))
start_rect1 = start.get_rect(topleft = (1675 , 375))
start_rect2 = start.get_rect(topleft = (1425 , 125))
player1 = Player(1)
player2 = Player(2)
player3 = Player(3)
player4 = Player(4)
player5 = Player(5)
playerList = [player1,player2,player3,player4,player5]
enemy1 = Enemy(2,1500,700)
enemy2 = Enemy(1,4000,0)
enemy3 = Enemy(2,6000,700)
enemy4 = Enemy(3,8000,0)
enemy5 = Enemy(2,1500,700)
enemy6 = Enemy(1,4000,0)
enemy7 = Enemy(2,6000,700)
enemy8 = Enemy(3,8000,0)
enemy9 = Enemy(4,3000,700)
enemy10 = Enemy(5,5000,700)
enemyList1 = [enemy1,enemy2,enemy3,enemy4]
enemyList2 = [enemy5,enemy6,enemy7,enemy8,enemy9,enemy10]
allEnemyLists = [enemyList1,enemyList2]
boss1 = Boss(1,10000,500)
bossList = [boss1,boss1,boss1,boss1,boss1]
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
menu = True
ticks = 0
level_selected = 1
level1_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(1750,450,50,50))
level2_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(1500,200,50,50))
timer_windwall = 0
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if menu:
        while(menu):
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            point = pygame.mouse.get_pos()
            dingus = bruh.get_rect(topleft = (x,y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    menu = False
                if dingus.colliderect(level1_rect):
                    if keys[pygame.K_SPACE]:
                       menu = False
                       level_selected = 0
                if dingus.colliderect(level2_rect):
                    if keys[pygame.K_SPACE]:
                        menu = False
                        level_selected = 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or keys[pygame.KMOD_ALT] and keys[pygame.K_F4]:
                run = False
            if keys[pygame.K_LEFT] and x > 5:
                        x-=vel * delta_time
            if keys[pygame.K_RIGHT] and x < 1915:
                        x+=vel * delta_time
            if keys[pygame.K_UP] and y > 5:
                        y -= vel * delta_time
            if keys[pygame.K_DOWN] and y < 1075:
                        y += vel * delta_time
            if keys[pygame.K_ESCAPE]:
                run = False
                menu = False
            win.blit(img, map)
            win.blit(bruh, dingus)
            level1_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(1750,450,50,50))
            level2_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(1500,200,50,50))
            if dingus.colliderect(level1_rect):
                win.blit(start, start_rect1)
            if dingus.colliderect(level2_rect):
                win.blit(start, start_rect2)
            pygame.display.update()
    player_group.add(playerList[level_selected])
    for j in range(len(allEnemyLists[level_selected])):
            enemy_group.add(allEnemyLists[level_selected][j])
    boss_group.add(bossList[level_selected])
    if menu != True:
        player1 = playerList[level_selected]
        while player1.Alive:
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    player1.Alive = False
            bullet_group.update()
            player_group.update()
            enemy_group.update()
            boss_group.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                player1.Alive = False
                run = False
            if keys[pygame.K_LEFT] and player1.player_rect.x > 0:
                player1.player_rect.x-=vel * delta_time
            if keys[pygame.K_RIGHT] and player1.player_rect.x < 200:
                player1.player_rect.x+=vel * delta_time
            if keys[pygame.K_UP] and player1.player_rect.y > 0:
                player1.player_rect.y -= vel * delta_time
                for i in range(len(allEnemyLists[level_selected])):
                    if allEnemyLists[level_selected][i].type != 2 and allEnemyLists[level_selected][i].type != 3:
                        if player1.player_rect.colliderect(allEnemyLists[level_selected][i].rect):
                            player1.player_rect.y += vel * delta_time
            if keys[pygame.K_DOWN]and player1.player_rect.y < 1080 - player1.height:
                player1.player_rect.y += vel * delta_time
                for i in range(len(allEnemyLists[level_selected])):
                    if allEnemyLists[level_selected][i].type != 2:
                        if player1.player_rect.colliderect(allEnemyLists[level_selected][i].rect):
                            player1.player_rect.y -= vel
                            
            win.fill((0,0,0))
            win.blit(sky, (0, 0)) # elle est mal place 
            win.blit(ground, (0, 0))
            win.blit(hp_bar, (0, -100)) # elle est mal placé / systeme d'hp pas implanté /pas de degat 
            for i in range(len(allEnemyLists[level_selected])):
                if allEnemyLists[level_selected][i].type != 2:
                    if player1.player_rect.colliderect(allEnemyLists[level_selected][i].rect):
                        player1.Alive=False
                enemy_group.draw(win)
            win.blit(player1.player_surf,player1.player_rect)
            bullet_group.draw(win)
            if timer_windwall != 0:
                if pygame.time.get_ticks() - timer_windwall < 500:
                    win.blit(player1.windwall_surf,player1.windwall_rect)
                else:
                    timer_windwall = 0

            if player1.type == 1 and keys[pygame.K_SPACE] and player1.cooldown == False:
                timer_windwall = pygame.time.get_ticks()
            boss_group.draw(win)

            fps_counter()
            pygame.display.update()
pygame.quit()