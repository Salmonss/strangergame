
import math
import random
import pygame, sys
import button
from pygame import mixer
from tkinter import *
mainClock = pygame.time.Clock()
from pygame.locals import *

#VARIABLE SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
pygame.init()
#FUNCTION SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
font = pygame.font.SysFont(None , 20)

#GAME CAPTIONS
pygame.display.set_caption('STRANGER SHOOTER GAME')
icon = pygame.image.load('assets/gamelogo.png')
pygame.display.set_icon(icon)

#IMAGE FUCNTIONS
def draw_text (text, font, color, surface, x, y):
    textobj =font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

# BACKGROUND MUSIC
mixer.music.load('sound/game.wav')
mixer.music.play(-1)

#VARIABLE 
click = False


# IMAGE LIBRARY
# IMAGE IN GAME MENU
bg_image = pygame.image.load("assets/design 4.png")
start_img = pygame.image.load('assets/start1.png')
option_img = pygame.image.load('assets/Options1.png')
abilities_img = pygame.image.load('assets/abilities1.png')
bg_bg = pygame.image.load('assets/bg.png')
bg_background = pygame.image.load('assets/background.png')

# FUNCTION BUTTONS IN GAME MENU

start_button = button.Button(280, 450, start_img, 0.8)
option_button = button.Button(280, 550, option_img, 0.8)
abilities_button = button.Button(540, 500, abilities_img, 0.8)

# IMAGE IN OPTIONS

bg_videos = pygame.image.load('assets/videos1.png')
bg_information = pygame.image.load('assets/info.png')
bg_keypads = pygame.image.load('assets/keypads1.png')
bg_about = pygame.image.load('assets/about1.png')
bg_back = pygame.image.load('assets/back.png')

# FUNCTION BUTTONS IN OPTIONS

information_button = button.Button(280, 200, bg_information, 0.8)
keypads_button = button.Button(10, 300, bg_keypads, 0.8)
about_button = button.Button(550, 300, bg_about, 0.8)
back_button = button.Button(280, 500, bg_back, 0.8)

# IMAGE IN KEYPADS

kp_back = pygame.image.load('assets/back.png')
kp_keypadss = pygame.image.load('assets/keypadss.png')


# FUNCTION BUTTON IN KEYPADS

back_kp = button.Button(15, 520, kp_back, 0.8)

# IMAGE IN INFORMATION

i_back = pygame.image.load('assets/back.png')
i_logo = pygame.image.load('assets/informationlogo.png')
i_forward = pygame.image.load('assets/next.png')

# FUNCTION BUTTON IN INFORMATION

back_i = button.Button(15, 520, i_back, 0.8)
infromation_forward = button.Button(500, 520, i_forward, 0.8)


# IMAGE IN ABOUT

a_back = pygame.image.load('assets/back.png')
a_aboutss = pygame.image.load('assets/aboutss.png')

# FUNCTION BUTTON IN ABOUTS

back_a = button.Button(15, 520, a_back, 0.8)

# IMAGE IN INFORMATION FOR ELEVEN

e_eleven = pygame.image.load('assets/eleven.png')

# IMAGE IN INFORMATION FOR MIKE

e_mike = pygame.image.load('assets/mike.png')

# IMAGE IN INFORMATION FOR LUCAS

e_lucas = pygame.image.load('assets/lucas.png')

# IMAGE IN INFORMATION FOR DUSTIN

e_dustin = pygame.image.load('assets/dustin.png')

# IMAGE IN INFORMATION FOR PLACES PART ONE

e_partone = pygame.image.load('assets/partone.png')

# IMAGE IN INFORMATION FOR PLACES PART TWO

e_parttwo = pygame.image.load('assets/parttwo.png')

# IMAGE IN SELECTION SCREEN

s_logo = pygame.image.load('assets/selectlogo.png')

# IMAGE IN SELECTION SCREEN 

l_eleven = pygame.image.load('assets/elevenlogo.png')
l_mike = pygame.image.load('assets/mikelogo.png')
l_lucas = pygame.image.load('assets/lucaslogo.png')
l_dustin = pygame.image.load('assets/dustinlogo.png')
# BUTTON IN SELECTION SCREEN

b_eleven = pygame.image.load('assets/elevenlogos.png')
b_mike = pygame.image.load('assets/mikelogos.png')
b_lucas = pygame.image.load('assets/lucaslogos.png')
b_dustin = pygame.image.load('assets/dustinlogos.png')


# FUNCTION IN SELECTION SCREEN

eleven_button = button.Button(1, 310, b_eleven, 0.7)
mike_button = button.Button(190, 310, b_mike, 0.7)
lucas_button = button.Button(380, 310, b_lucas, 0.7)
dustin_button = button.Button(580, 310, b_dustin, 0.7)


# IMAGE IN PLACE REVIEW 

place_r = pygame.image.load('assets/placereview.png')
E_for = pygame.image.load('assets/elevenbutton.png')
M_for = pygame.image.load('assets/mikebutton.png')
L_for = pygame.image.load('assets/lucasbutton.png')
D_for = pygame.image.load('assets/dustinbutton.png')


#BUTTON IN PLACE REVIEW

p_eleven = button.Button(270, 570, E_for, 0.8)
p_mike = button.Button(270, 570, M_for, 0.8)
p_lucas = button.Button(270, 570, L_for, 0.8)
p_dustin = button.Button(270, 570, D_for, 0.8)


#SET UP OF EVERY SCREEN IN THE GAME
#CUSTOMIZE OR PUTTING A FUNCTION IN THE GAME IS ALSO IN DOWN
#GAME SET UP
#VARIABLE FUCNTION AND OTHER STAFF TO CHANGE 

# SET UP IN GAME MENU

