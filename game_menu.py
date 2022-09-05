
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

#IMAGE FUCNTIONS
def draw_text (text, font, color, surface, x, y):
    textobj =font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

#VARIABLE 
click = False

# IMAGE LIBRARY
# IMAGE IN GAME MENU
bg_image = pygame.image.load("assets/design 4.png")
start_img = pygame.image.load('assets/start1.png')
option_img = pygame.image.load('assets/Options1.png')
abilities_img = pygame.image.load('assets/abilities1.png')
bg_bg = pygame.image.load('assets/bg.png')

# FUNCTION BUTTONS IN GAME MENU

start_button = button.Button(280, 450, start_img, 0.8)
option_button = button.Button(5, 500, option_img, 0.8)
abilities_button = button.Button(540, 500, abilities_img, 0.8)

# IMAGE IN OPTIONS

bg_videos = pygame.image.load('assets/videos1.png')
bg_sounds = pygame.image.load('assets/sounds1.png')
bg_keypads = pygame.image.load('assets/keypads1.png')
bg_about = pygame.image.load('assets/about1.png')
bg_back = pygame.image.load('assets/back.png')

# FUNCTION BUTTONS IN OPTIONS

videos_button = button.Button(280, 200, bg_videos, 0.8)
sounds_button = button.Button(280, 100, bg_sounds, 0.8)
keypads_button = button.Button(280, 300, bg_keypads, 0.8)
about_button = button.Button(280, 400, bg_about, 0.8)
back_button = button.Button(280, 500, bg_back, 0.8)

# IMAGE IN KEYPADS

kp_back = pygame.image.load('assets/back.png')
kp_key = pygame.image.load('assets/arrowkey.png')
kp_down = pygame.image.load('assets/downkey1.png')
kp_up = pygame.image.load('assets/upkey1.png')
kp_left = pygame.image.load('assets/leftkey1.png')
kp_right = pygame.image.load('assets/rightkey1.png')

# FUNCTION BUTTON IN KEYPADS

back_kp = button.Button(15, 500, kp_back, 0.8)

# IMAGE IN SOUNDS

s_back = pygame.image.load('assets/back.png')

# FUNCTION BUTTON IN SOUNDS

back_s = button.Button(15, 500, s_back, 0.8)

# IMAGE IN VIDEOS

v_back = pygame.image.load('assets/back.png')

# FUNCTION BUTTON IN VIDEOS

back_v = button.Button(15, 500, v_back, 0.8)

# IMAGE IN ABOUT

a_back = pygame.image.load('assets/back.png')

# FUNCTION BUTTON IN ABOUTS

back_a = button.Button(15, 500, a_back, 0.8)


# IMAGE IN ABILITIES

ab_back = pygame.image.load('assets/back.png')
b_next = pygame.image.load('assets/next.png')

# FUNCTION BUTTON IN ABILITIES

back_ab = button.Button(15, 500, ab_back, 0.8)
next_b = button.Button(540, 500, b_next, 0.8)
ab_ab1 = button.Button(540, 500, b_next, 0.8)


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


# SET UP IN KEYPADS

def keypads():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        screen.blit(kp_down, (280, 300))
        screen.blit(kp_up, (280, 200))
        screen.blit(kp_left, (280, 400))
        screen.blit(kp_right, (280, 500))
        screen.blit(kp_key, (280, 100))

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


# SET UP IN VIDEOS

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



# SET UP IN ABOUTS

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


# SET UP IN ABILITIES

def abilities():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        

        draw_text("ABILITIES", font, (255, 255, 255), screen, 20, 20)
        

        if back_ab.draw(screen):
            if click:
                option()
        click = False
        if next_b.draw(screen):
            if click:
                game_menu()          
        if ab_ab1.draw(screen):
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


# SET UP IN FIRST ABILITIES

def bullets():
    running = True
    while running:
        #SCREEN
        screen.blit(bg_bg, (0,0))
        draw_text("ABILITIES", font, (255, 255, 255), screen, 20, 20)

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