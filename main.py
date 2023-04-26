import pygame
import math
import sys
sys.path.insert(0,"imports")
from class_import import *
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