def game_menu():
    screen.blit(bg_image, (0,0))
    while True:

        #SCREEN
        screen.blit(bg_image, (0,0))
        
        draw_text("Game menu", font, (255, 255, 255), screen, 20, 20)

        # SCREEN TO SCREEN
        
        if start_button.draw(screen):
            if click:
                start_sound = mixer.Sound('sound/buttoneffect.wav')
                start_sound.play()
                game_selection()
        if option_button.draw(screen):
            if click:
                option_sound = mixer.Sound('sound/buttoneffect.wav')
                option_sound.play()
                option()

        click = False
        #GAME LOOP

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# SET UP IN GAME
def game_selection():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background,(0, 0))
        screen.blit(s_logo,(0, 0))
        screen.blit(l_eleven,(-40, 340))
        screen.blit(l_mike,(150, 340))
        screen.blit(l_lucas,(340, 340))
        screen.blit(l_dustin,(540, 340))
        draw_text("Game Selection", font, (255, 255, 255), screen, 20, 20)   
        
        if eleven_button.draw(screen):
            if click:
                elbutton_sound = mixer.Sound('sound/buttoneffect.wav')
                elbutton_sound.play()
                Eplacereview()
        
        if mike_button.draw(screen):
            if click:
                mbutton_sound = mixer.Sound('sound/buttoneffect.wav')
                mbutton_sound.play()
                Mplacereview()

        if lucas_button.draw(screen):
            if click:
                lbutton_sound = mixer.Sound('sound/buttoneffect.wav')
                lbutton_sound.play()
                Lplacereview()

        if dustin_button.draw(screen):
            if click:
                dbutton_sound = mixer.Sound('sound/buttoneffect.wav')
                dbutton_sound.play()
                Dplacereview()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# SET UP IN OPTIONS
def option():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0, 0 ))
        draw_text("OPTIONS", font, (255, 255, 255), screen, 20, 20)

        
        #SCREEN TO SCREEN 
        if information_button.draw(screen):
            if click:
                information_sound = mixer.Sound('sound/buttoneffect.wav')
                information_sound.play()
                information()
        if keypads_button.draw(screen):
            if click:
                keypads_sound = mixer.Sound('sound/buttoneffect.wav')
                keypads_sound.play()
                keypads()
        if about_button.draw(screen):
            if click:
                about_sound = mixer.Sound('sound/buttoneffect.wav')
                about_sound.play()
                about()
        if back_button.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                game_menu()

        click = False
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)


# SET UP IN KEYPADS
def keypads():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(kp_keypadss, (350,50))

        draw_text("KEYPADS", font, (255, 255, 255), screen, 20, 20)
        
        
        #SCREEN TO SCREEN
        
        if back_kp.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                option()
            

        click = False
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# SET UP IN SOUNDS

def information():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(i_logo, (0,120))
        draw_text("INFORMATION", font, (255, 255, 255), screen, 20, 20)
        if infromation_forward.draw(screen):
            if click:
                informations_sound = mixer.Sound('sound/buttoneffect.wav')
                informations_sound.play()
                eleven()
        if back_i.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                option()

        click = False
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# SET UP IN ABOUTS

def about():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(a_aboutss, (350, 50))
        draw_text("ABOUT", font, (255, 255, 255), screen, 20, 20)
        
        if back_a.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                option()
        
        click = False
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# SET UP IN FIRST INFORMATION

def eleven():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_eleven, (0,30))
        draw_text("ELEVEN", font, (255, 255, 255), screen, 20, 20)
        
        
        if infromation_forward.draw(screen):
            if click:
                mike_sound = mixer.Sound('sound/buttoneffect.wav')
                mike_sound.play()
                mike()
        if back_i.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                information()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# SET UP IN SECOND INFORMATION

def mike():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_mike, (0,30))
        draw_text("MIKE", font, (255, 255, 255), screen, 20, 20)
        
        
        if infromation_forward.draw(screen):
            if click:
                lucas_sound = mixer.Sound('sound/buttoneffect.wav')
                lucas_sound.play()
                lucas()
        if back_i.draw(screen):
            if click:
                eleven_sound = mixer.Sound('sound/buttoneffect.wav')
                eleven_sound.play()
                eleven()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# SET UP IN THIRD INFORMATION

def lucas():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_lucas, (0,30))
        draw_text("LUCAS", font, (255, 255, 255), screen, 20, 20)
        
        
        if infromation_forward.draw(screen):
            if click:
                dustin_sound = mixer.Sound('sound/buttoneffect.wav')
                dustin_sound.play()
                dustin()
        if back_i.draw(screen):
            if click:
                mike_sound = mixer.Sound('sound/buttoneffect.wav')
                mike_sound.play()
                mike()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# SET UP IN FOURTH INFORMATION

def dustin():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_dustin, (0,30))
        draw_text("DUSTIN", font, (255, 255, 255), screen, 20, 20)
        
        
        if infromation_forward.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                partone()
        if back_i.draw(screen):
            if click:
                lucas_sound = mixer.Sound('sound/buttoneffect.wav')
                lucas_sound.play()
                lucas()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# SET UP IN PLACES PART ONE

def partone():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_partone, (0,30))
        draw_text("PARTONE", font, (255, 255, 255), screen, 20, 20)
        
        
        if infromation_forward.draw(screen):
            if click:
                parttwo_sound = mixer.Sound('sound/buttoneffect.wav')
                parttwo_sound.play()
                parttwo()
        if back_i.draw(screen):
            if click:
                dustin_sound = mixer.Sound('sound/buttoneffect.wav')
                dustin_sound.play()
                dustin()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# SET UP IN PLACES PART TWO

def parttwo():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(e_parttwo, (0,30))
        draw_text("PARTTWO", font, (255, 255, 255), screen, 20, 20)

        if back_i.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                partone()
        click = False   
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# ELEVEN PERSPECTIVE SCREEN AND PLACES REVIEW

def Eplacereview():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_r, (0, 170))
        draw_text("PLACE REVIEW", font, (255, 255, 255), screen, 20, 20)

        if p_eleven.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Eplay()

        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                game_selection()


        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# MIKE PERSPECTIVE SCREEN ADN PLACES REVIEW

def Mplacereview():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_r, (0, 170))
        draw_text("PLACE REVIEW", font, (255, 255, 255), screen, 20, 20)

        if p_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Mplay()
        
        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                game_selection()
 
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# LUCAS PERSPECTIVE SCREEN AND PLACES REVIEW

def Lplacereview():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_r, (0, 170))
        draw_text("PLACE REVIEW", font, (255, 255, 255), screen, 20, 20)

        if p_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Lplay()
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                game_selection()
 
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# DUSTIN PERSPECTIVE SCREEN AND PLACES REVIEW

def Dplacereview():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_r, (0, 170))
        draw_text("PLACE REVIEW", font, (255, 255, 255), screen, 20, 20)

        if p_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Dplay()
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                game_selection()
 
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

