import pygame
import random
import time
import sqlite3
pygame.init()
connect = sqlite3.connect('leaderboardTest.db')
cursor = connect.cursor()
#after initialising the library, I set a screen size of 1000X1000
GameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('immune response')
#this boolean value of gameExit allows me to create a while loop for the game
#if they would want to quit i would set it to true to exit the loop
gameExit = False
pygame.display.update
FPS = 30

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS studentTable(StudentID INTEGER, Name TEXT, Year INTEGER, Score INTEGER)")
create_table()

def fetchLives():
    cursor.execute('SELECT quizScore FROM studentScores')
    quizScoreList = cursor.fetchall()
    quizScoreTuple = quizScoreList[-1]
    


#this is a function that allows text to be rendered to the screen, it is
#called anytime a message must be output
#it takes the arguments for the message and x and y points
def texts(msg,x,y):
   #initialises the font thats used with size
   font=pygame.font.SysFont(None,30)
   #this renders it by converting the message to a string and it uses white text
   text=font.render(str(msg), 1,white)
   #this will blit the text to the canvas at the x and y points that are passed
   GameDisplay.blit(text, (x, y))
    
#using the RGB colour values I declared the colours I would use
#for the background and characters
black = (0,0,0)
white = (255,255,255)
red = (155,0,0)
blue = (0,0,255)
green = (118,238,0)
orange = (255,128,0)
#these are the new variables i have added, they say where the x and y points
#for the top left corner of the WBC is, they are put into the code for
#rendering them at the bottom of the game loop
WBC_x = 500
WBC_x_change = 0
WBC_y = 600
#this will be the initial value of the y and x co-oridnates of the pathogen 
pathogen_y = 0
pathogen_x = 500
pathogen2_x = 0
pathogen2_y = 500
pathogen3_x = 0
pathogen3_y = 500
shade_of_blue = 0
pathogen_width = 40
WBC_width = 40
cursor.execute('SELECT quizScore FROM studentScores')
quizScoreList = cursor.fetchall()
print(quizScoreList)
quizScoreTuple = quizScoreList[-1]
quizScore = quizScoreTuple[0]
print(quizScore)
##scoreFile = open('scoreFile.txt','r')
##print(scoreFile.read())
##scoreFileData = scoreFile.readline(5)
##
##print(scoreFileData)
##print(scoreFileDataElement)
##scoreFileDataString = str(scoreFileData)
##scoreFiledataInteger = int(scoreFileDataString)
lives = quizScore

score = 1
livesMsg = 'lives'
scoreMsg = 'hits'
pathogen_speed = 5
roundNumber = 1

def dataEntry(score):
    cursor.execute("INSERT INTO studentTable(Score) VALUES (?)",(score,))
    print('hello')
    connect.commit()
    
#this is the game loop, it always runs while the gameExit value is False,
#this means that when the user wants to quit the game you just change
#gameExit to true


