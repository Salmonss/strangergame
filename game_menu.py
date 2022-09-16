
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
option_button = button.Button(5, 500, option_img, 0.8)
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


# IMAGE IN ABILITIES

b_next = pygame.image.load('assets/next.png')
l_abilities = pygame.image.load('assets/abilitieslogo.png')
back_z = pygame.image.load('assets/back.png')


# FUNCTION BUTTON IN ABILITIES

forward_n = button.Button(399, 520, b_next, 0.8)
abilities_l = button.Button(0, 120, l_abilities, 1.0)
back_back = button.Button(120, 520, back_z, 0.8)


# IMAGE IN BULLETISTIC
f_bulletistic = pygame.image.load('assets/bulletistic.png')

# IMAGE IN RAFMANIA
f_rafmania = pygame.image.load('assets/rafmania.png')


# IMAGE IN KABOOM

f_kaboom = pygame.image.load('assets/kaboom.png')

# IMAGE IN TRIPLEMAN

f_tripleman = pygame.image.load('assets/tripleman.png')

# IMAGE IN SPECIAL B

f_specialb = pygame.image.load('assets/specialb.png')

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
b_bselection = pygame.image.load('assets/back.png')
balik_lobby = pygame.image.load('assets/lobbybutton.png')

# FUNCTION IN SELECTION SCREEN

eleven_button = button.Button(1, 310, b_eleven, 0.7)
mike_button = button.Button(190, 310, b_mike, 0.7)
lucas_button = button.Button(380, 310, b_lucas, 0.7)
dustin_button = button.Button(580, 310, b_dustin, 0.7)
lobby_button = button.Button(270, 570, balik_lobby, 0.8)

# IMAGE IN PLACE REVIEW 

place_r = pygame.image.load('assets/placereview.png')
E_for = pygame.image.load('assets/elevenbutton.png')
M_for = pygame.image.load('assets/mikebutton.png')
L_for = pygame.image.load('assets/lucasbutton.png')
D_for = pygame.image.load('assets/dustinbutton.png')


#BUTTON IN PLACE REVIEW

p_eleven = button.Button(270, 530, E_for, 0.8)
p_mike = button.Button(270, 530, M_for, 0.8)
p_lucas = button.Button(270, 530, L_for, 0.8)
p_dustin = button.Button(270, 530, D_for, 0.8)


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
            
        if abilities_button.draw(screen):
            if click:
                abilities_sound = mixer.Sound('sound/buttoneffect.wav')
                abilities_sound.play()
                abilities()
        

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

        if lobby_button.draw(screen):
            if click:
                dbutton_sound = mixer.Sound('sound/buttoneffect.wav')
                dbutton_sound.play()
                game_menu()   

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


# SET UP IN ABILITIES
def abilities():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0 ))
        

        draw_text("ABILITIES", font, (255, 255, 255), screen, 20, 20)
        
        #SCREEN TO SCREEN 
        if forward_n.draw(screen):
            if click:
                forward_sound = mixer.Sound('sound/buttoneffect.wav')
                forward_sound.play()
                bullet_tistic()
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                game_menu()
        
        if abilities_l.draw(screen):
            if click:
                pass          
            
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


# SET UP IN FIRST ABILITIES

def bullet_tistic():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(f_bulletistic, (0,100))
        draw_text("BULLETISTIC", font, (255, 255, 255), screen, 20, 20)
        
        if forward_n.draw(screen):
            if click:
                rafmania_sound = mixer.Sound('sound/buttoneffect.wav')
                rafmania_sound.play()
                raf_mania()
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                abilities()
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


# SET UP IN SECOND ABILITIES

def raf_mania():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(f_rafmania, (0,100))
        draw_text("RAFMANIA", font, (255, 255, 255), screen, 20, 20)
        
        if forward_n.draw(screen):
            if click:
                kaboom_sound = mixer.Sound('sound/buttoneffect.wav')
                kaboom_sound.play()
                kaboom()
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                bullet_tistic()
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


# SET UP IN THIRD ABILITIES

def kaboom():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(f_kaboom, (0,100))
        draw_text("KABOOM", font, (255, 255, 255), screen, 20, 20)
        
        if forward_n.draw(screen):
            if click:
                tripleman_sound = mixer.Sound('sound/buttoneffect.wav')
                tripleman_sound.play()
                tripleman()
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                raf_mania()
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


# SET UP IN FOURT ABILITIES

