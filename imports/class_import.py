import pygame
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
class Boss(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.hp = 3
        self.canShoot=True
        self.dead = False
        self.coinTimer = 0
        self.tookDamage = False
        if self.type == 1:
            self.test = True
            self.image0 = pygame.image.load("img/tree.png").convert_alpha()
            self.image = pygame.transform.scale(self.image0 , (1000 , 1080))
            self.rect = self.image.get_rect(topleft = (x,y))
        if self.type == 2:
            self.test = True
            self.image0 = pygame.image.load("img/boss.png").convert()
            self.image = pygame.transform.scale(self.image0 , (1000 , 1080))
            self.rect = self.image.get_rect(topleft = (x,y))
            self.canDropCoin = True
    def update(self):
        if self.hp == 0:
            if self.dead != True:
                self.tookDamage = True
                self.death = pygame.time.get_ticks()
            self.dead = True
            if pygame.time.get_ticks() - self.death >3000:
                self.kill()
                player1.Alive = False
        if self.rect.x > 1920-self.rect.width*0.75:
            self.x -= 300 * delta_time * speed
            self.rect.x = self.x
        else:
            if self.test:
                self.timer = pygame.time.get_ticks()
                self.coinTimer = pygame.time.get_ticks()
                self.test = False
                self.canDropCoin = True
        if self.type == 1:
            if self.rect.x <= 1920-self.rect.width*0.75 and self.canShoot:
                bullet = Bullet(4,self.rect.x,1080/4)
                bullet_group.add(bullet)
                self.canShoot = False
        if self.type == 2:
            if self.rect.x <= 1920-self.rect.width*0.75 and self.canShoot:
                wall = Enemy(6,self.rect.x,self.y)
                enemyList2.append(wall)
                enemy_group.add(wall)
                self.canShoot = False
            if self.rect.x <= 1920-self.rect.width and pygame.time.get_ticks() - self.coinTimer > 9000 and self.canDropCoin == True:
                piece = Coin(1,self.rect.x,self.y)
                coinList.append(piece)
                coin_group.add(piece)
                self.canDropCoin = False
        if self.test == False:
            if pygame.time.get_ticks() - self.timer > 6000:
                self.canShoot = True
                self.timer = pygame.time.get_ticks()

class Coin(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.type = type
        self.x = x
        self.y = y
        self.isdead = False
        if self.type == 1:  #dash level 2
            self.image = model_coin
            self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        self.x -= 300 * delta_time * speed
        self.rect.x = self.x
        if self.rect.x+5 < 0-self.rect.width:
            self.kill()
            self.isdead = True

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
            self.damage = 1000
        if self.type == 2:#chasseur
            self.image = model_enemy2
            self.rect = self.image.get_rect(topleft = (x,y))
            self.damage = 0
        if self.type == 3:#volant
            self.image = model_enemy3
            self.rect = self.image.get_rect(topleft = (x,y))
            self.damage = 50
        if self.type == 4:#sac plastique
            self.fly = True
            self.isFlying = True
            self.image = model_enemy4_1
            self.rect = self.image.get_rect(topleft = (x,y))
            self.damage = 30
        if self.type == 5:#éolienne
            self.image = model_enemy5
            self.rect = self.image.get_rect(topleft = (x,y))
            self.damage = 1000
        if self.type == 6:#mur cassable
            self.image = model_enemy6
            self.rect = self.image.get_rect(topleft = (x,y))
            self.damage = 100

    def update(self):
        self.x -= 300 * delta_time * speed
        self.rect.x = self.x
        if self.type == 2:
            if self.rect.x < 1920-self.rect.width and self.canShoot:
                for i in range(1,4,1):
                    bullet = Bullet(i,self.rect.x,self.y)
                    bullet_group.add(bullet)
                self.canShoot = False
        if self.type == 4:
            if self.rect.x < 1920-self.rect.width:
                self.y += math.sin(pygame.time.get_ticks() * 0.5 * math.pi / (40 * 2))
                self.rect.y = self.y
                if self.fly:
                    self.timer = pygame.time.get_ticks()
                    self.fly = False
                if self.fly == False:
                    if self.isFlying:
                        self.y -= 250 * delta_time * speed
                        self.image = model_enemy4_2
                        self.rect.y = self.y
                        if pygame.time.get_ticks() - self.timer >2000:
                            self.fly = True
                            self.timer = pygame.time.get_ticks()
                            self.isFlying = False
                            self.image = model_enemy4_1
                    else:
                        if pygame.time.get_ticks() - self.timer >2000:
                            self.fly = True
                            self.timer = pygame.time.get_ticks()
                            self.isFlying = True
        if self.type != 2:
            if player1.player_rect.colliderect(self.rect):
                player1.hp -= self.damage
        if self.type == 5:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.kill()
        if self.type == 6:
            if player1.windwall_rect.colliderect(self.rect) and ((keys[pygame.K_SPACE] and player1.cooldown == False) or (pygame.time.get_ticks() - timer_dash < 1000 and pygame.time.get_ticks() - timer_dash != 0)):
                self.kill()
                boss2.timer = pygame.time.get_ticks()
                if boss2.rect.x <= 1920-self.rect.width*0.75:
                    boss2.hp -= 1
            if player1.player_rect.colliderect(self.rect):
                self.kill()
        if self.rect.x+5 < 0-self.rect.width:
            if self.type == 6:
                boss2.timer = pygame.time.get_ticks()
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
            self.image = model_fireball
            self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        if self.type == 1:
            self.x -= 800 * delta_time * speed
            self.y -= 400 * delta_time * speed
            self.rect.x = self.x
            self.rect.y = self.y
        if self.type == 2:
            self.x -= 800 * delta_time * speed
            self.rect.x = self.x
        if self.type == 3:
            self.x -= 800 * delta_time * speed
            self.y += 400 * delta_time * speed
            self.rect.x = self.x
            self.rect.y = self.y
        if player1.type == 1:
            if self.rect.x < 0-self.rect.width or (player1.windwall_rect.colliderect(self.rect) and ((keys[pygame.K_SPACE] and player1.cooldown == False) or (pygame.time.get_ticks() - timer_windwall < 500 and pygame.time.get_ticks() - timer_windwall != 0)) and self.type != 4  and self.type != 5):
                self.kill()
        if self.type == 4:
            self.x -= 800 * delta_time * speed
            self.rect.x = self.x
            self.y += math.sin(pygame.time.get_ticks() * 0.5 * math.pi / 40)
            self.rect.y = self.y
            if player1.player_rect.y >= self.rect.y:
                self.y += 100 * delta_time * speed
                self.rect.y = self.y
            else:
                self.y -= 100 * delta_time * speed
                self.rect.y =self.y
            if player1.windwall_rect.colliderect(self.rect) and ((keys[pygame.K_SPACE] and player1.cooldown == False) or (pygame.time.get_ticks() - timer_windwall < 500 and pygame.time.get_ticks() - timer_windwall != 0)):
                boss1.hp -=1
                self.type = 5
        if self.type == 5:
            self.x += 1000 * delta_time  * speed
            self.rect.x = self.x
            self.image = model_fireball2
            if self.rect.colliderect(boss1.rect):
                self.kill()
        if player1.player_rect.colliderect(self.rect):
            player1.hp -= 25 
            self.kill()
        
class Player(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.x = 100
        self.y = 700
        self.Alive = True
        self.cooldown = False
        self.timer = 0
        if self.type == 1: #Eagle
            self.max_hp = 100
            self.hp = self.max_hp
            self.player_surf0 = pygame.image.load("img/Bird.png").convert_alpha()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/3)
            self.player_rect = self.player_surf.get_rect(topleft = (self.x,self.y))
            self.height = self.player_surf.get_height()
            self.windwall_surf = pygame.image.load("img/WindWall.png").convert_alpha()
            self.windwall_surf = pygame.transform.scale(self.windwall_surf , (539/3 , 386/3))
            self.windwall_rect = self.windwall_surf.get_rect(topleft = (self.player_rect.x,self.player_rect.y))
        if self.type == 2:#Oiseau 2
            self.max_hp = 80
            self.hp = self.max_hp
            self.player_surf0 = pygame.image.load("img/Bird.png").convert_alpha()
            self.player_surf = pygame.transform.scale_by(self.player_surf0,1/4)
            self.player_rect = self.player_surf.get_rect(topleft = (self.x,self.y))
            self.height = self.player_surf.get_height()
            self.windwall_surf = pygame.image.load("img/WindWall.png").convert_alpha()
            self.windwall_surf = pygame.transform.scale(self.windwall_surf , (539/3 , 386/3))
            # self.windwall_surf.set_alpha(256)
            self.windwall_rect = self.windwall_surf.get_rect(topleft = (self.player_rect.x,self.player_rect.y))
        if self.type == 3:#Oiseau 3
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (self.x,self.y))
            self.height = self.player_surf.get_height()
        if self.type == 4:#Oiseau 4
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (self.x,self.y))
            self.height = self.player_surf.get_height()
        if self.type == 5:#Oiseau 5
            self.player_surf = pygame.image.load("img/pitie.png").convert()
            self.player_rect = self.player_surf.get_rect(topleft = (self.x,self.y))
            self.height = self.player_surf.get_height()

    def update(self):
        if self.type == 1:
            self.windwall_rect.x = self.player_rect.x+self.player_rect.width
            self.windwall_rect.y = self.player_rect.y
            if keys[pygame.K_SPACE]:
                if self.cooldown == False:
                    self.timer = pygame.time.get_ticks()
                    self.cooldown = True
                elif pygame.time.get_ticks() - self.timer > 2000:
                    self.cooldown = False
        if self.type == 2:
            self.windwall_rect.x = self.player_rect.x+self.player_rect.width
            self.windwall_rect.y = self.player_rect.y
            if self.cooldown == True:   
                if pygame.time.get_ticks() - self.timer > 2000:
                    self.cooldown = False
