import pygame
import time

pygame.init()
#window size
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
#title
pygame.display.set_caption('The Chase')
#measure FPS
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def game_loop():
    
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        counter, text = 10, '10'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 30)

        run = True
        while run:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'boom!'
                if e.type == pygame.QUIT: 
                    run = False 
    
        pygame.display.update()
        clock.tick(60)
        
        
        
def crash():
    message_display('You Crashed')

def quitgame():
    pygame.quit()
    quit()
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("The Spanish Chase", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        # if GO is pressed - activate game 
        button("Start Game!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,pygame.QUIT)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
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
    
    
           
# if user quits game, stop.
game_intro()
game_loop()
pygame.quit()
quit()