def GameLoop(gameExit,black,white,red,blue,WBC_x,WBC_x_change,WBC_y,pathogen_y,pathogen_x,shade_of_blue,pathogen_width,
             WBC_width,lives,score,livesMsg,scoreMsg,pathogen_speed,orange,green,pathogen2_x,pathogen2_y,pathogen3_y,pathogen3_x,roundNumber):
    while gameExit == False:
        #this is the event handling loop it allows me to use the users interaction
        #as input for controling events, and character movement 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                cursor.execute('SELECT quizScore FROM studentScores')
                connect.commit()
                quizScoreList = cursor.fetchall()
                print(quizScoreList)
                quizScoreTuple = quizScoreList[-1]
                quizScore = quizScoreTuple[0]
                print(quizScore)
            #here i am asking the quesion is the user pressing left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    WBC_x_change = -25
                if event.key == pygame.K_RIGHT:
                    WBC_x_change = 25
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    WBC_x_change = 0
        
        #this is the calculation to produce a new x point that is a factor of 100
        random_pathogen_position = round(random.randrange(100,900)/100)*100
        random_pathogen2_position = round(random.randrange(100,900)/100)*100
        random_pathogen3_position = round(random.randrange(100,900)/100)*100
        #If the positions generated are equal then one of them has 100 added to them
        #this prevents them appearing on top of each each other, so they can
        #be englufed seperatly
        if random_pathogen_position == random_pathogen2_position:
           random_pathogen_position += 100

        if random_pathogen_position == random_pathogen3_position:
            random_pathogen3_position +=100

        if random_pathogen2_position == random_pathogen3_position:
           random_pathogen2_position +=100
         



        #this is an important line as it makes the change to the x point
        #this would be reflected on the canvas every frame
        WBC_x = WBC_x + WBC_x_change
        #this will move the the pathogen 25 pixels down per frame
        #adding pathogen_speed as a seperate variable allows me to adjust it as rounds change,
        #if round goes up then more pathogens are added, originally they will be at 0, this
        #will make them appear to be moving
        if roundNumber == 1 or roundNumber == 2:
            pathogen_y = pathogen_y + pathogen_speed
        if roundNumber == 3:
            pathogen_y = pathogen_y + pathogen_speed
            pathogen2_y = pathogen2_y + pathogen_speed
        if roundNumber == 4 or roundNumber >= 5:
            pathogen_y = pathogen_y + pathogen_speed
            pathogen2_y = pathogen2_y + pathogen_speed           
            pathogen3_y = pathogen3_y + pathogen_speed
        #this prevents the pathogen appearing on outside the blood vessel
        if WBC_x >= 860:
            WBC_x = 860
        elif WBC_x <= 100:
            WBC_x = 100
        #once the pathogen hits the bottom of the screen it, the y point will be
        #set back to a new point on the x axis so move down the screen again
        #when the round have gone up then the additional pathogen added and the effect
        #on number of lives will have to be accounted for with additional if statments
        if roundNumber == 1 or roundNumber == 2:
            if pathogen_y >= 1000:
                pathogen_y = 0
                pathogen_x = random_pathogen_position
                lives = lives -1
        if roundNumber == 3: 
            if pathogen_y >= 1000:
                pathogen_y = 0
                pathogen_x = random_pathogen_position
                lives = lives-1
            elif pathogen2_y >=1000:
                pathogen2_y = 0
                pathogen2_x = random_pathogen2_position
                lives = lives -1
        if roundNumber == 4 or roundNumber >=5:
            if pathogen_y >= 1000:
                pathogen_y = 0
                pathogen_x = random_pathogen_position
                lives = lives -1
            elif pathogen2_y >=1000:
                pathogen2_y = 0
                pathogen2_x = random_pathogen2_position
                lives = lives -1
            elif pathogen3_y >= 1000:
                pathogen3_y = 0
                pathogen3_x = random_pathogen3_position
                lives = lives -1
            

            
                
        #pathagon contact with WBC, if the x and y points are equal there is contact
        if (pathogen_y == WBC_y and pathogen_x == WBC_x) or (pathogen_y == WBC_y and pathogen_x<WBC_x+WBC_width and pathogen_x>WBC_x) or (pathogen_x+pathogen_width>WBC_x and pathogen_x+pathogen_width<WBC_x+WBC_width and pathogen_y == WBC_y):
            shade_of_blue += 1
            score +=1
            if shade_of_blue%2 == 1:
                blue = (0,155,255)
            elif shade_of_blue % 2 == 0:
                blue = (0,0,255)
            pathogen_y = 0
            pathogen_x = random_pathogen_position
            if score % 5 == 0:
                pathogen_speed += 2.5
                roundNumber +=1
            print(pathogen_speed)
         #contact has to be there for these additonal pathogens 
        if (pathogen2_y == WBC_y and pathogen2_x == WBC_x) or (pathogen2_y == WBC_y and pathogen2_x<WBC_x+WBC_width and pathogen2_x>WBC_x) or (pathogen2_x+pathogen_width>WBC_x and pathogen2_x+pathogen_width<WBC_x+WBC_width and pathogen2_y == WBC_y):
            pathogen2_y = 0
            pathogen2_x = random_pathogen2_position
            score+=1
        if (pathogen3_y == WBC_y and pathogen3_x == WBC_x) or (pathogen3_y == WBC_y and pathogen3_x<WBC_x+WBC_width and pathogen3_x>WBC_x) or (pathogen3_x+pathogen_width>WBC_x and pathogen3_x+pathogen_width<WBC_x+WBC_width and pathogen3_y == WBC_y):
            pathogen3_y = 0
            pathogen3_x = random_pathogen3_position
            score+=1

        #for this design sub-problem these are the characters being rendered
        GameDisplay.fill(black)
        #pathogen(s)
        pygame.draw.rect(GameDisplay,blue,[pathogen_x,pathogen_y,40,pathogen_width])
        pygame.draw.rect(GameDisplay,orange,[pathogen2_x,pathogen2_y,40,pathogen_width])
        pygame.draw.rect(GameDisplay,green,[pathogen3_x,pathogen3_y,40,pathogen_width])

        #WBC
        pygame.draw.rect(GameDisplay,white,[WBC_x,WBC_y,40,40])
        #drawing blood vessels
        pygame.draw.rect(GameDisplay,red,[0,0,100,1000])
        pygame.draw.rect(GameDisplay,red,[900,0,200,1000])
        texts(scoreMsg,100,100)
        texts(livesMsg,700,100)
        texts(lives,800,100)
        texts(score,200,100)
        #when they have run out of lives this if statement will be executed 
        if lives == 0:
            #turns canvas black
            GameDisplay.fill(black)
            #calls text function and passes the message and the co-ordinates that they are rendered at
            texts('the host is dead, the immune response had failed',200,500)
            texts('if you would like to play again press P if not press q',200,700)
            #this sleeps the display so thay have time to choose the options 
            time.sleep(5)
            #event loop, it waits for the user to press keys p or q
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                       #this resets all variables to their initial values, 
                        lives = 10
                        score = 0
                        pathogen_speed = 5
                        roundNumber = 1
                        pathogen2_y = -pathogen_width
                        pathogen3_y = -pathogen_width
                        #if they press q the game (WHILE) loop is executed
                    if event.key == pygame.K_q:
                        gameExit = True
           

        #print(scoreFile.readline(),'immune')
            
            

        pygame.display.update()
#main program
GameLoop(gameExit,black,white,red,blue,WBC_x,WBC_x_change,WBC_y,pathogen_y,pathogen_x,shade_of_blue,pathogen_width,
             WBC_width,lives,score,livesMsg,scoreMsg,pathogen_speed,orange,green,pathogen2_x,pathogen2_y,pathogen3_y,pathogen3_x,roundNumber)
dataEntry(score)
print(quizScoreList)

cursor.close
connect.close()

pygame.quit()
quit()