img = pygame.image.load("img/map.png").convert_alpha()
img = pygame.transform.scale(img , (1920 , 1080))
bruh =pygame.image.load("img/ship.png").convert_alpha()
bruh = pygame.transform.scale(bruh , (50 , 75))
bruh_0 = pygame.transform.rotate(bruh , 0)
bruh_1 = pygame.transform.rotate(bruh , 90)
bruh_15 = pygame.transform.rotate(bruh , 45)
bruh_25 = pygame.transform.rotate(bruh , 135)
bruh_2 = pygame.transform.rotate(bruh , 180)
bruh_35 = pygame.transform.rotate(bruh , 225)
bruh_3 = pygame.transform.rotate(bruh , 270)
bruh_4 = pygame.transform.rotate(bruh , 315)
play = pygame.image.load("img/play.png").convert_alpha()
play = pygame.transform.scale(play, (75,60))
play_rect1 = play.get_rect(topleft = (598,740))
play_rect2 = play.get_rect(topleft = (418,510))
start = pygame.image.load("img/start.png").convert_alpha()
start = pygame.transform.scale(start , (200 , 200))
background = pygame.image.load("img/back.png").convert_alpha()
background = pygame.transform.scale(background, (1920 * 3 , 1080))
hp_bar = pygame.image.load("img/ProgressBar.png").convert_alpha()
hp_bar = pygame.transform.scale(hp_bar, (500 , 300))
model_enemy1 = pygame.image.load("img/wall.png").convert_alpha()
model_enemy1 = pygame.transform.scale(model_enemy1,(600 , 450))
model_enemy2 = pygame.image.load("img/hunter.png").convert_alpha()
model_enemy2 = pygame.transform.scale(model_enemy2,(650 , 400))
model_enemy3 = pygame.image.load("img/plane.png").convert_alpha()
model_enemy3 = pygame.transform.scale(model_enemy3,(400 , 400))
model_enemy4 = pygame.image.load("img/Plastic_bag.png").convert_alpha()
model_enemy4 = pygame.transform.scale(model_enemy4,(200 , 200))
model_enemy4_1 = pygame.transform.rotate(model_enemy4, 270)
model_enemy4_2 = pygame.transform.rotate(model_enemy4, 225)
model_enemy5 = pygame.image.load("img/wind_turbine.png").convert_alpha()
model_enemy6 = pygame.image.load("img/broken_wall.png").convert_alpha()
model_enemy6 = pygame.transform.scale(model_enemy6,(600 , 450))
model_bullet0 = pygame.image.load("img/Bullet.png").convert_alpha()
model_bullet = pygame.transform.scale_by(model_bullet0,1/4)
model_fireball = pygame.image.load("img/fireball.png").convert_alpha()
model_fireball = pygame.transform.scale_by(model_fireball,1/2)
model_fireball = pygame.transform.rotate(model_fireball, 45)
model_fireball2 = pygame.transform.rotate(model_fireball, 180)
icon_windwall = pygame.image.load("img/WindWall.png").convert_alpha()
icon_windwall = pygame.transform.scale(icon_windwall, (50 , 50))
icon_windwall.set_alpha(150)
skip_button = pygame.image.load("img/skip.png").convert_alpha()
skip_button = pygame.transform.scale(skip_button, (50 , 50))
pause_button = pygame.image.load("img/pause.png").convert_alpha()
pause_button = pygame.transform.scale(pause_button, (50 , 50))
took_damage = pygame.Surface((1000,1080))
took_damage.set_alpha(128)
took_damage.fill((255,0,0))
dialog_box = pygame.image.load("img/dialog_box.png").convert_alpha()
dialog_box = pygame.transform.scale(dialog_box, (1000 , 325))
dialog = pygame.transform.scale(dialog_box , (750 , 320))
valider = pygame.image.load("img/valider.png").convert_alpha()
valider = pygame.transform.scale(valider ,(100,100))
refuser = pygame.image.load("img/refuser.png").convert_alpha()
refuser = pygame.transform.scale(refuser , (100,100))
robot_model1 = pygame.image.load("img/little_robot.png").convert_alpha()
robot_model1 = pygame.transform.scale(robot_model1, (900 , 600))
robot_model2 = pygame.image.load("img/little_robot_happy.png").convert_alpha()
robot_model2 = pygame.transform.scale(robot_model2, (800 , 600))
robot_model3 = pygame.image.load("img/little_robot_sad.png").convert_alpha()
robot_model3 = pygame.transform.scale(robot_model3, (800 , 600))
robot_model4 = pygame.image.load("img/little_robot_idea.png").convert_alpha()
robot_model4 = pygame.transform.scale(robot_model4, (900 , 600))
red_cross = pygame.image.load("img/Red_Cross.png").convert_alpha()
red_cross = pygame.transform.scale(red_cross, (60 , 60))
x_background = 0
speed = 1
model_coin0 = pygame.image.load("img/coin.png").convert_alpha()
model_coin = pygame.transform.scale_by(model_coin0,1/4)
piece =  pygame.transform.scale(model_coin0, (50 , 50))
map = img.get_rect(topleft = (0,0))
start_rect1 = start.get_rect(topleft = (535 , 670))
start_rect2 = start.get_rect(topleft = (345 , 440))
menu = True
ticks = 0
level_selected = 1
level1_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(610,745,50,50))
level2_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(430,515,50,50))