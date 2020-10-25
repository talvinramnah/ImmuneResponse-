open('user.txt', 'w').close()

usernameTextFile = open('user.txt','w')
import sqlite3
from appJar import gui


app = gui('login','500x500')
app.setFont(20)

connect = sqlite3.connect('leaderboardTest.db')
cursor = connect.cursor()


#this adds a title for the window
app.addLabel('title','Sign Up Here!',0,0,2)
app.setLabelBg('title','blue')

app.addValidationEntry('username',1,0)
app.setEntryDefault('username','enter your username here')
app.addValidationEntry('password', 2,0,True)
app.setEntryDefault('password','enter your password here')

cursor.execute("SELECT Username FROM studentInformationTable4")
usernameList = cursor.fetchall()
cursor.execute("SELECT Password FROM studentInformationTable4")
passwordList = cursor.fetchall()
username = app.getEntry('username')


def stopGUI(self):
    app.stop()

def LoginChecker(self):
    index = -1
    passwordIndex = 0
    hashValue = 0
    username = app.getEntry('username')
    password = app.getEntry('password')
    for i in usernameList:
        index +=1
        if username in i:
            print(index)
            print(usernameList[index])
            for everyLetter in password:
                passwordIndex+=1
                hashValue += ord(str(everyLetter))
                print(hashValue)
                print(passwordList[index])
                passwordTuple = passwordList[index]
                print(passwordTuple[0])
                if int(hashValue)==  int(passwordTuple[0]):
                    app.infoBox('huzzah','your username and password were correct, press OK to begin')
                    app.setEntryValid('username')
                    app.setEntryValid('password')
                    #cursor.execute("INSERT INTO studentScores(Username) VALUES (?)",(username,))
                    #connect.commit()
##                    cursor.close()
##                    connect.close()
                    
                    str(username)
                    usernameTextFile.write(username)
                    usernameTextFile.close()
                    app.addButton('go to game',stopGUI,3,1)
                if int(hashValue)!= int(passwordTuple[0]) and passwordIndex == len(password):
                    app.infoBox('error','your password did not match, try again')
    
        if index == len(usernameList):
            app.infoBox('error','your username was not found, go back and register first!')
            break
app.addButton('press',LoginChecker,3,0)

app.go()
def miniLB():
    from appJar import gui
    import sqlite3
    import operator
    app = gui('mini leaderboard','300x400')
    connect = sqlite3.connect('leaderboardTest.db')
    cursor = connect.cursor()
    app.setFont('20')
    x = 0
    def quitFunc(self):
        app.stop()
        
    cursor.execute("SELECT Username,GameHits FROM studentScores ORDER BY GameHits desc")
    leaderboard = cursor.fetchall()
    gameElements = list(map(operator.itemgetter(1), leaderboard))
    usernameElements = list(map(operator.itemgetter(0), leaderboard))

    app.setTransparency(75)
    app.setBg('grey')
    app.addLabel('username','USERNAME',0,0)
    app.addLabel('score','SCORE',0,1)
    for i in range (5):

        app.addLabel(i,usernameElements[i],i+1)
        app.addLabel(i+10,gameElements[i],i+1,1)
        
    app.addButton('QUIT',quitFunc,6,0)
    app.go()
    cursor.close()
    connect.close()
    