# ELEVEN PERSPECTIVE SCREEN WHILE PLAYING 
# LEVEL NUMBER 1
player_eleven = pygame.image.load('assets/ElevenSpace.png')
enemy_eleven = pygame.image.load('assets/alien.png')
enemy_elevenn = pygame.image.load('assets/alien2.png')
bullets_eleven = pygame.image.load('assets/bullet.png')
places_level = pygame.image.load("assets/level1place.png")
success = pygame.image.load("assets/elevenbutton.png")
success_eleven = pygame.image.load("assets/balikbuttoneleven.png")

#LEVEL 2
enemy_level = pygame.image.load("assets/level2alien2.png")
enemy_level2 = pygame.image.load("assets/level2alien.png")
places_level2 = pygame.image.load("assets/level2place.png")


#LEVEL 3
enemy_levell3 = pygame.image.load("assets/ufolevel1.png")
enemy_level3 = pygame.image.load("assets/ufolevel.png")
places_level3 = pygame.image.load("assets/placeslevel3.png")

#LEVEL 4
enemy_levell4 = pygame.image.load("assets/ufolevel33.png")
enemy_level4 = pygame.image.load("assets/ufolevel3.png")
places_level4 = pygame.image.load("assets/placeslevel4.png")

umulit = button.Button(500, 570, success, 0.8)
umuulit = button.Button(20, 570, success_eleven, 0.8)

# DISPLAY 
def Display(x,y):
    screen.blit(player_eleven, (x,y))
# ENEMY
def Enemy(x,y):
    screen.blit(enemy_elevenn, (x,y))
def Enemies(x,y):
    screen.blit(enemy_eleven, (x,y))
def Enemieslevel(x,y):
    screen.blit(enemy_level, (x,y))
def Enemieslevel2(x,y):
    screen.blit(enemy_level2, (x,y))
def Enemieslevell(x,y):
    screen.blit(enemy_levell3, (x,y))
def Enemieslevel3(x,y):
    screen.blit(enemy_level3, (x,y))
def Enemieslevelll4(x,y):
    screen.blit(enemy_levell4, (x,y))
def Enemieslevel4(x,y):
    screen.blit(enemy_level4, (x,y))

    
# BULLETS
def fire_Bullets(x, y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bullets_eleven, (x + 16,y + 10))

# SCORE BOARD
def show_score(x,y):
    fonts = pygame.font.Font('freesansbold.ttf', 32)
    score_value = 0
    score = fonts.render("SCORE : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

# GAME OVER
def gameover():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,500))

