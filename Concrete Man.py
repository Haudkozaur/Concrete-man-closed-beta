import pygame
import random
import time
import numpy as np
pygame.init()
def game():
        global rebar_state, playerY, playerX, playerX_change, playerY_change, kierownikchujX, kierownikchujY, kierownikchujY_change, kierownikchujX_change, bhpX_change, bhpY_change, bhpX, bhpY, rebarX, rebarY, score, hp, game_state, time, current_time, rebar_fallX, rebar_fallY, run, game_over
        game_state = "will see"
        mainClock = pygame.time.Clock()
        # sound
        from pygame import mixer

        # background music
        mixer.music.load('doomer.mp3')
        mixer.music.play(-1)

        # window
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Concrete Man")
        icon = pygame.image.load('concrete (1).png')
        pygame.display.set_icon(icon)
        max_screen_width = 736
        min_screen_wh = 0
        max_screen_height = 536

        background = pygame.image.load('rydlowka.png')
        concrete_man = pygame.image.load('concrete_man.png')
        beer = pygame.image.load('thumb_up.png')
        concrete_man_2 = pygame.image.load('concrete_man_2_86.png')
        concrete_man_3 = pygame.image.load('concrete_warrior_git.png')
        # player

        playerimg = pygame.image.load('worker (2).png')
        playerX = 400
        playerY = 300
        playerX_change = 0
        playerY_change = 0

        basic_player_velocity = 3
        loaded_player_velocity = 1.5


        def player(x, y):
            screen.blit(playerimg, (x, y))


        # points

        score = 0
        hp = 100

        font = pygame.font.Font('freesansbold.ttf', 32)
        scoreX = 10
        scoreY = 10


        def show_score(x, y):
            score_value = font.render("Score : " + str(score), True, (0, 0, 0))
            screen.blit(score_value, (x, y))
            hp_print = font.render("hp : " + str(hp), True, (255, 0, 0))
            screen.blit(hp_print, (650, 10))


        # arrays of map

        first_poleX = []
        first_poleY = []
        rows, cols = (8, 12)

        x1 = 10
        y1 = 65
        for c in range(cols):
            first_poleX.append(x1)
            x1 += 65
        for r in range(rows):
            first_poleY.append(y1)
            y1 += 65
        # print(first_poleX)
        # print(first_poleY)
        # fpX=np.array(first_poleX)
        # fpY=np.array(first_poleY)
        # fpXY=fpX*fpY
        # print(fpXY)
        first_poleXY = []


        def theMap():
            for i in range(cols):
                for j in range(rows):
                    trufle = (first_poleX[i], first_poleY[j], "free")
                    first_poleXY.append(trufle)


        theMap()
        # print(first_poleXY)

        num_of_formworks = 1
        formworkX = []
        formworkY = []


        def chessboardMachine():
            while len(formworkX) != num_of_formworks:
                t = random.randint(0, 95)
                if first_poleXY[t][2] == "free":
                    formworkX.append(first_poleXY[t][0])
                    formworkY.append(first_poleXY[t][1])
                    newtrufla = (first_poleXY[t][0], first_poleXY[t][1], "taken")
                    first_poleXY[t] = newtrufla


        chessboardMachine()

        # formwork

        formworkimg = []
        bottom_netimg = []
        formwork_state = []

        for i in range(num_of_formworks):
            formworkimg.append(pygame.image.load('parquet.png'))
            bottom_netimg.append(pygame.image.load('bottom_net_rotated.png'))
            formwork_state.append("empty")


        def formwork(x, y, i):
            if formwork_state[i] == "empty":
                screen.blit(formworkimg[i], (x, y))


            elif formwork_state[i] == "bottom_net":
                screen.blit(bottom_netimg[i], (x, y))


        # kierownikchuj
        kierownikchujimg = pygame.image.load('kierownikchuj.png')
        kierownikchujX = 790
        kierownikchujY = 590
        kierownikchujX_change = 0.5
        kierownikchujY_change = 0.5


        def kierownikchuj(x, y):
            screen.blit(kierownikchujimg, (x, y))


        # bhp
        bhpimg = pygame.image.load('BHP.png')
        bhpX = min_screen_wh
        bhpY = min_screen_wh
        bhpX_change = 4
        bhpY_change = 0


        def bhp(x, y):
            screen.blit(bhpimg, (x, y))


        bhp_state = "horizontal"


        # hitbox

        def hitbox(x, y, z, w):
            distance = (((x - z) ** 2) + ((y - w) ** 2)) ** 0.5
            if distance < 40:
                return True
            else:
                return False


        # rebar

        rebarimg = pygame.image.load('iron-bar.png')
        rebarX = random.randint(50, 750)
        rebarY = random.randint(50, 550)
        rebar_state = "delivered"
        rebarX_change = 0
        rebarY_change = 0
        rebar_HITBOX = 40
        rebar_shoulderX = 25
        rebar_shoulderY = 20


        def rebar(x, y):
            screen.blit(rebarimg, (x, y))
            # screen.blit(rebarimg, (x / 2, y / 2))
            # screen.blit(rebarimg, ((x * y) ** 0.5, y / x))


        def rebar_picked(x, y):
            global rebar_state
            rebar_state = "picked"
            screen.blit(rebarimg, (x, y))


        # game over
        over_font = pygame.font.Font('freesansbold.ttf', 100)


        def game_over():
            if score == num_of_formworks:
                game_over = over_font.render("Well done!", True, (0, 0, 0))
                screen.blit(game_over, (150, 2))
            elif hp <= 0:
                game_over = over_font.render("GAME OVER", True, (255, 0, 0))
                screen.blit(game_over, (90, 250))


        # time

        start_time = time.time()


        def timer():
            time = font.render(str(current_time), True, (0, 0, 0))
            screen.blit(time, (20, 560))


        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)


        pupa = True
        run = True
        zupa = True
        click = False


        def main_menu():
            global run, pupa, zupa, click
            zupa = True
            while zupa:
                # screen.fill((120, 120, 120))

                screen.blit(concrete_man_3, (0, 0))
                draw_text('main menu', font, (255, 0, 0), screen, 55, 20)

                mx, my = pygame.mouse.get_pos()
                button_1 = pygame.Rect(50, 100, 200, 50)
                if button_1.collidepoint((mx, my)):
                    if click:
                        zupa = False
                        pupa = True
                        press_any_key_lvl1()
                pygame.draw.rect(screen, (0, 0, 0), button_1)
                draw_text('play', font, (255, 0, 0), screen, 120, 105)
                click = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pupa = False
                        run = False
                        zupa = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
                pygame.display.update()
            # loop

            # begginning


        def press_any_key_lvl1():
            global pupa, zupa, run
            while pupa:

                # screen.fill((120, 120, 120))

                screen.blit(concrete_man_2, (0, 0))
                pressanykey = font.render("Press any key to start", True, (255, 0, 0))
                screen.blit(pressanykey, (450, 500))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pupa = False
                        run = False
                    if event.type == pygame.KEYDOWN:
                        level1()
                        pupa = False
                        run = True
                pygame.display.update()
            # loop


        def level1():
            global rebar_state, playerY, playerX, playerX_change, playerY_change, kierownikchujX, kierownikchujY, \
                kierownikchujY_change, kierownikchujX_change, bhpX_change, bhpY_change, bhpX, bhpY, rebarX, rebarY, score, hp, game_state, time, current_time, rebar_fallX, rebar_fallY, run, game_over
            while run:
                # RGB
                # screen.fill((120, 120, 120))
                screen.blit(background, (0, 0))

                # flesh

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                        # control
                    if rebar_state == "delivered" or rebar_state == "forsaken":
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                playerX_change = -basic_player_velocity
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                playerX_change = basic_player_velocity
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                playerY_change = -basic_player_velocity
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                playerY_change = basic_player_velocity
                    if rebar_state == "picked":
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                                playerX_change = -loaded_player_velocity
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                                playerX_change = loaded_player_velocity
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                playerY_change = -loaded_player_velocity
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                playerY_change = loaded_player_velocity
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and rebar_state == "delivered":
                        if hitbox_rebar_delivered:
                            rebar_state = "picked"
                            lifting = mixer.Sound('lifting.wav')
                            lifting.play()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and rebar_state == "forsaken":
                        if hitbox_rebar_forsaken:
                            rebar_state = "picked"
                            lifting = mixer.Sound('lifting.wav')
                            lifting.play()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and rebar_state == "picked":
                        rebar_state = "forsaken"
                        rebar_fallX = playerX + 15
                        rebar_fallY = playerY + 60
                        metal_falling = mixer.Sound('metal_falling.wav')
                        metal_falling.play()
                        if rebar_fallY >= max_screen_height + rebar_HITBOX:
                            rebar_fallY = max_screen_height + rebar_HITBOX - 5
                    if event.type == pygame.KEYUP:
                        playerX_change = 0
                        playerY_change = 0
                    if event.type == pygame.KEYDOWN and game_state == "game over":
                        run = False
                        game()

                    for i in range(num_of_formworks):

                        formwork(formworkX[i], formworkY[i], i)
                        # formwork
                        if rebar_state == "delivered":
                            hitbox_formwork_player = hitbox(playerX, playerY, formworkX[i], formworkY[i])
                            hitbox_formwork_rebar = hitbox(rebarX, rebarY, formworkX[i], formworkY[i])
                        if rebar_state == "forsaken":
                            hitbox_formwork_player = hitbox(playerX, playerY, formworkX[i], formworkY[i])
                            hitbox_formwork_rebar = hitbox(rebar_fallX, rebar_fallY, formworkX[i], formworkY[i])

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and (
                                rebar_state == "forsaken" or rebar_state == "delivered") and hitbox_formwork_rebar and hitbox_formwork_player and \
                                formwork_state[i] == "empty":
                            print("ready to reinforce")
                            formwork_state[i] = "bottom_net"
                            rebar_state = "delivered"
                            rebarX = random.randint(50, 750)
                            rebarY = random.randint(50, 550)
                            score += 1
                            print(score)
                            instal = mixer.Sound('instal.wav')
                            instal.play()
                for i in range(num_of_formworks):
                    formwork(formworkX[i], formworkY[i], i)
                # player
                playerX += playerX_change
                playerY += playerY_change
                if playerX <= 0:
                    playerX = 0
                elif playerX >= max_screen_width:
                    playerX = max_screen_width
                if playerY <= min_screen_wh:
                    playerY = min_screen_wh
                elif playerY >= max_screen_height:
                    playerY = max_screen_height

                player(playerX, playerY)

                # kierownikchuj
                kierownikchuj(kierownikchujX, kierownikchujY)

                kierownikchujX += kierownikchujX_change
                kierownikchujY += kierownikchujY_change

                if kierownikchujX <= min_screen_wh or kierownikchujX >= max_screen_width:
                    kierownikchujX_change = (random.randint(-4, 4))
                    kierownikchujY_change = (random.randint(-4, 4))

                if kierownikchujY <= min_screen_wh or kierownikchujY >= max_screen_height:
                    kierownikchujY_change = (random.randint(-4, 4))
                    kierownikchujX_change = (random.randint(-4, 4))

                if kierownikchujX <= min_screen_wh:
                    kierownikchujX = min_screen_wh
                elif kierownikchujX >= max_screen_width:
                    kierownikchujX = max_screen_width
                if kierownikchujY <= min_screen_wh:
                    kierownikchujY = min_screen_wh
                elif kierownikchujY >= max_screen_height:
                    kierownikchujY = max_screen_height

                # bhp
                bhp(bhpX, bhpY)

                bhpX += bhpX_change
                bhpY += bhpY_change

                if bhp_state == "horizontal":
                    # print("X",bhpX,"Y",bhpY)
                    if bhpX >= max_screen_width and bhpY >= max_screen_height:
                        bhpX = min_screen_wh
                        bhpY = min_screen_wh
                        bhpX_change = 4
                        bhpY_change = 0
                    if bhpX >= max_screen_width and bhpY != max_screen_height:
                        bhpX_change = -4
                        bhpY_change = 35
                    elif bhpX <= min_screen_wh and bhpY != max_screen_height and bhpY != min_screen_wh:
                        bhpX_change = 4
                        bhpY_change = 35
                    # elif bhpY >= max_screen_height and bhpX <= min_screen_wh:
                    # bhp_state = "vertical"
                    else:
                        bhpY_change = 0

                # elif bhp_state == "vertical":
                # print("bhpX:", bhpX, "bhpY:", bhpY)
                # if bhpY >= max_screen_height and bhpX != min_screen_wh:
                #     bhpX_change = 35
                #     bhpY_change = -2
                # elif bhpY <= min_screen_wh and bhpY != min_screen_wh:
                #     bhpX_change = 35
                #     bhpY_change = 2
                # elif bhpX >= max_screen_width:
                #     bhpX_change = -736
                #     bhpY_change = -536
                #     bhp_state = "horizontal"
                # else:
                #     bhpX_change = 0

                if bhpX < min_screen_wh:
                    bhpX = min_screen_wh
                elif bhpX > max_screen_width:
                    bhpX = max_screen_width
                if bhpY < min_screen_wh:
                    bhpY = min_screen_wh
                elif bhpY > max_screen_height:
                    bhpY = max_screen_height

                    # rebar
                if rebar_state == "delivered":
                    rebar(rebarX, rebarY)
                elif rebar_state == "picked":
                    rebar_picked(playerX + 25, playerY + 20)
                elif rebar_state == "forsaken":
                    rebar(rebar_fallX, rebar_fallY)

                # hitboxes rebar
                if rebar_state == "delivered":
                    hitbox_rebar_delivered = hitbox(playerX, playerY, rebarX, rebarY)
                elif rebar_state == "forsaken":
                    hitbox_rebar_forsaken = hitbox(playerX, playerY, rebar_fallX, rebar_fallY)

                # hitboxes kierownikchuj
                hitbox_kierownik = hitbox(playerX, playerY, kierownikchujX, kierownikchujY)
                # hitboxes bhp
                hitbox_bhp = hitbox(playerX, playerY, bhpX, bhpY)

                # collisions

                if hitbox_kierownik and game_state == "will see":
                    hp -= 1
                    kurwa = mixer.Sound('kurwa_dobra.wav')
                    kurwa.play()
                if hitbox_bhp and game_state == "will see":
                    hp -= 1
                    ja_pierdole = mixer.Sound('ja_pierdole.wav')
                    ja_pierdole.play()

                show_score(scoreX, scoreY)

                # game over

                if score == num_of_formworks:
                    game_state = "game over"
                    screen.blit(beer, (0, 0))
                    game_over()
                    backtomenu = font.render("Press any key to return to main menu", True, (255, 0, 0))
                    screen.blit(backtomenu, (200, 500))


                elif hp <= 0:
                    game_state = "game over"
                    screen.blit(concrete_man, (0, 0))
                    game_over()
                    backtomenu = font.render("Press any key to return to main menu", True, (255, 0, 0))
                    screen.blit(backtomenu, (200, 500))



                # time
                if game_state == "will see":
                    current_time = round((time.time() - start_time), 2)
                    # print(current_time)
                    timer()
                mainClock.tick(120)
                # print(hitbox_formwork_player, hitbox_formwork_rebar)
                # update
                # print(game_state)
                pygame.display.update()


        main_menu()
game()