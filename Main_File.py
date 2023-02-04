import pygame
import random
from pygame.locals import *
pygame.init() 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("trialname") 
red = (255,0,0)
green = (0,255,0)

clock = pygame.time.Clock()
foodx = (random.randint(0,600) // 10) * 10
foody = (random.randint(0,600) // 10) * 10
snakex = (random.randint(0,600) // 10) * 10
snakey = (random.randint(0,600) // 10) * 10
snakelist = []
snakelist.append([snakex,snakey])
up = 0
down = 0
left = 0
right = 0
score = 0
v = 20
def show_text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("freesans",size, bold=True, italic=True)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

while True:
    clock.tick(v)
    screen.fill((0,0,0))
    show_text("SCORE: " + str(score),0,0,red,25)
    pygame.draw.rect(screen,red,(foodx,foody,10,10))
    for s in snakelist:
        pygame.draw.rect(screen,green,s+[10,10])
    if snakex > 600:
        snakex = 10
    if snakex < 0:
        snakex = 590
    if snakey < 0:
        snakey = 590
    if snakey > 600:
        snakey = 10
    if (snakex, snakey) == (foodx, foody):
        score = score + 1
        foodx = (random.randint(0,600) // 10) * 10
        foody = (random.randint(0,600) // 10) * 10
        snakelist.append([foodx,foody])
    if up == 1:
        snakey = snakey - 10
    if down == 1:
        snakey = snakey + 10
    if left == 1:
        snakex = snakex - 10
    if right == 1:
        snakex = snakex + 10
    snakelist.pop()
    snakelist.insert(0,[snakex,snakey])
    if score == 10:
        clock.tick(25)
        snakelist = [[snakex,snakey]]
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP and down == 0:
                up = 1
                down = 0
                left = 0
                right = 0
            if event.key == K_DOWN and up == 0:
                down = 1
                up = 0
                left = 0
                right = 0
            if event.key == K_LEFT and right == 0:
                left = 1
                up = 0
                down = 0
                right = 0
            if event.key == K_RIGHT and left == 0:
                right = 1
                up = 0
                down = 0
                left = 0
        if event.type == QUIT: 
            pygame.quit()
            exit()
    if [snakex,snakey] in snakelist[1:]:
        show_text("GAME OVER!",250,300,red,50)
        pygame.display.update()
        break
    pygame.display.update()
