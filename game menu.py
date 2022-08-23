

import pygame, sys
import button

mainClock = pygame.time.Clock()
from pygame.locals import *

#VARIABLE SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
bg_image = pygame.image.load("design 4.png")
start_img = pygame.image.load('start1.png')
option_img = pygame.image.load('Options1.png')
abilities_img = pygame.image.load('abilities1.png')
bg_bg = pygame.image.load('bg.png')
pygame.init()

#GAME CAPTIONS
pygame.display.set_caption('STRANGER SHOOTER GAME')

#FUNCTION SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
font = pygame.font.SysFont(None , 20)

start_button = button.Button(280, 450, start_img, 0.8)
option_button = button.Button(5, 500, option_img, 0.8)
abilities_button = button.Button(540, 500, abilities_img, 0.8)

def draw_text (text, font, color, surface, x, y):
    textobj =font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

    

#VARIABLE 
click = False

# GAME MENU SET UP
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
# GAME SET UP
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

#VARIBALES IN OPTIONS
bg_videos = pygame.image.load('videos1.png')
bg_sounds = pygame.image.load('sounds1.png')
bg_keypads = pygame.image.load('keypads1.png')
bg_about = pygame.image.load('about1.png')
bg_back = pygame.image.load('back.png')
#FUNCTIONS BUTTONS

videos_button = button.Button(280, 200, bg_videos, 0.8)
sounds_button = button.Button(280, 100, bg_sounds, 0.8)
keypads_button = button.Button(280, 300, bg_keypads, 0.8)
about_button = button.Button(280, 400, bg_about, 0.8)
back_button = button.Button(280, 500, bg_back, 0.8)

# OPTIONS SET UP
def option():
    
    while True:
        #SCREEN
        screen.blit(bg_bg, (0, 0 ))
        draw_text("OPTIONS", font, (255, 255, 255), screen, 20, 20)

        
        #SCREEN TO SCREEN 
        if videos_button.draw(screen):
            if click:
                videos()
        if sounds_button.draw(screen):
            if click:
                sounds()
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

#VARIABLES IN KEYPADS
kp_back = pygame.image.load('back.png')
kp_key = pygame.image.load('arrowkey.png')
kp_down = pygame.image.load('downkey1.png')
kp_up = pygame.image.load('upkey1.png')
kp_left = pygame.image.load('leftkey1.png')
kp_right = pygame.image.load('rightkey1.png')

#FUNCTION BUTTONS
down_kp = button.Button(280, 300, kp_down, 0.8)
up_kp = button.Button(280, 200, kp_up, 0.8)
left_kp = button.Button(280, 400, kp_left, 0.8)
right_kp = button.Button(280, 500, kp_right, 0.8)
key_kp = button.Button(280, 100, kp_key, 0.8)
back_kp = button.Button(15, 500, kp_back, 0.8)

# KEYPADS SET UP
def keypads():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        draw_text("KEYPADS", font, (255, 255, 255), screen, 20, 20)
        
        
        #SCREEN TO SCREEN
        
        if back_kp.draw(screen):
            if click:
                option()
        if key_kp.draw(screen):
            pass
        if down_kp.draw(screen):
            pass  
        if up_kp.draw(screen):
            pass
        if left_kp.draw(screen):
            pass
        if right_kp.draw(screen):
            pass
        
        

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

#VARIABLE IN ABILITIES
ab_back = pygame.image.load('back.png')

#FUNCTION BUTTON
back_ab = button.Button(15, 500, ab_back, 0.8)

# ABILITIES SET UP
def abilities():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        draw_text("ABILITIES", font, (255, 255, 255), screen, 20, 20)


        if back_ab.draw(screen):
            if click:
                game_menu

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

#VARIABLES IN SOUNDS
s_back = pygame.image.load('back.png')

#FUCTIONS BUTTON
back_s = button.Button(15, 500, s_back, 0.8)

# SOUNDS SET UP
def sounds():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        draw_text("SOUNDS", font, (255, 255, 255), screen, 20, 20)

        if back_s.draw(screen):
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

#VARIBALE IN VIDEOS
v_back = pygame.image.load('back.png')

#FUCTIONS BUTTON
back_v = button.Button(15, 500, v_back, 0.8)

# VIDEOS SET UP
def videos():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        draw_text("VIDEOS", font, (255, 255, 255), screen, 20, 20)

        if back_v.draw(screen):
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

#VARIABLE IN ABOUT
a_back = pygame.image.load('back.png')

#FUNCTION BUTTON
back_a = button.Button(15, 500, a_back, 0.8)

# ABOUT SET UP
def about():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
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
game_menu()