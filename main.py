import pygame
import os

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

CHASE_LOGO_IMAGE = pygame.image.load(
    os.path.join('Assets', 'chase_logo.png'))
CHASE_LOGO = pygame.transform.scale(CHASE_LOGO_IMAGE, (300, 200))

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Chase')

def draw_window():
    gameDisplay.fill(red)
    gameDisplay.blit(CHASE_LOGO, (300, 100))
    button("Start Game!",150,450,100,50,green,bright_green,game_loop)
    button("Quit",550,450,100,50,red,bright_red,pygame.QUIT)
    pygame.display.update()
    
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

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_loop():
    gameDisplay.fill(white)
    clock = pygame.time.Clock()
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    
        pygame.display.update()
        clock.tick(60)
        
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
        
    pygame.quit()

if __name__ == "__main__":
    main() 