def gameCallFunc(quizScoreNew):
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
    insertQuizScore = quizScoreNew
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
##    cursor.execute('SELECT quizScore FROM studentScores')
##    quizScoreList = cursor.fetchall()
##    print(quizScoreList)
##    quizScoreTuple = quizScoreList[-1]
##    quizScore = quizScoreTuple[0]
##    print(quizScore)
    ##scoreFile = open('scoreFile.txt','r')
    ##print(scoreFile.read())
    ##scoreFileData = scoreFile.readline(5)
    ##
    ##print(scoreFileData)
    ##print(scoreFileDataElement)
    ##scoreFileDataString = str(scoreFileData)
    ##scoreFiledataInteger = int(scoreFileDataString)
    lives = quizScoreNew

    score = 1
    livesMsg = 'lives'
    scoreMsg = 'hits'
    pathogen_speed = 5
    roundNumber = 1
    mutation = False
    def dataEntry(score):
        cursor.execute("INSERT INTO studentTable(Score) VALUES (?)",(score,))
        print('hello')
        connect.commit()
        
    #this is the game loop, it always runs while the gameExit value is False,
    #this means that when the user wants to quit the game you just change
    #gameExit to true


    def GameLoop(gameExit,black,white,red,blue,WBC_x,WBC_x_change,WBC_y,pathogen_y,pathogen_x,shade_of_blue,pathogen_width,
                 WBC_width,lives,score,livesMsg,scoreMsg,pathogen_speed,orange,green,pathogen2_x,pathogen2_y,pathogen3_y,pathogen3_x,roundNumber,mutation,insertQuizScore):
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
                mutation = True
            if roundNumber == 4 or roundNumber >= 5:
                mutation = False
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
                if mutation == False:
                    score +=1
                if mutation == True:
                    lives -=1
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
                if mutation == False:
                    score+=1
                if mutation == True:
                    lives-=1
            if (pathogen3_y == WBC_y and pathogen3_x == WBC_x) or (pathogen3_y == WBC_y and pathogen3_x<WBC_x+WBC_width and pathogen3_x>WBC_x) or (pathogen3_x+pathogen_width>WBC_x and pathogen3_x+pathogen_width<WBC_x+WBC_width and pathogen3_y == WBC_y):
                pathogen3_y = 0
                pathogen3_x = random_pathogen3_position
                if mutation == False:
                    score+=1
                if mutation == True:
                    lives-=1

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
                            usernameTextFile = open('user.txt','r')
                            username = usernameTextFile.read()
                            str(username)
                            import datetime
                            import operator
                            unix = int(time.time())
                            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
                            cursor.execute("SELECT Username,quizScore FROM studentScores")
                            usernamesAndquizScore = cursor.fetchall()
                            usernames = list(map(operator.itemgetter(0),usernamesAndquizScore))
                            quizScores = list(map(operator.itemgetter(1),usernamesAndquizScore))
                            #checks if user in DB already
                            if username in usernames:
                                #if they are it gets their score using index from usrname list
                                scoreInLBIndex = usernames.index(username)
                                scoreInLB = quizScores[scoreInLBIndex]
                                int(scoreInLB)
                                #checks if new score is higher than one in DB
                                if insertQuizScore>scoreInLB:
                                    #if it is previous record deleted
                                    deletingPreviousRecord = "DELETE FROM studentScores WHERE Username = '%s'" %username
                                    cursor.execute(deletingPreviousRecord)
                                    #new score and other deital inserted
                                    cursor.execute("INSERT INTO studentScores(GameHits,quizScore,Username,date) VALUES (?,?,?,?)",(score,insertQuizScore,username,date))
                            #if username not in DB score is added
                            if username not in usernames:
                                cursor.execute("INSERT INTO studentScores(GameHits,quizScore,Username,date) VALUES (?,?,?,?)",(score,insertQuizScore,username,date))




            

                            connect.commit()
                            usernameTextFile.close()
               

            #print(scoreFile.readline(),'immune')
                
                

            pygame.display.update()
    #main program
    GameLoop(gameExit,black,white,red,blue,WBC_x,WBC_x_change,WBC_y,pathogen_y,pathogen_x,shade_of_blue,pathogen_width,
                 WBC_width,lives,score,livesMsg,scoreMsg,pathogen_speed,orange,green,pathogen2_x,pathogen2_y,pathogen3_y,pathogen3_x,roundNumber,mutation,insertQuizScore)
    cursor.close()
    connect.close()
    miniLB()


    pygame.quit()
    quit()






from appJar import gui
import sqlite3
app = gui('question engine','800x800')

connect = sqlite3.connect('leaderboardTest.db')
cursor = connect.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS studentScores(quizScore INTEGER, GameHits INTEGER, Username TEXT,date TEXT)")
create_table()

#opening up the textfile document mcw.txt in write mode
TextFile =  open('mcq.txt','w')
#writing questions to textfile in the format of question on one line the next four lines
#have each option, the last line has the answer a total of 6 lines per question
TextFile.write('Question: Which of the following bonds are broken during DNA replication?\n')
TextFile.write('A: Ionic bonds\n')
TextFile.write('B: Hydrogen bonds\n')
TextFile.write('C: covalent bonds \n')
TextFile.write('D: phosphodiester bonds \n')
TextFile.write('option B hydrogen bonds \n')
TextFile.write('Question: Where does sucrose go from and to in a plant\n')
TextFile.write('A: source to sink \n')
TextFile.write('B: leaf to root \n')
TextFile.write('C: root to leaf \n')
TextFile.write('D: sink to source \n')
TextFile.write('option A source to sink \n')
TextFile.write('Question: What is the enzyme that allows carbonic acid to form \n')
TextFile.write('A: amylase \n')
TextFile.write('B: lactase \n')
TextFile.write('C: carbonic anhydrase\n')
TextFile.write('D: catalase\n')
TextFile.write('option C carbonic anhydrase \n')
TextFile.write('Question: what cell is responsible for manufacturing antibodies \n')
TextFile.write('A: plasma cells \n')
TextFile.write('B: T killer cells \n')
TextFile.write('C: B lymphocytes \n')
TextFile.write('D: opsonins \n')
TextFile.write('option A plasma cells \n')
TextFile.write('Questions: what is the process of grouping pathogens together \n')
TextFile.write('A: agglutination \n')
TextFile.write('B: opsonination\n')
TextFile.write('C: anti toxination \n')
TextFile.write('D: inhibition \n')
TextFile.write('option A agglutination \n')
TextFile.write('Question: how many chambers in the heart\n')
TextFile.write('A: 1\n')
TextFile.write('B: 2\n')
TextFile.write('C: 3\n')
TextFile.write('D: 4\n')
TextFile.write('option D 4 \n')
TextFile.write('Question: what circulation gets oxygen into the blood\n')
TextFile.write('A: single\n')
TextFile.write('D: systemic\n')
TextFile.write('D: double\n')
TextFile.write('D: pulmunory\n')
TextFile.write('option D pulmunaro \n')
TextFile.write('Question: what type of structure is the amino acid sequence\n')
TextFile.write('A: quartenary\n')
TextFile.write('B: tertiary\n')
TextFile.write('C: primary\n')
TextFile.write('D: secondary\n')
TextFile.write('option C  primary \n')
TextFile.write('Question: what colour does stach turn if iodide ions added\n')
TextFile.write('A: black\n')
TextFile.write('B: blue\n')
TextFile.write('C: lilac\n')
TextFile.write('D: yellow\n')
TextFile.write('Question: what type of protein does regulatory region produce \n')
TextFile.write('option A enzyme \n')
TextFile.write('option B hormone \n')
TextFile.write('option C repressor \n')
TextFile.write('option D structural \n')
TextFile.write('option C repressor \n')


