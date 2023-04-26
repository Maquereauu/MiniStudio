import pygame
import math

pygame.init()
pygame.display.set_caption("masterclass")
win=pygame.display.set_mode((1920,1080))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Heheheha', False, (255, 0, 0))
run = True
lose = False
fin = False
c1 = 0 
c2 = 0
width = 50
height = 50
vel = 750
nb_dash = 0
clock = pygame.time.Clock()
pos = pygame.mouse.get_pos()
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
map = img.get_rect(topleft = (0,0))
start_rect1 = start.get_rect(topleft = (535 , 670))
start_rect2 = start.get_rect(topleft = (345 , 440))
menu = True
ticks = 0
level_selected = 1
level1_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(610,745,50,50))
level2_rect  = pygame.draw.rect(win,color=(156,0,36), rect=(430,515,50,50))
timer_windwall = 0
timer_dash = 0
pauseScreen = False
Tutorial = True
while run:
    x = 40
    y = 40
    nb_dash = 0
    background_x = 0
    background2_x = 1920*3
    player_1 = Player(1)
    player_2 = Player(2)
    player_3 = Player(3)
    player_4 = Player(4)
    player_5 = Player(5)
    playerList = [player_1,player_2,player_3,player_4,player_5]
    enemy1 = Enemy(2,2000,700)
    enemy2 = Enemy(3,4000,0)
    enemy3 = Enemy(4,5500,850)
    enemy4 = Enemy(1,7000,-100)
    enemy5 = Enemy(2,7500,700)
    enemy6 = Enemy(1,9000,700)
    enemy7 = Enemy(3,10500,0)
    enemy8 = Enemy(2,12000,700)
    #niveau 2
    enemy9 = Enemy(6,2000,700)
    enemy18 = Enemy(1,3000,-100)
    enemy10 = Enemy(5,3000,400)
    enemy11 = Enemy(4,5500,850)
    enemy12 = Enemy(1,7000,-100)
    enemy13 = Enemy(5,7000,400)
    enemy14 = Enemy(2,7500,700)
    enemy15 = Enemy(1,9000,700)
    enemy16 = Enemy(3,10500,0)
    enemy17 = Enemy(2,12000,700)
    coin1 = Coin(1,3500, 100)
    coin2 = Coin(1,4000, 50)
    coin3 = Coin(1,5000, 700)
    coin4 = Coin(1,5600, 50)
    coin5 = Coin(1,1000, 500)
    coinList = [coin1, coin2, coin3, coin4, coin5]
    enemyList1 = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8]
    enemyList2 = [enemy9,enemy18,enemy10,enemy11,enemy12,enemy13,enemy14,enemy15,enemy16,enemy17]
    allEnemyLists = [enemyList1,enemyList2]
    boss1 = Boss(1,15000,0)
    boss2 = Boss(2,15000,0)
    bossList = [boss1,boss2,boss1,boss1,boss1]
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    timer_windwall = 1
    ship = bruh.get_rect(topleft = (x,y))
    Tutorial = True
    first = True
    first2 = True
    first3 = True
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if menu:
        while(menu):
            preGame = True
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            point = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x > 5:
               x-=vel * delta_time
               bruh=bruh_1
               ship = bruh_1.get_rect(topleft = (x,y))
            if keys[pygame.K_RIGHT] and x < 1915:
               x+=vel * delta_time
               bruh = bruh_3
               ship = bruh_3.get_rect(topleft = (x,y))
            if keys[pygame.K_UP] and y > 5:
               y -= vel * delta_time
               bruh = bruh_0
               ship = bruh.get_rect(topleft = (x,y))
            if keys[pygame.K_DOWN] and y < 1075:
                y += vel * delta_time
                ship = bruh_2.get_rect(topleft = (x,y))
                bruh = bruh_2
            if keys[pygame.K_LEFT] and x > 5 and keys[pygame.K_UP] and y > 5 and x > 5:
               x-=vel * delta_time
               y -= vel * delta_time
               bruh=bruh_15
               ship = bruh_15.get_rect(topleft = (x,y))
            if keys[pygame.K_RIGHT] and x > 5 and keys[pygame.K_UP] and y > 5 and x < 1915:
               x+=vel * delta_time
               y -= vel * delta_time
               bruh=bruh_4
               ship = bruh_4.get_rect(topleft = (x,y))
            if keys[pygame.K_RIGHT] and x > 5 and keys[pygame.K_DOWN] and y < 1075 and x < 1915:
               x+=vel * delta_time
               y += vel * delta_time
               bruh=bruh_35
               ship = bruh_35.get_rect(topleft = (x,y))
            if keys[pygame.K_LEFT] and x > 5 and keys[pygame.K_DOWN] and y < 1075 and x > 5:
               x-=vel * delta_time
               y += vel * delta_time
               bruh=bruh_25
               ship = bruh_25.get_rect(topleft = (x,y))
            if keys[pygame.K_ESCAPE]:
                run = False
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if ship.colliderect(level1_rect):
                    if keys[pygame.K_SPACE]:
                       menu = False
                       level_selected = 0
                if ship.colliderect(level2_rect):
                    if keys[pygame.K_SPACE]:
                        menu = False
                        level_selected = 1
            win.blit(img, map)
            win.blit(bruh, ship)
            level1_rect  = win.blit(play, play_rect1)
            level2_rect  = win.blit(play, play_rect2)
            if ship.colliderect(level1_rect):
                win.blit(start, start_rect1)
                win.blit(dialog , (735,605))
                win.blit(robot_model1 , (955, 325))
                win.blit(valider , (1075 , 800))
                if valider.get_rect(topleft = (1075,800)).collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    menu = False
                    level_selected = 0
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((0,0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((0,0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
                text_level1 = my_font.render("Souhaites tu lancer le premier niveau ?", 1, pygame.Color("BLACK"))
                win.blit(text_level1 , (750 , 700))
            if ship.colliderect(level2_rect):
                win.blit(start, start_rect2)
                win.blit(dialog , (545,375))
                win.blit(robot_model1 , (765, 65))
                win.blit(valider , (885 , 575))
                text_level1 = my_font.render("Souhaites tu lancer le second niveau ?", 1, pygame.Color("BLACK"))
                win.blit(text_level1 , (560 , 470))
                if valider.get_rect(topleft = (885,575)).collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                    menu = False
                    level_selected = 1
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((0,0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((0,0,0))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    win.fill((255,255,255))
                    pygame.display.flip()
                    pygame.time.delay(100)
            pygame.display.update()
    player_group.add(playerList[level_selected])
    for j in range(len(allEnemyLists[level_selected])):
            enemy_group.add(allEnemyLists[level_selected][j])
    boss_group.add(bossList[level_selected])
    for i in range(len(coinList)):
        coin_group.add(coinList[i])
    player1 = playerList[level_selected]
    player1.hp = playerList[level_selected].max_hp
    if menu != True:
        preGameTimer = pygame.time.get_ticks()
        while preGame:
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    preGame = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
                preGame = False
            if keys[pygame.K_SPACE]:
                preGame = False
            text3_pregame = my_font.render("Appuyez sur espace pour commencer", 1, pygame.Color("WHITE"))
            if level_selected == 0:
                win.fill((135,206,235))
                win.blit(robot_model1,(1000,400))
                win.blit(player1.player_surf,(800,300))
                text1_pregame = my_font.render("Grâce à ses ailes puissantes,Serge l'aigle peut créer des bourrasques de vent,", 1, pygame.Color("WHITE"))
                text2_pregame = my_font.render("permettant ainsi de contre les balles des méchants chasseurs.", 1, pygame.Color("WHITE"))
                win.blit(text1_pregame,(400,600))
                win.blit(text2_pregame,(400,650))
                if pygame.time.get_ticks() - preGameTimer > 3000:
                    win.blit(text3_pregame,(400,850))
                pygame.display.update()
            if level_selected == 1:
                win.fill((135,206,235))
                win.blit(robot_model1,(1000,400))
                win.blit(player1.player_surf,(800,300))
                text1_pregame = my_font.render("Grâce à sa vitesse de plongé impressionnante,Paul le faucon peut utiliser son dash,", 1, pygame.Color("WHITE"))
                text2_pregame = my_font.render("lui permettant ainsi de briser les murs fissurés.", 1, pygame.Color("WHITE"))
                win.blit(text1_pregame,(400,600))
                win.blit(text2_pregame,(400,650))
                if pygame.time.get_ticks() - preGameTimer > 3000:
                    win.blit(text3_pregame,(400,850))
                pygame.display.update()
        while player1.Alive:
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            if pauseScreen != True:
                if level_selected == 0:
                    if Tutorial:
                        if allEnemyLists[level_selected][0].x <= 400:
                            Tutorial = False
                            speed = 1
                        text1 = my_font.render("Dans ce niveau tu incarneras un aigle,", 1, pygame.Color("BLACK"))
                        text2 = my_font.render("ces oiseaux étaient connus pour", 1, pygame.Color("BLACK"))
                        text3 = my_font.render("être les 'rois' du ciel", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 1500:
                            text1 = my_font.render("Oh non,un méchant chasseur!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 1300:
                            text1 = my_font.render("Ne t'en fais pas,Serge l'aigle peut", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("utiliser ses puissantes ailes", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("pour faire disparaître ces balles!", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 900:
                                text1 = my_font.render("Appuie sur espace pour envoyer", 1, pygame.Color("BLACK"))
                                text2 = my_font.render("une bourrasque de vent!", 1, pygame.Color("BLACK"))
                                text3 = my_font.render("", 1, pygame.Color("BLACK"))
                                if first:
                                    first = False
                                    pauseScreen = True
                        if allEnemyLists[level_selected][0].x <= 888:
                            text1 = my_font.render("Félicitations!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("Tu peux également esquiver les balles ainsi", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("que les obstacles en te déplaçant", 1, pygame.Color("BLACK"))
                if level_selected == 1:
                    if Tutorial:
                        if allEnemyLists[level_selected][3].x <= 2200:
                            Tutorial = False
                            speed = 1
                        text1 = my_font.render("Dans ce niveau tu incarneras un faucon,", 1, pygame.Color("BLACK"))
                        text2 = my_font.render("ces oiseaux étaient connus pour", 1, pygame.Color("BLACK"))
                        text3 = my_font.render("être les 'rapides' du ciel", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 1600:
                            text1 = my_font.render("Oh,une pièce!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("Elles permettent de restaurer tes dash.", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("1 pièce = 1 dash", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 1100:
                            text1 = my_font.render("Ne t'en fais pas,Paul le faucon peut", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("utiliser son dash pour pouvoir", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("détruire les murs fissurés", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][0].x <= 250:
                                text1 = my_font.render("Appuie sur espace pour utiliser", 1, pygame.Color("BLACK"))
                                text2 = my_font.render("ton dash!", 1, pygame.Color("BLACK"))
                                text3 = my_font.render("", 1, pygame.Color("BLACK"))
                                if first:
                                    first = False
                                    pauseScreen = True
                        if allEnemyLists[level_selected][1].x <= 500:
                            text1 = my_font.render("Fais attention!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("Une éolienne se rapproche dangereusement!", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("Clique lui dessus pour l'éliminer.", 1, pygame.Color("BLACK"))
                        if allEnemyLists[level_selected][1].x <= 250:
                            text1 = my_font.render("Fais attention!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("Une éolienne se rapproche dangereusement!", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("Clique lui dessus pour l'éliminer.", 1, pygame.Color("BLACK"))
                            if first2:
                                    first2 = False
                                    pauseScreen = True
                        if allEnemyLists[level_selected][1].x <= 248:
                            text1 = my_font.render("Félicitations!", 1, pygame.Color("BLACK"))
                            text2 = my_font.render("Tu peux également esquiver les balles ainsi", 1, pygame.Color("BLACK"))
                            text3 = my_font.render("que les obstacles en te déplaçant", 1, pygame.Color("BLACK"))
                if Tutorial:
                    speed = 0.25
                background_x -= 300 * delta_time * speed
                background2_x -= 300 * delta_time * speed
                if background_x <= (-1920)*3 + 1:
                    background_x = 1920*3
                if background2_x <= (-1920)*3 + 1:
                    background2_x = 1920*3
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        player1.Alive = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    player1.Alive = False
                    run = False
                if Tutorial != 1:
                    if keys[pygame.K_f]:
                        pauseScreen = True
                    if keys[pygame.K_LEFT] and player1.player_rect.x > 0:
                        player1.player_rect.x-=vel * delta_time * speed
                    if keys[pygame.K_RIGHT] and player1.player_rect.x < 200:
                        player1.player_rect.x+=vel * delta_time * speed
                    if keys[pygame.K_UP] and player1.player_rect.y > 0:
                        player1.player_rect.y -= vel * delta_time * speed
                        for i in range(len(allEnemyLists[level_selected])):
                            if allEnemyLists[level_selected][i].type == 1:
                                if player1.player_rect.colliderect(allEnemyLists[level_selected][i].rect):
                                    player1.player_rect.y += vel * delta_time * speed
                    if keys[pygame.K_DOWN] and player1.player_rect.y < 1080 - player1.height:
                        player1.player_rect.y += vel * delta_time * speed
                        for i in range(len(allEnemyLists[level_selected])):
                            if allEnemyLists[level_selected][i].type == 1:
                                if player1.player_rect.colliderect(allEnemyLists[level_selected][i].rect):
                                    player1.player_rect.y -= vel * 1.2 * delta_time * speed
                bullet_group.update()
                player_group.update()
                enemy_group.update()
                coin_group.update()
                boss_group.update()
                win.fill((0,0,0))
                win.blit(background, (background_x, 0)) 
                win.blit(background, (background2_x-1, 0))
                if level_selected == 1:
                    for i in range(len(coinList)):
                        if coinList[i].type == 1:
                            if player1.player_rect.colliderect(coinList[i].rect) and coinList[i].isdead == False and nb_dash < 4:
                                nb_dash += 1
                                coinList[i].isdead = True
                                coinList[i].kill()
                        if coinList[i].isdead == False :
                            win.blit(coinList[i].image,coinList[i].rect)
                        if player1.type == 2 and keys[pygame.K_SPACE] and player1.cooldown == False and nb_dash > 0 and timer_dash == 0:
                            timer_dash = pygame.time.get_ticks()
                            nb_dash -= 1
                    coin_group.draw(win)
                enemy_group.draw(win)
                win.blit(player1.player_surf,player1.player_rect)
                bullet_group.draw(win)
                if timer_dash != 0:
                    if pygame.time.get_ticks() - timer_dash < 1000:
                        player1.player_surf0 = pygame.image.load("img/Bird.gif").convert_alpha()
                        player1.player_surf = pygame.transform.scale_by(player1.player_surf0,1/4)
                    else:
                        timer_dash = 0
                        player1.player_surf0 = pygame.image.load("img/Bird.png").convert_alpha()
                        player1.player_surf = pygame.transform.scale_by(player1.player_surf0,1/4)
                if timer_windwall != 0:
                    if pygame.time.get_ticks() - timer_windwall < 500:
                        win.blit(player1.windwall_surf,player1.windwall_rect)
                    else:
                        timer_windwall = 0
                win.blit(hp_bar, (-30, -60))    
                if level_selected == 0:
                    win.blit(icon_windwall, (75, 125))
                if player1.type == 1 and keys[pygame.K_SPACE] and player1.cooldown == False:
                    timer_windwall = pygame.time.get_ticks()
                if level_selected == 0:
                    if pygame.time.get_ticks() - player1.timer < 2000:
                        win.blit(red_cross, (70, 120))
                boss_group.draw(win)
                if level_selected == 0:
                    if Tutorial:
                        win.blit(dialog_box,(500,10))
                        win.blit(text1,(600,100))
                        win.blit(text2,(600,150))
                        win.blit(text3,(600,200))
                        if allEnemyLists[level_selected][0].x <= 888:
                            win.blit(robot_model2,(600,0))
                        elif allEnemyLists[level_selected][0].x <= 1500 and allEnemyLists[level_selected][0].x >= 1300:
                            win.blit(robot_model3,(900,-275))
                        else:
                            win.blit(robot_model4,(750,0))
                if level_selected == 1:
                    if Tutorial:
                        win.blit(dialog_box,(500,10))
                        win.blit(text1,(600,100))
                        win.blit(text2,(600,150))
                        win.blit(text3,(600,200))
                        if allEnemyLists[level_selected][0].x <= 200:
                            win.blit(robot_model2,(600,0))
                        else:
                            win.blit(robot_model4,(750,0))
                if bossList[level_selected].tookDamage:
                    win.blit(took_damage, (1300,0))
                healthBar = pygame.draw.rect(win,color=(156,0,36), rect=(75,65,player1.hp*2.2,30))
                if Tutorial:
                    win.blit(skip_button,(1820,0))
                    if skip_button.get_rect(topleft = (1820,0)).collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        Tutorial = False
                        speed = 1
                if level_selected == 1:
                    if nb_dash >= 1 :
                        win.blit(piece , (75 , 125))
                        if nb_dash >= 2:
                            win.blit(piece , (130 , 125))
                            if nb_dash >= 3:
                                win.blit(piece, (185 , 125))
                                if nb_dash == 4:
                                    win.blit(piece, (240 , 125))
                if Tutorial != True:
                    win.blit(pause_button,(1870,0))
                    if pause_button.get_rect(topleft = (1870,0)).collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pauseScreen = True
                pygame.display.update()
                if player1.hp <= 0:
                    lose = True
                    break
            else:
                if Tutorial == True:
                    if first3:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            pauseScreen = False
                            first3 = False
                    else:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                player1.Alive = False
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                pauseScreen = False
                    if keys[pygame.K_ESCAPE]:
                        player1.Alive = False
                        run = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            player1.Alive = False
                else:
                    resume = pygame.draw.rect(win,color=(156,0,36), rect=(500,500,300,50))
                    retry = pygame.draw.rect(win,color=(156,0,36), rect=(1000,500,300,50))
                    lobby = pygame.draw.rect(win,color=(156,0,36), rect=(1500,500,300,50))
                    textRetry = my_font.render("Rejouer", 1, pygame.Color("WHITE"))
                    textMenu = my_font.render("Menu", 1, pygame.Color("WHITE"))
                    textResume = my_font.render("Continuer", 1, pygame.Color("WHITE"))
                    win.blit(textResume,(550,500))
                    win.blit(textRetry,(1050,500))
                    win.blit(textMenu,(1550,500))
                    for event in pygame.event.get():
                        if resume.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            pauseScreen = False
                        if retry.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            player1.Alive = False
                            pauseScreen = False
                            menu = False
                        if lobby.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            player1.Alive = False
                            menu = True
                            pauseScreen = False
                    if player1.Alive == False and pauseScreen == False and menu == False:
                        break
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        player1.Alive = False
                        run = False
                    pygame.display.update()
            if player1.Alive == False:
                menu = True
            if bossList[level_selected].hp == 0:
                fin = True
        while lose:
            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time
            win.fill((0,0,0))
            win.blit(robot_model3,(600,-100))
            textlose1 = my_font.render("Tu es mort !", 1, pygame.Color("WHITE"))
            textlose2 = my_font.render("Tu peux rejouer ou retourner au menu.", 1, pygame.Color("WHITE"))
            textRetry = my_font.render("Rejouer", 1, pygame.Color("WHITE"))
            textMenu = my_font.render("Menu", 1, pygame.Color("WHITE"))
            win.blit(textlose1,(800,600))
            win.blit(textlose2,(650,650))
            retry1 = pygame.draw.rect(win,color=(156,0,36), rect=(350,800,250,50))
            lobby1 = pygame.draw.rect(win,color=(156,0,36), rect=(1250,800,250,50))
            win.blit(textRetry,(420,800))
            win.blit(textMenu,(1330,800))
            for event in pygame.event.get():
                if retry1.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    lose = False
                    menu = False
                if lobby1.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    lose = False
                    menu = True          
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                player1.Alive = False
                run = False
                lose = False
            pygame.display.update()
        while fin :
            win.fill((0,0,0))
            win.blit(robot_model2,(300,100))
            textFin = my_font.render("Tu as gagné ! les oiseaux n'ont plus de secrets pour toi !", 1, pygame.Color("WHITE"))
            textFin_level0 = my_font.render("Les aigles ont une ésperance de vie d’environ 25 ans. Protege les !", 1, pygame.Color("WHITE"))
            textFin_level1 = my_font.render("Les faucons ont la particularité de posséder une vue perçante et des griffes en forme de faux.", 1, pygame.Color("WHITE"))
            textFin2 = my_font.render("Clique ici pour retourner au menu.", 1, pygame.Color("WHITE"))
            textMenu = my_font.render("Menu", 1, pygame.Color("WHITE"))
            textListFin = [textFin_level0, textFin_level1]
            win.blit(textFin,(500,500))
            win.blit(textListFin[level_selected],(500,550))
            lobby = pygame.draw.rect(win,color=(156,0,36), rect=(1250,800,250,50))
            win.blit(textFin2,(500,650))
            win.blit(textMenu,(1330,800))
            for event in pygame.event.get():
                if lobby.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    fin = False
                    menu = True          
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                player1.Alive = False
                run = False
                lose = False
            pygame.display.update()
        while fin :
            win.fill((0,0,0))
            win.blit(robot_model2,(300,100))
            textFin = my_font.render("Tu as gagné ! les oiseaux n'ont plus de secrets pour toi !", 1, pygame.Color("WHITE"))
            textFin_level0 = my_font.render("Les aigles ont une ésperance de vie d’environ 25 ans. Protege les !", 1, pygame.Color("WHITE"))
            textFin_level1 = my_font.render("Les faucons ont la particularité de posséder une vue perçante et des griffes en forme de faux.", 1, pygame.Color("WHITE"))
            textFin2 = my_font.render("Clique ici pour retourner au menu.", 1, pygame.Color("WHITE"))
            textMenu = my_font.render("Menu", 1, pygame.Color("WHITE"))
            textListFin = [textFin_level0, textFin_level1]
            win.blit(textFin,(500,500))
            win.blit(textListFin[level_selected],(500,550))
            lobby = pygame.draw.rect(win,color=(156,0,36), rect=(1250,800,250,50))
            win.blit(textFin2,(500,650))
            win.blit(textMenu,(1330,800))
            for event in pygame.event.get():
                if lobby.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    fin = False
                    menu = True          
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                player1.Alive = False
                run = False
            pygame.display.update()
pygame.quit()