def tripleman():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(f_tripleman, (0,100))
        draw_text("TRIPLEMAN", font, (255, 255, 255), screen, 20, 20)
        
        if forward_n.draw(screen):
            if click:
                specialb_sound = mixer.Sound('sound/buttoneffect.wav')
                specialb_sound.play()
                special_b()
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                kaboom()
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

# SET UP IN FIVE ABILITIES

def special_b():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_background, (0,0))
        screen.blit(f_specialb, (0,100))
        draw_text("SPECIAL B", font, (255, 255, 255), screen, 20, 20)
        
        
        if back_back.draw(screen):
            if click:
                back_sound = mixer.Sound('sound/buttoneffect.wav')
                back_sound.play()
                tripleman()
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
                pass
 
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
                pass
 
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
                pass
 
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
bullets_eleven = pygame.image.load('assets/bullet.png')
places_level = pygame.image.load("assets/level1place.png")

# DISPLAY 
def Display(x,y):
    screen.blit(player_eleven, (x,y))
# ENEMY
def Enemy(x,y):
    screen.blit(enemy_eleven, (x,y))
    
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


def Eplay():


    # BULLET MOVEMENT
    bullets_eleven = pygame.image.load("assets/bullet.png")
    bullet_X = 0
    bulletY = 600
    bulletX_changed = 0
    bulletY_changed = 15
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
        #GAME LOOP   
        
        for event in pygame.event.get():
        
            if event.type == QUIT:
                running = False
                sys.exit()    
            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_changed = -5
                if event.key == pygame.K_RIGHT:
                    playerX_changed = 5
                    

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
        
        if enemy_X <=0:
            enemyX_changed = 3
            enemyY += enemyY_changed
        elif enemy_X >= 736:
            enemyX_changed = -3
            enemyY += enemyY_changed

        # SECOND ENEMIES MOVEMENT
        enemies_X += enemiesX_changed

        if enemies_X <=0:
            enemiesX_changed = 3
            enemiesY += enemiesY_changed
        elif enemies_X >= 736:
            enemiesX_changed = -3
            enemiesY += enemiesY_changed

        # THIRD ENEMIES MOVEMENT
        enemiess_X += enemiessX_changed

        if enemiess_X <=0:
            enemiessX_changed = 3
            enemiessY += enemiessY_changed
        elif enemiess_X >= 736:
            enemiessX_changed = -3
            enemiessY += enemiessY_changed

        # FOURT ENEMIES MOVEMENT
        enemiesss_X += enemiesssX_changed

        if enemiesss_X <=0:
            enemiesssX_changed = 3
            enemiesssY += enemiesssY_changed
        elif enemiesss_X >= 736:
            enemiesssX_changed = -3
            enemiesssY += enemiessY_changed

        # FIVE ENEMIES MOVEMENT
        enemiessss_X += enemiessssX_changed

        if enemiessss_X <=0:
            enemiessssX_changed = 3
            enemiessssY += enemiessssY_changed
        elif enemiessss_X >= 736:
            enemiessssX_changed = -3
            enemiessssY += enemiesssY_changed

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
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemyY = random.randint(50,150)
            enemy_X = random.randint(0,735)

        # SECOND ENEMIES
        onecollision = oneCollision(enemies_X,enemiesY,bullet_X,bulletY)
        if onecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesY = random.randint(50,150)
            enemies_X = random.randint(0,735)

        # THIRD ENEMIES
        twocollision = twoCollision(enemiess_X,enemiessY,bullet_X,bulletY)
        if twocollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiessY = random.randint(50,150)
            enemiess_X = random.randint(0,735)
        
        # FOURT ENEMIES
        threecollision = twoCollision(enemiesss_X,enemiesssY,bullet_X,bulletY)
        if threecollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiesssY = random.randint(50,150)
            enemiesss_X = random.randint(0,735)
        
        # FIVE ENEMIES
        fourtcollision = twoCollision(enemiessss_X,enemiessssY,bullet_X,bulletY)
        if fourtcollision:
            bullet_sound = mixer.Sound('sound/explosion.wav')
            bullet_sound.play()
            bulletY = 480
            bullets_state = "fire"
            score_value += 1
            print(score_value)
            enemiessssY = random.randint(50,150)
            enemiessss_X = random.randint(0,735)

        Enemy(enemiessss_X, enemiessssY)
        Enemy(enemiesss_X, enemiesssY)
        Enemy(enemiess_X, enemiessY)
        Enemy(enemies_X, enemiesY)
        Enemy(enemy_X, enemyY)
        Display(player_X,playerY)
        pygame.display.update()
        mainClock.tick(60)

game_menu()