TextFile.close()

TextFile = open('mcq.txt','r')
#loading up questions in a list using the readlines() function
questionsQueue = TextFile.readlines()
#index's in questionsQueue list of options and questions
currentQuestion = 0
currentOptionA = 1
currentOptionB = 2
currentOptionC = 3
currentOptionD = 4
currentAnswerIndex = 5
#text for drop area label
dropAreaText = 'please drop your answer here'
questionLabelColour = 'blue'
optionALabelColour = 'red'
optionBLabelColour = 'orange'
optionCLabelColour = 'yellow'
optionDLabelColour = 'green'
answer = questionsQueue[currentAnswerIndex]
selected = ' '
score = 1


#overall function for questions engine
def visuals(currentQuestion,currentOptionA,currentOptionB,
            currentOptionC,currentOptionD,currentAnswer,dropAreaText,selected):
    #these are the functions called when an option is dragged/dropped
    def dragA(self):
        app.setLabelBg('optionBLabel',optionBLabelColour)
        app.setLabelBg('optionCLabel',optionCLabelColour)
        app.setLabelBg('optionDLabel',optionDLabelColour)
        app.setLabelBg('optionALabel','white')
    def dropA(self):
        app.setLabelBg('dropArea',optionALabelColour)
        global selected
        selected = 'A'
        app.addButton('submit A',submitFunc,7,1,1)
    def dragB(self):
        app.setLabelBg('optionALabel',optionALabelColour)
        app.setLabelBg('optionCLabel',optionCLabelColour)
        app.setLabelBg('optionDLabel',optionDLabelColour)
        app.setLabelBg('optionBLabel','white')
    def dropB(self):
        app.setLabelBg('dropArea',optionBLabelColour)
        global selected
        selected = 'B'
        app.addButton('submit B',submitFunc,7,1,1)

    def dragC(self):
        app.setLabelBg('optionALabel',optionALabelColour)
        app.setLabelBg('optionBLabel',optionBLabelColour)
        app.setLabelBg('optionDLabel',optionDLabelColour)
        app.setLabelBg('optionCLabel','white')
    def dropC(self):
        app.setLabelBg('dropArea',optionCLabelColour)
        global selected
        selected = 'C'
        app.addButton('submit C',submitFunc,7,1,1)

    def dragD(self):
        app.setLabelBg('optionALabel',optionALabelColour)
        app.setLabelBg('optionCLabel',optionCLabelColour)
        app.setLabelBg('optionBLabel',optionBLabelColour)
        app.setLabelBg('optionDLabel','white')
    def dropD(self):
        app.setLabelBg('dropArea',optionDLabelColour)
        global selected
        selected = 'D'
        app.addButton('submit D',submitFunc,7,1,1)



    #initialising labels with title,text and position
    app.addLabel('questionLabel',questionsQueue[currentQuestion],1,1,1)
    app.addLabel('optionALabel',questionsQueue[currentOptionA],2,1,1)
    app.addLabel('optionBLabel',questionsQueue[currentOptionB],3,1,1)
    app.addLabel('optionCLabel',questionsQueue[currentOptionC],4,1,1)
    app.addLabel('optionDLabel',questionsQueue[currentOptionD],5,1,1)
    currentAnswer = questionsQueue[currentAnswerIndex]
    #the drop area label will flash black and white
    app.addFlashLabel('dropArea',dropAreaText,6,1,1)
    #setting the colour and dont size for the labels
    app.setFont(20)
    app.setLabelBg('questionLabel',questionLabelColour)
    app.setLabelBg('optionALabel',optionALabelColour)
    app.setLabelBg('optionBLabel',optionBLabelColour)
    app.setLabelBg('optionCLabel',optionCLabelColour)
    app.setLabelBg('optionDLabel',optionDLabelColour)

    #these functions from appJar take the title of label and a list
    #with the function for dragging/dropping the label
    #each label has a different function
    app.setLabelDragFunction('optionALabel',[dragA,dropA])
    app.setLabelDragFunction('optionBLabel',[dragB,dropB])
    app.setLabelDragFunction('optionCLabel',[dragC,dropC])
    app.setLabelDragFunction('optionDLabel',[dragD,dropD])
    #adding the scale so the user can change question from 1 - 40
    app.addScale('progress',9,1,1)
    app.setScaleRange('progress' ,1,40)
    app.showScaleIntervals('progress',1)
    app.showScaleValue('progress',True)
    currentQuestionProgress = app.getScale('progress')
    #this built-in function allows the function questionFetcher to
    #be called whenever the scale is changed
    app.setScaleChangeFunction('progress', questionFetcher)

    app.addLabel('scoreLabel',score,8,1,1)
    


