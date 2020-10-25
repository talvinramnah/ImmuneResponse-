import pygame
import time
pygame.init()

GameDisplay = pygame.display.set_mode((1000,1000))
mutation = True
black = (0,0,0)
white = (255,255,255)
red = (155,0,0)
blue = (0,0,255)
green = (118,238,0)
orange = (255,128,0)
top = 0
middle = 333
bottom = 666
counter = 0
def texts(msg,x,y):
   #initialises the font thats used with size
   font=pygame.font.SysFont(None,30)
   #this renders it by converting the message to a string and it uses white text
   text=font.render(str(msg), 1,white)
   #this will blit the text to the canvas at the x and y points that are passed
   GameDisplay.blit(text, (x, y))
while mutation == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mutation = False
    pygame.draw.rect(GameDisplay,black,[0,top,1000,333])
    pygame.draw.rect(GameDisplay,blue,[0,middle,1000,333])
    pygame.draw.rect(GameDisplay,red,[0,bottom,1000,333])
    temp = top
    top = middle
    middle = temp
    temp = middle
    middle = bottom
    bottom = temp
    texts('MUTATION',500,middle)
    pygame.time.delay(150)
    counter +=1
    print(counter)
    pygame.display.update()
    
    if counter == 10:
       
      pygame.quit()
      quit()
