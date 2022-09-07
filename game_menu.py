

import pygame, sys
import button

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
icon = pygame.image.load('assets/alien.png')
pygame.display.set_icon(icon)

#IMAGE FUCNTIONS
def draw_text (text, font, color, surface, x, y):
    textobj =font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

#VARIABLE 
click = False
go = False

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


#SET UP OF EVERY SCREEN IN THE GAME
#CUSTOMIZE OR PUTTING A FUNCTION IN THE GAME IS ALSO IN DOWN
#GAME SET UP
#VARIABLE FUCNTION AND OTHER STAFF TO CHANGE 

# SET UP IN GAME MENU

def game_menu():
    while True:

        #SCREEN
        screen.blit(bg_image, (0,0))
        
        draw_text("Game menu", font, (255, 255, 255), screen, 20, 20)

        # SCREEN TO SCREEN
        
        if start_button.draw(screen):
            if click:
                game()
        if option_button.draw(screen):
            if click:
                option()
        if abilities_button.draw(screen):
            if click:
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
def game():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg,(0, 0))
        draw_text("Game", font, (255, 255, 255), screen, 20, 20)

        #GAME LOOP
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False

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
                information()
        if keypads_button.draw(screen):
            if click:
                keypads()
        if about_button.draw(screen):
            if click:
                about()
        if back_button.draw(screen):
            if click:
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
                bullet_tistic()
        if back_back.draw(screen):
            if click:
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
                eleven()
        if back_i.draw(screen):
            if click:
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
                raf_mania()
        if back_back.draw(screen):
            if click:
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
                kaboom()
        if back_back.draw(screen):
            if click:
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
                tripleman()
        if back_back.draw(screen):
            if click:
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
                special_b()
        if back_back.draw(screen):
            if click:
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
                mike()
        if back_i.draw(screen):
            if click:
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
                lucas()
        if back_i.draw(screen):
            if click:
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
                dustin()
        if back_i.draw(screen):
            if click:
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
                partone()
        if back_i.draw(screen):
            if click:
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
                parttwo()
        if back_i.draw(screen):
            if click:
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
game_menu()