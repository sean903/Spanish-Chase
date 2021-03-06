import pygame
import os
import pandas as pd
import random

pygame.init()
#window size
display_width = 900
display_height = 500

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

FPS = 60
myfont = pygame.font.SysFont("Comic Sans MS", 100)

vocab_df = pd.read_csv('./data/spanish_vocab.csv')

CHASE_LOGO_IMAGE = pygame.image.load(
    os.path.join('Assets', 'chase_logo.png'))
CHASE_LOGO = pygame.transform.scale(CHASE_LOGO_IMAGE, (300, 200))

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Chase')

# WINDOWS
def menu_window():
    gameDisplay.fill(red)
    gameDisplay.blit(CHASE_LOGO, (300, 100))
    button("Start Game!",200,350,100,50,green,bright_green,game_one)
    button("Quit",600,350,100,50,red,bright_red,pygame.QUIT)
    pygame.display.update()

def game_one_window():
    gameDisplay.fill(green)
    correct_english, correct_spanish, spanish_rand1, spanish_rand2  = answer_options()
    button_messages = [correct_spanish, spanish_rand1, spanish_rand2]
    random.shuffle(button_messages)
    
    message_display(f"What is {correct_english} in Spanish?")
    button(button_messages[0],200,250,100,50,red,bright_red)
    button(button_messages[1],400,250,100,50,red,bright_red)
    button(button_messages[2],600,250,100,50,red,bright_red)
    
    timer()
 
def timer():
    start_ticks=pygame.time.get_ticks() #starter tick
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds>10: # if more than 10 seconds close the game
        print('boom')
    print (seconds)
    # counter, text = 10, '10'.rjust(3)
    # pygame.time.set_timer(pygame.USEREVENT, 1000)
    # font = pygame.font.SysFont('Consolas', 30)
    # clock = pygame.time.Clock()

    # run = True
    # while run:
    #     for e in pygame.event.get():
    #         if e.type == pygame.USEREVENT: 
    #             counter -= 1
    #             text = str(counter).rjust(3) if counter > 0 else 'boom!'
    #         if e.type == pygame.QUIT: 
    #             run = False

    #     # gameDisplay.fill((255, 255, 255))
    #     gameDisplay.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    #     pygame.display.flip()
    #     clock.tick(60)
   
def answer_options():
    english_word = vocab_df.sample(n=1) 
    correct_english = english_word['in English'].item()
    correct_spanish = english_word['Spanish'].item()
    spanish_rand1 = vocab_df['Spanish'].sample(n=1).item()
    spanish_rand2 = vocab_df['Spanish'].sample(n=1).item()
    
    return correct_english, correct_spanish, spanish_rand1, spanish_rand2

# ITEMS ON SCREEN   
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


# FIRST PART OF GAME LOGIC
def game_one():
    game_one_window()
    
    clock = pygame.time.Clock()
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)
        

# MAIN FUNCTION        
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        menu_window()
        
    pygame.quit()

if __name__ == "__main__":
    main() 