def questionFetcher(self):
    #when the questions changes the colour of drop area changes back to white
    app.setLabelBg('dropArea','white')
    #this variable gets the question number
    currentQuestionProgress = app.getScale('progress')
    #uses the nth term to find the index of question in list
    global currentOptionA
    global currentOptionB
    global currentOptionC
    global currentOptionD
    global answer
    global score
    print(score)
    currentQuestion  = (6*currentQuestionProgress)- 6
    currentOptionA = currentQuestion+1
    currentOptionB = currentOptionA+1
    currentOptionC = currentOptionB+1
    currentOptionD = currentOptionC +1
    currentAnswerIndex = currentOptionD+1
    answer = questionsQueue[currentAnswerIndex]

    #these change the text of the labels to that questions respective options
    app.setLabel('questionLabel',questionsQueue[currentQuestion])
    app.setLabel('optionALabel',questionsQueue[currentOptionA])
    app.setLabel('optionBLabel',questionsQueue[currentOptionB])
    app.setLabel('optionCLabel',questionsQueue[currentOptionC])
    app.setLabel('optionDLabel',questionsQueue[currentOptionD])
    app.setLabelBg('optionALabel',optionALabelColour)
    app.setLabelBg('optionCLabel',optionCLabelColour)
    app.setLabelBg('optionBLabel',optionBLabelColour)
    app.setLabelBg('optionDLabel',optionDLabelColour)
    if currentQuestionProgress % 7 == 0:
        gameCallFunc(score)

##        cursor.execute('INSERT INTO studentScores(quizScore) VALUES (?)',(score,))
##        connect.commit
##        cursor.execute('SELECT Username FROM studentScores')
##        data = cursor.fetchall()
##        connect.commit
##        print(data)
##        cursor.close()
##        connect.close()
##        import immuneresponsev3


    return currentQuestion,currentOptionA,currentOptionB,currentOptionC,currentOptionD

def callGame():
        cursor.execute('INSERT INTO studentScores(quizScore) VALUES (?)',(score,))
        connect.commit
        cursor.execute('SELECT quizScore FROM studentScores')
        data = cursor.fetchall()
        connect.commit
        print(data)
        cursor.close()
        connect.close()

def submitFunc(self):
    #these pass in the global variables as appJar doesn't let
    # you do that through buttons    
    global score
    global selected
    global answer
    #this witness statement prints the option letter
    #at the answer line, it's always the 7th string element 
    print(answer[7])
    #this is a variable that is set when an option is dropped
    #if they drop A selected goes from ' '  to 'A'
    #it is used as a condition in this function
    print(selected)
    #if the option answer letter is equal to the option they dropped
    #score is increased by 1 
    if answer[7] == 'A' and selected == 'A':
        score = score +1
        print(score)
        app.removeButton('submit A')

    if answer[7] == 'B' and selected == 'B':
        score = score +1
        print(score)
        app.removeButton('submit B')

    if answer[7] == 'C' and selected == 'C':
        score = score +1
        print(score)
        app.removeButton('submit C')

    if answer[7] == 'D' and selected == 'D':
        score = score +1
        print(score)
        app.removeButton('submit D')

    #once they have pressed the submit button it is removed
    #this prevents cheating through double pressing
    #this updates the score label to the current score 
    app.setLabel('scoreLabel',score)
    

    



    








#main program
visuals(currentQuestion,currentOptionA,currentOptionB,currentOptionC,currentOptionD,currentAnswerIndex,dropAreaText,selected)
app.go()
TextFile.close()