# COLLISION
def isCollision (enemy_X, enemyY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemy_X-bullet_X,2)+ (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
# COLLISION TWO
def oneCollision(enemies_X, enemiesY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemies_X-bullet_X,2)+ (math.pow(enemiesY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
# COLLISION THREE
def twoCollision(enemiess_X, enemiessY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemiess_X-bullet_X,2)+ (math.pow(enemiessY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
# COLLISION FOURT
def threeCollision(enemiesss_X, enemiesssY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemiesss_X-bullet_X,2)+ (math.pow(enemiesssY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
# COLLISION FIVE
def threeCollision(enemiesss_X, enemiesssY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemiesss_X-bullet_X,2)+ (math.pow(enemiesssY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
# COLLISION SIX
def fourCollision(enemiessss_X, enemiessssY, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemiessss_X-bullet_X,2)+ (math.pow(enemiessssY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# COLLISION SEVEN
def fourCollision(enemies7_X, enemies7Y, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemies7_X-bullet_X,2)+ (math.pow(enemies7Y-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# COLLISION SEVEN
def fourCollision(enemies8_X, enemies8Y, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemies8_X-bullet_X,2)+ (math.pow(enemies8Y-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# COLLISION SEVEN
def fourCollision(enemies9_X, enemies9Y, bullet_X, bulletY):
    distance = math.sqrt(math.pow(enemies9_X-bullet_X,2)+ (math.pow(enemies9Y-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#LEVEL 1
def Eplay():

    
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 40

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 40

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 40

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 40

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # EIGHT ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # NINE ENEMIES
    enemies9Y = random.randint(50,150)
    enemies9_X = random.randint(0,736)
    enemies9X_changed = 20
    enemies9Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 40

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level, (0,0))
        draw_text("LEVEL1", font, (255, 255, 255), screen, 20, 20)

    
        if umulit.draw(screen):
            if click:
                EEplaylevel2()

        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Eplacereview() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 20
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -20
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 20
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -20
            enemies7Y += enemies7Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 20
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -20
            enemies8Y += enemies8Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies9_X += enemies9X_changed

        if enemies9_X <= 1:
            enemies9X_changed = 20
            enemies9Y += enemies9Y_changed
        elif enemies9_X >= 736:
            enemies9X_changed = -20
            enemies9Y += enemies9Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bullets(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)
        
        # NINE ENEMIES
        fivecollision = fourCollision(enemies9_X,enemies9Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies9_X,enemies9Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies9Y = random.randint(50,150)
            enemies9_X = random.randint(0,735)


        Enemies(enemies9_X, enemies9Y)
        Enemies(enemies8_X, enemies8Y)   
        Enemies(enemies7_X, enemies7Y)
        Enemies(enemiesssss_X, enemiesssssY)
        Enemy(enemiessss_X, enemiessssY)
        Enemy(enemiesss_X, enemiesssY)
        Enemy(enemiess_X, enemiessY)
        Enemy(enemies_X, enemiesY)
        Enemy(enemy_X, enemyY)
        Display(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 2 PLACE

def EEplaylevel2():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review2, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 2", font, (255, 255, 255), screen, 20, 20)

        if p_eleven.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEplay()
        
        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Eplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def EEplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level2, (0,0))
        draw_text("LEVEL2", font, (255, 255, 255), screen, 20, 20)

    
        if umulit.draw(screen):
            if click:
                EEplaylevel3()

        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEplaylevel2() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 25
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -25
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 25
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -25
            enemies7Y += enemies7Y_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 25
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -25
            enemies8Y += enemies8Y_changed

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bullets(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)

        
        Enemieslevel(enemies8_X, enemies8Y)
        Enemieslevel(enemies7_X, enemies7Y)
        Enemieslevel(enemiesssss_X, enemiesssssY)
        Enemieslevel2(enemiessss_X, enemiessssY)
        Enemieslevel2(enemiesss_X, enemiesssY)
        Enemieslevel2(enemiess_X, enemiessY)
        Enemieslevel2(enemies_X, enemiesY)
        Enemieslevel2(enemy_X, enemyY)
        Display(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 3 PLACE

def EEplaylevel3():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review3, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 3", font, (255, 255, 255), screen, 20, 20)

        if p_eleven.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEEplay()
        
        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEplay()
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def EEEplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level3, (0,0))
        draw_text("LEVEL3", font, (255, 255, 255), screen, 20, 20)

    
        if umulit.draw(screen):
            if click:
                EEplaylevel4()

        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEplaylevel3() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 30
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -30
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 30
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -30
            enemies7Y += enemies7Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bullets(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)


        
        
        Enemieslevell(enemies7_X, enemies7Y)
        Enemieslevell(enemiesssss_X, enemiesssssY)
        Enemieslevel3(enemiessss_X, enemiessssY)
        Enemieslevel3(enemiesss_X, enemiesssY)
        Enemieslevel3(enemiess_X, enemiessY)
        Enemieslevel3(enemies_X, enemiesY)
        Enemieslevel3(enemy_X, enemyY)
        Display(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)

#LEVEL 4 PLACE

def EEplaylevel4():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review4, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 4", font, (255, 255, 255), screen, 20, 20)

        if p_eleven.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEEEplay()
        
        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEEplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def EEEEplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level4, (0,0))
        draw_text("LEVEL4", font, (255, 255, 255), screen, 20, 20)

    
        if umulit.draw(screen):
            if click:
                pass
        
        if umuulit.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                EEplaylevel4()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 40
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -40
            enemiesssssY += enemiesssssY_changed
        
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bullets(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        

        
        
        Enemieslevelll4(enemiesssss_X, enemiesssssY)
        Enemieslevel4(enemiessss_X, enemiessssY)
        Enemieslevel4(enemiesss_X, enemiesssY)
        Enemieslevel4(enemiess_X, enemiessY)
        Enemieslevel4(enemies_X, enemiesY)
        Enemieslevel4(enemy_X, enemyY)
        Display(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


# MIKE PERSPECTIVE SCREEN WHILE PLAYING 
# LEVEL NUMBER 1
player_mike = pygame.image.load('assets/mikespace.png')
enemy_eleven = pygame.image.load('assets/alien.png')
enemy_elevenn = pygame.image.load('assets/alien2.png')
bullets_eleven = pygame.image.load('assets/bullet.png')
bullets_mike = pygame.image.load('assets/bulletmike.png')
places_level = pygame.image.load("assets/level1place.png")
success = pygame.image.load("assets/elevenbutton.png")
success_mike = pygame.image.load("assets/mikebutton.png")
success_mikee = pygame.image.load("assets/balikbuttonmike.png")
place_review2 = pygame.image.load('assets/placereviewlevel2.png')
place_review3 = pygame.image.load('assets/placereviewlevel3.png')
place_review4 = pygame.image.load('assets/placereviewlevel4.png')

#LEVEL 2
enemy_level = pygame.image.load("assets/level2alien2.png")
enemy_level2 = pygame.image.load("assets/level2alien.png")
places_level2 = pygame.image.load("assets/level2place.png")


#LEVEL 3
enemy_levell3 = pygame.image.load("assets/ufolevel1.png")
enemy_level3 = pygame.image.load("assets/ufolevel.png")
places_level3 = pygame.image.load("assets/placeslevel3.png")

#LEVEL 4
enemy_levell4 = pygame.image.load("assets/ufolevel33.png")
enemy_level4 = pygame.image.load("assets/ufolevel3.png")
places_level4 = pygame.image.load("assets/placeslevel4.png")

umulit = button.Button(500, 570, success, 0.8)
umulit_mike = button.Button(500, 570, success_mike, 0.8)
umuulit_mike = button.Button(20, 570, success_mikee, 0.8)

# DISPLAY 
def Displaymike(x,y):
    screen.blit(player_mike, (x,y))
# ENEMY
def Enemy(x,y):
    screen.blit(enemy_elevenn, (x,y))
def Enemies(x,y):
    screen.blit(enemy_eleven, (x,y))
def Enemieslevel(x,y):
    screen.blit(enemy_level, (x,y))
def Enemieslevel2(x,y):
    screen.blit(enemy_level2, (x,y))
def Enemieslevell(x,y):
    screen.blit(enemy_levell3, (x,y))
def Enemieslevel3(x,y):
    screen.blit(enemy_level3, (x,y))
def Enemieslevelll4(x,y):
    screen.blit(enemy_levell4, (x,y))
def Enemieslevel4(x,y):
    screen.blit(enemy_level4, (x,y))

    
# BULLETS
def fire_Bullets(x, y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bullets_eleven, (x + 16,y + 10))

# BULLETS
def fire_Bulletss(x, y):
    global bullets_statemike
    bullets_statemike = "fire"
    screen.blit(bullets_mike, (x + 16,y + 10))


# SCORE BOARD
def show_score(x,y):
    fonts = pygame.font.Font('freesansbold.ttf', 32)
    score_value = 0
    score = fonts.render("SCORE : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

# GAME OVER
def gameover():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,500))

# LEVEL 1
def Mplay():

    
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 40

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 40

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 40

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 40

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # EIGHT ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # NINE ENEMIES
    enemies9Y = random.randint(50,150)
    enemies9_X = random.randint(0,736)
    enemies9X_changed = 20
    enemies9Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 40

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level, (0,0))
        draw_text("LEVEL1", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_mike.draw(screen):
            if click:
                MMplaylevel2()

        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Mplacereview() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 20
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -20
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 20
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -20
            enemies7Y += enemies7Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 20
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -20
            enemies8Y += enemies8Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies9_X += enemies9X_changed

        if enemies9_X <= 1:
            enemies9X_changed = 20
            enemies9Y += enemies9Y_changed
        elif enemies9_X >= 736:
            enemies9X_changed = -20
            enemies9Y += enemies9Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)
        
        # NINE ENEMIES
        fivecollision = fourCollision(enemies9_X,enemies9Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies9_X,enemies9Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies9Y = random.randint(50,150)
            enemies9_X = random.randint(0,735)


        Enemies(enemies9_X, enemies9Y)
        Enemies(enemies8_X, enemies8Y)   
        Enemies(enemies7_X, enemies7Y)
        Enemies(enemiesssss_X, enemiesssssY)
        Enemy(enemiessss_X, enemiessssY)
        Enemy(enemiesss_X, enemiesssY)
        Enemy(enemiess_X, enemiessY)
        Enemy(enemies_X, enemiesY)
        Enemy(enemy_X, enemyY)
        Displaymike(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 2 PLACE

def MMplaylevel2():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review2, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 2", font, (255, 255, 255), screen, 20, 20)

        if p_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMplay()
        
        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Mplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def MMplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level2, (0,0))
        draw_text("LEVEL2", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_mike.draw(screen):
            if click:
                MMplaylevel3()

        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMplaylevel2() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 25
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -25
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 25
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -25
            enemies7Y += enemies7Y_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 25
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -25
            enemies8Y += enemies8Y_changed

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)

        
        Enemieslevel(enemies8_X, enemies8Y)
        Enemieslevel(enemies7_X, enemies7Y)
        Enemieslevel(enemiesssss_X, enemiesssssY)
        Enemieslevel2(enemiessss_X, enemiessssY)
        Enemieslevel2(enemiesss_X, enemiesssY)
        Enemieslevel2(enemiess_X, enemiessY)
        Enemieslevel2(enemies_X, enemiesY)
        Enemieslevel2(enemy_X, enemyY)
        Displaymike(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 3 PLACE

def MMplaylevel3():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review3, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 3", font, (255, 255, 255), screen, 20, 20)

        if p_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMMplay()
        
        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMplay()
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def MMMplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level3, (0,0))
        draw_text("LEVEL3", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_mike.draw(screen):
            if click:
                MMplaylevel4()

        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMplaylevel3() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 30
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -30
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 30
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -30
            enemies7Y += enemies7Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)


        
        
        Enemieslevell(enemies7_X, enemies7Y)
        Enemieslevell(enemiesssss_X, enemiesssssY)
        Enemieslevel3(enemiessss_X, enemiessssY)
        Enemieslevel3(enemiesss_X, enemiesssY)
        Enemieslevel3(enemiess_X, enemiessY)
        Enemieslevel3(enemies_X, enemiesY)
        Enemieslevel3(enemy_X, enemyY)
        Displaymike(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)

#LEVEL 4 PLACE

def MMplaylevel4():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review4, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 4", font, (255, 255, 255), screen, 20, 20)

        if p_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMMMplay()
        
        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMMplay()
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def MMMMplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level4, (0,0))
        draw_text("LEVEL4", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_mike.draw(screen):
            if click:
                pass

        if umuulit_mike.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                MMplaylevel4() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 40
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -40
            enemiesssssY += enemiesssssY_changed
        
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        

        
        
        Enemieslevelll4(enemiesssss_X, enemiesssssY)
        Enemieslevel4(enemiessss_X, enemiessssY)
        Enemieslevel4(enemiesss_X, enemiesssY)
        Enemieslevel4(enemiess_X, enemiessY)
        Enemieslevel4(enemies_X, enemiesY)
        Enemieslevel4(enemy_X, enemyY)
        Displaymike(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


# LUCAS PERSPECTIVE SCREEN WHILE PLAYING 
# LEVEL NUMBER 1
player_lucas = pygame.image.load('assets/lucasspace.png')
enemy_eleven = pygame.image.load('assets/alien.png')
enemy_elevenn = pygame.image.load('assets/alien2.png')
bullets_eleven = pygame.image.load('assets/bullet.png')
bullets_mike = pygame.image.load('assets/bulletmike.png')
bullets_lucas = pygame.image.load('assets/bulletlucas.png')
places_level = pygame.image.load("assets/level1place.png")
success = pygame.image.load("assets/elevenbutton.png")
success_mike = pygame.image.load("assets/mikebutton.png")
success_lucas = pygame.image.load("assets/lucasbutton.png")
success_lucass = pygame.image.load("assets/balikbuttonlucas.png")

#LEVEL 2
enemy_level = pygame.image.load("assets/level2alien2.png")
enemy_level2 = pygame.image.load("assets/level2alien.png")
places_level2 = pygame.image.load("assets/level2place.png")


#LEVEL 3
enemy_levell3 = pygame.image.load("assets/ufolevel1.png")
enemy_level3 = pygame.image.load("assets/ufolevel.png")
places_level3 = pygame.image.load("assets/placeslevel3.png")

#LEVEL 4
enemy_levell4 = pygame.image.load("assets/ufolevel33.png")
enemy_level4 = pygame.image.load("assets/ufolevel3.png")
places_level4 = pygame.image.load("assets/placeslevel4.png")

umulit = button.Button(500, 570, success, 0.8)
umulit_mike = button.Button(500, 570, success_mike, 0.8)
umulit_lucas = button.Button(500, 570, success_lucas, 0.8)
umuulit_lucas = button.Button(20, 570, success_lucass, 0.8)

# DISPLAY 
def Displaylucas(x,y):
    screen.blit(player_lucas, (x,y))
# ENEMY
def Enemy(x,y):
    screen.blit(enemy_elevenn, (x,y))
def Enemies(x,y):
    screen.blit(enemy_eleven, (x,y))
def Enemieslevel(x,y):
    screen.blit(enemy_level, (x,y))
def Enemieslevel2(x,y):
    screen.blit(enemy_level2, (x,y))
def Enemieslevell(x,y):
    screen.blit(enemy_levell3, (x,y))
def Enemieslevel3(x,y):
    screen.blit(enemy_level3, (x,y))
def Enemieslevelll4(x,y):
    screen.blit(enemy_levell4, (x,y))
def Enemieslevel4(x,y):
    screen.blit(enemy_level4, (x,y))

    
# BULLETS
def fire_Bullets(x, y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bullets_eleven, (x + 16,y + 10))

# BULLETS
def fire_Bulletss(x, y):
    global bullets_statemike
    bullets_statemike = "fire"
    screen.blit(bullets_mike, (x + 16,y + 10))

# BULLETS
def fire_Bulletsss(x, y):
    global bullets_statelucas
    bullets_statelucas = "fire"
    screen.blit(bullets_lucas, (x + 16,y + 10))


# SCORE BOARD
def show_score(x,y):
    fonts = pygame.font.Font('freesansbold.ttf', 32)
    score_value = 0
    score = fonts.render("SCORE : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

# GAME OVER
def gameover():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,500))

# LEVEL 1
def Lplay():

    
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 40

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 40

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 40

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 40

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # EIGHT ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # NINE ENEMIES
    enemies9Y = random.randint(50,150)
    enemies9_X = random.randint(0,736)
    enemies9X_changed = 20
    enemies9Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 40

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level, (0,0))
        draw_text("LEVEL1", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_lucas.draw(screen):
            if click:
                LLplaylevel2() 
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Lplacereview()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 20
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -20
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 20
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -20
            enemies7Y += enemies7Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 20
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -20
            enemies8Y += enemies8Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies9_X += enemies9X_changed

        if enemies9_X <= 1:
            enemies9X_changed = 20
            enemies9Y += enemies9Y_changed
        elif enemies9_X >= 736:
            enemies9X_changed = -20
            enemies9Y += enemies9Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletsss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)
        
        # NINE ENEMIES
        fivecollision = fourCollision(enemies9_X,enemies9Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies9_X,enemies9Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies9Y = random.randint(50,150)
            enemies9_X = random.randint(0,735)


        Enemies(enemies9_X, enemies9Y)
        Enemies(enemies8_X, enemies8Y)   
        Enemies(enemies7_X, enemies7Y)
        Enemies(enemiesssss_X, enemiesssssY)
        Enemy(enemiessss_X, enemiessssY)
        Enemy(enemiesss_X, enemiesssY)
        Enemy(enemiess_X, enemiessY)
        Enemy(enemies_X, enemiesY)
        Enemy(enemy_X, enemyY)
        Displaylucas(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 2 PLACE

def LLplaylevel2():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review2, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 2", font, (255, 255, 255), screen, 20, 20)

        if p_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLplay()
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Lplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def LLplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level2, (0,0))
        draw_text("LEVEL2", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_lucas.draw(screen):
            if click:
                LLplaylevel3()

        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLplaylevel2() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 25
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -25
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 25
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -25
            enemies7Y += enemies7Y_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 25
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -25
            enemies8Y += enemies8Y_changed

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletsss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)

        
        Enemieslevel(enemies8_X, enemies8Y)
        Enemieslevel(enemies7_X, enemies7Y)
        Enemieslevel(enemiesssss_X, enemiesssssY)
        Enemieslevel2(enemiessss_X, enemiessssY)
        Enemieslevel2(enemiesss_X, enemiesssY)
        Enemieslevel2(enemiess_X, enemiessY)
        Enemieslevel2(enemies_X, enemiesY)
        Enemieslevel2(enemy_X, enemyY)
        Displaylucas(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 3 PLACE

def LLplaylevel3():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review3, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 3", font, (255, 255, 255), screen, 20, 20)

        if p_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLLplay()
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLplay()
        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def LLLplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level3, (0,0))
        draw_text("LEVEL3", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_lucas.draw(screen):
            if click:
                LLplaylevel4()

        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLplaylevel3() 

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 30
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -30
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 30
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -30
            enemies7Y += enemies7Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletsss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)


        
        
        Enemieslevell(enemies7_X, enemies7Y)
        Enemieslevell(enemiesssss_X, enemiesssssY)
        Enemieslevel3(enemiessss_X, enemiessssY)
        Enemieslevel3(enemiesss_X, enemiesssY)
        Enemieslevel3(enemiess_X, enemiessY)
        Enemieslevel3(enemies_X, enemiesY)
        Enemieslevel3(enemy_X, enemyY)
        Displaylucas(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)

#LEVEL 4 PLACE

def LLplaylevel4():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review4, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 4", font, (255, 255, 255), screen, 20, 20)

        if p_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLLLplay()
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLLplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def LLLLplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level4, (0,0))
        draw_text("LEVEL4", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_lucas.draw(screen):
            if click:
                pass
        
        if umuulit_lucas.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                LLplaylevel4()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 40
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -40
            enemiesssssY += enemiesssssY_changed
        
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletsss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        

        
        
        Enemieslevelll4(enemiesssss_X, enemiesssssY)
        Enemieslevel4(enemiessss_X, enemiessssY)
        Enemieslevel4(enemiesss_X, enemiesssY)
        Enemieslevel4(enemiess_X, enemiessY)
        Enemieslevel4(enemies_X, enemiesY)
        Enemieslevel4(enemy_X, enemyY)
        Displaylucas(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


# DUSTIN PERSPECTIVE SCREEN WHILE PLAYING 

# LEVEL NUMBER 1
player_dustin = pygame.image.load('assets/dustinspace.png')
enemy_eleven = pygame.image.load('assets/alien.png')
enemy_elevenn = pygame.image.load('assets/alien2.png')
bullets_eleven = pygame.image.load('assets/bullet.png')
bullets_mike = pygame.image.load('assets/bulletmike.png')
bullets_lucas = pygame.image.load('assets/bulletlucas.png')
bullets_dustin = pygame.image.load('assets/bulletdustin.png')
places_level = pygame.image.load("assets/level1place.png")
success = pygame.image.load("assets/elevenbutton.png")
success_mike = pygame.image.load("assets/mikebutton.png")
success_lucas = pygame.image.load("assets/lucasbutton.png")
success_dustin = pygame.image.load("assets/dustinbutton.png")
success_dustinn = pygame.image.load("assets/balikbuttondustin.png")

#LEVEL 2
enemy_level = pygame.image.load("assets/level2alien2.png")
enemy_level2 = pygame.image.load("assets/level2alien.png")
places_level2 = pygame.image.load("assets/level2place.png")


#LEVEL 3
enemy_levell3 = pygame.image.load("assets/ufolevel1.png")
enemy_level3 = pygame.image.load("assets/ufolevel.png")
places_level3 = pygame.image.load("assets/placeslevel3.png")

#LEVEL 4
enemy_levell4 = pygame.image.load("assets/ufolevel33.png")
enemy_level4 = pygame.image.load("assets/ufolevel3.png")
places_level4 = pygame.image.load("assets/placeslevel4.png")

umulit = button.Button(500, 570, success, 0.8)
umulit_mike = button.Button(500, 570, success_mike, 0.8)
umulit_lucas = button.Button(500, 570, success_lucas, 0.8)
umulit_dustin = button.Button(500, 570, success_dustin, 0.8)
umuulit_dustin = button.Button(20, 570, success_dustinn, 0.8)

# DISPLAY 
def Displaydustin(x,y):
    screen.blit(player_dustin, (x,y))
# ENEMY
def Enemy(x,y):
    screen.blit(enemy_elevenn, (x,y))
def Enemies(x,y):
    screen.blit(enemy_eleven, (x,y))
def Enemieslevel(x,y):
    screen.blit(enemy_level, (x,y))
def Enemieslevel2(x,y):
    screen.blit(enemy_level2, (x,y))
def Enemieslevell(x,y):
    screen.blit(enemy_levell3, (x,y))
def Enemieslevel3(x,y):
    screen.blit(enemy_level3, (x,y))
def Enemieslevelll4(x,y):
    screen.blit(enemy_levell4, (x,y))
def Enemieslevel4(x,y):
    screen.blit(enemy_level4, (x,y))

    
# BULLETS
def fire_Bullets(x, y):
    global bullets_state
    bullets_state = "fire"
    screen.blit(bullets_eleven, (x + 16,y + 10))

# BULLETS
def fire_Bulletss(x, y):
    global bullets_statemike
    bullets_statemike = "fire"
    screen.blit(bullets_mike, (x + 16,y + 10))

# BULLETS
def fire_Bulletsss(x, y):
    global bullets_statelucas
    bullets_statelucas = "fire"
    screen.blit(bullets_lucas, (x + 16,y + 10))

# BULLETS
def fire_Bulletssss(x, y):
    global bullets_statedustin
    bullets_statedustin = "fire"
    screen.blit(bullets_dustin, (x + 16,y + 10))


# SCORE BOARD
def show_score(x,y):
    fonts = pygame.font.Font('freesansbold.ttf', 32)
    score_value = 0
    score = fonts.render("SCORE : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

# GAME OVER
def gameover():
    over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,500))

# LEVEL 1
def Dplay():

    
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 40

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 40

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 40

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 40

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # EIGHT ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # NINE ENEMIES
    enemies9Y = random.randint(50,150)
    enemies9_X = random.randint(0,736)
    enemies9X_changed = 20
    enemies9Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 40

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level, (0,0))
        draw_text("LEVEL1", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_dustin.draw(screen):
            if click:
                DDplaylevel2() 


        if umuulit_dustin.draw(screen):
            if click:
                Dplacereview()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 20
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -20
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 20
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -20
            enemies7Y += enemies7Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 20
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -20
            enemies8Y += enemies8Y_changed
        
        # EIGHT ENEMIES MOVEMENT
        
        enemies9_X += enemies9X_changed

        if enemies9_X <= 1:
            enemies9X_changed = 20
            enemies9Y += enemies9Y_changed
        elif enemies9_X >= 736:
            enemies9X_changed = -20
            enemies9Y += enemies9Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletssss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)
        
        # NINE ENEMIES
        fivecollision = fourCollision(enemies9_X,enemies9Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies9_X,enemies9Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies9Y = random.randint(50,150)
            enemies9_X = random.randint(0,735)


        Enemies(enemies9_X, enemies9Y)
        Enemies(enemies8_X, enemies8Y)   
        Enemies(enemies7_X, enemies7Y)
        Enemies(enemiesssss_X, enemiesssssY)
        Enemy(enemiessss_X, enemiessssY)
        Enemy(enemiesss_X, enemiesssY)
        Enemy(enemiess_X, enemiessY)
        Enemy(enemies_X, enemiesY)
        Enemy(enemy_X, enemyY)
        Displaydustin(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 2 PLACE

def DDplaylevel2():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review2, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 2", font, (255, 255, 255), screen, 20, 20)

        if p_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDplay()
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                Dplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def DDplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level2, (0,0))
        draw_text("LEVEL2", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_dustin.draw(screen):
            if click:
                DDplaylevel3() 
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDplaylevel2()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 25
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -25
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 25
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -25
            enemies7Y += enemies7Y_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies8_X += enemies8X_changed

        if enemies8_X <= 1:
            enemies8X_changed = 25
            enemies8Y += enemies8Y_changed
        elif enemies8_X >= 736:
            enemies8X_changed = -25
            enemies8Y += enemies8Y_changed

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletssss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)

        # EIGHT ENEMIES
        fivecollision = fourCollision(enemies8_X,enemies8Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies8_X,enemies8Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies8Y = random.randint(50,150)
            enemies8_X = random.randint(0,735)

        
        Enemieslevel(enemies8_X, enemies8Y)
        Enemieslevel(enemies7_X, enemies7Y)
        Enemieslevel(enemiesssss_X, enemiesssssY)
        Enemieslevel2(enemiessss_X, enemiessssY)
        Enemieslevel2(enemiesss_X, enemiesssY)
        Enemieslevel2(enemiess_X, enemiessY)
        Enemieslevel2(enemies_X, enemiesY)
        Enemieslevel2(enemy_X, enemyY)
        Displaydustin(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


#LEVEL 3 PLACE

def DDplaylevel3():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review3, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 3", font, (255, 255, 255), screen, 20, 20)

        if p_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDDplay()
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def DDDplay():
     # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # SEVEN ENEMIES
    enemies7Y = random.randint(50,150)
    enemies7_X = random.randint(0,736)
    enemies7X_changed = 20
    enemies7Y_changed = 0

    # SEVEN ENEMIES
    enemies8Y = random.randint(50,150)
    enemies8_X = random.randint(0,736)
    enemies8X_changed = 20
    enemies8Y_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level3, (0,0))
        draw_text("LEVEL3", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_dustin.draw(screen):
            if click:
                DDplaylevel4()
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDplaylevel3()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 30
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -30
            enemiesssssY += enemiesssssY_changed
        
        # SEVEN ENEMIES MOVEMENT
        
        enemies7_X += enemies7X_changed

        if enemies7_X <= 1:
            enemies7X_changed = 30
            enemies7Y += enemies7Y_changed
        elif enemies7_X >= 736:
            enemies7X_changed = -30
            enemies7Y += enemies7Y_changed
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletssss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        
        # SEVEN ENEMIES
        fivecollision = fourCollision(enemies7_X,enemies7Y,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies7_X,enemies7Y))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemies7Y = random.randint(50,150)
            enemies7_X = random.randint(0,735)


        
        
        Enemieslevell(enemies7_X, enemies7Y)
        Enemieslevell(enemiesssss_X, enemiesssssY)
        Enemieslevel3(enemiessss_X, enemiessssY)
        Enemieslevel3(enemiesss_X, enemiesssY)
        Enemieslevel3(enemiess_X, enemiessY)
        Enemieslevel3(enemies_X, enemiesY)
        Enemieslevel3(enemy_X, enemyY)
        Displaydustin(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)

#LEVEL 4 PLACE

def DDplaylevel4():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(place_review4, (0, 170))
        draw_text("PLACE REVIEW FOR LEVEL 4", font, (255, 255, 255), screen, 20, 20)

        if p_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDDDplay()
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDDplay()

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        pygame.display.update()
        mainClock.tick(60)

def DDDDplay():
    # EXPLOSION EFFECT
    explosive  = pygame.image.load('assets/explode.png')

    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 20
    bullets_state = "fire"
    
    # SCORE
    score_value = 0 
    textX = 10
    textY = 10
    
    # SECOND ENEMIES
    enemiesY = random.randint(50,150)
    enemies_X = random.randint(0,736)
    enemiesX_changed = 3
    enemiesY_changed = 10

    # THIRD ENEMIES
    enemiessY = random.randint(50,150)
    enemiess_X = random.randint(0,736)
    enemiessX_changed = 3
    enemiessY_changed = 10

    # FOURT ENEMIES
    enemiesssY = random.randint(50,150)
    enemiesss_X = random.randint(0,736)
    enemiesssX_changed = 3
    enemiesssY_changed = 10

    # FIVE ENEMIES
    enemiessssY = random.randint(50,150)
    enemiessss_X = random.randint(0,736)
    enemiessssX_changed = 3
    enemiessssY_changed = 10

    # SIX ENEMIES
    enemiesssssY = random.randint(50,150)
    enemiesssss_X = random.randint(0,736)
    enemiesssssX_changed = 20
    enemiesssssY_changed = 0

    # ENEMY MOVEMENT
    enemyY = random.randint(50,150)
    enemy_X = random.randint(0,736)
    enemyX_changed = 3
    enemyY_changed = 10

    #PLAYER MOVEMENT
    playerY = 600
    playerX_changed = 0
    player_X = 370  

    running = True
    while running:
        #SCREEN
        screen.blit(places_level4, (0,0))
        draw_text("LEVEL4", font, (255, 255, 255), screen, 20, 20)

    
        if umulit_dustin.draw(screen):
            if click:
                pass 
        
        if umuulit_dustin.draw(screen):
            if click:
                partone_sound = mixer.Sound('sound/buttoneffect.wav')
                partone_sound.play()
                DDplaylevel4()

        #GAME LOOP   
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_changed = 0

            
        # BOUNDARIES OF PLAYER
        player_X += playerX_changed

        if player_X <=0:
            player_X = 0
        elif player_X >= 736:
            player_X = 736
        
        # ENEMY MOVEMENT
        
        
        enemy_X += enemyX_changed
        
        if enemy_X <= 2:
            enemyX_changed = 5
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -5
            enemyY += enemyY_changed
        
        
        # SECOND ENEMIES MOVEMENT

        # ENEMY MOVEMENT

        enemies_X += enemiesX_changed

        if enemies_X <=  2:
            enemiesX_changed = 5
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -5
            enemiesY += enemiesY_changed


        # THIRD ENEMIES MOVEMENT

        # ENEMY MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <= 2:
            enemiessX_changed = 5
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -5
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT

        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=  2:
            enemiesssX_changed = 5
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -5
            enemiessssY += enemiesssY_changed

        # FIVE ENEMIES MOVEMENT
        
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <= 2:
            enemiessssX_changed = 5
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -5
            enemiessssY += enemiessssY_changed
        
        # SIX ENEMIES MOVEMENT
        
        enemiesssss_X += enemiesssssX_changed

        if enemiesssss_X <= 1:
            enemiesssssX_changed = 40
            enemiesssssY += enemiesssssY_changed
        elif enemiesssss_X >= 736:
            enemiesssssX_changed = -40
            enemiesssssY += enemiesssssY_changed
        
        

        # BULLET MOVEMENT
        if bulletY <= 0:
            bullet_sound = mixer.Sound('sound/laser.wav')
            bullet_sound.play()    
            bulletY = 600
            bullets_state = "fire"
            bullet_X = player_X
            

        if bullets_state == "fire":
            fire_Bulletssss(bullet_X, bulletY)
            bulletY -= bulletY_changed

        # COLLISION FIRST ENEMY
        collision = isCollision(enemy_X,enemyY,bullet_X,bulletY)
        if collision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemy_X,enemyY))
            bulletY = 480
            bullets_state = "fire"
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)
            

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemies_X,enemiesY))
            bulletY = 480
            bullets_state = "fire"
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiess_X,enemiessY))
            bulletY = 480
            bullets_state = "fire"
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesss_X,enemiesssY))
            bulletY = 480
            bullets_state = "fire"
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiessss_X,enemiessssY))
            bulletY = 480
            bullets_state = "fire"
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)
        
        # SIX ENEMIES
        fivecollision = fourCollision(enemiesssss_X,enemiesssssY,bullet_X,bulletY)
        if fivecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            screen.blit(explosive, (enemiesssss_X,enemiesssssY))
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssssY = random.randint(50,150)
            enemiesssss_X = random.randint(0,735)
        

        
        
        Enemieslevelll4(enemiesssss_X, enemiesssssY)
        Enemieslevel4(enemiessss_X, enemiessssY)
        Enemieslevel4(enemiesss_X, enemiesssY)
        Enemieslevel4(enemiess_X, enemiessY)
        Enemieslevel4(enemies_X, enemiesY)
        Enemieslevel4(enemy_X, enemyY)
        Displaydustin(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)


game_menu()