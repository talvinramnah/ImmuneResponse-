from appJar import gui
import sqlite3
import operator
app = gui('leaderboard','900x200')
connect = sqlite3.connect('leaderboardTest.db')
cursor = connect.cursor()
app.setFont('20')

app.startScrollPna('leaderboard')

#initial leaderboard
#firstly in alphabetical order
cursor.execute("SELECT Username,quizScore,GameHits,date FROM studentScores ORDER BY Username ASC")
#returns the list of tuples into thsi variable
leaderboardList = cursor.fetchall()
#thsi function will take all of the elements out of the tuples and put
#the item into a list with no tuples
gameScoreElements = list(map(operator.itemgetter(2), leaderboardList))
quizScoreElements = list(map(operator.itemgetter(1), leaderboardList))
usernameElements = list(map(operator.itemgetter(0), leaderboardList))
dateElements = list(map(operator.itemgetter(3),leaderboardList))
#gets length for FOR LOOP
length = len(gameScoreElements)

#title
app.addLabel('LEADA BOD','LEADERBOARD',0,1,4)
app.setLabelBg('LEADA BOD','blue')
#leaderboard headers
app.addLabel('usernameLabel','USERNAME',1,1)
app.addLabel('quizScoreLabel','QUIZ SCORE',1,2)
app.addLabel('gameHitsLabel','GAME SCORE',1,3)
app.addLabel('dateLabel','DATE',1,4)
app.setLabelBg('usernameLabel','black')
app.setLabelBg('quizScoreLabel','black')
app.setLabelBg('gameHitsLabel','black')
app.setLabelFg('gameHitsLabel','white')
app.setLabelFg('quizScoreLabel','white')
app.setLabelFg('usernameLabel','white')
#adding labels with the initial values
#goes through each item and adds a label below
#the one before for each field
for i in range (length):
    app.addLabel(i+1,gameScoreElements[i],i+2,3)
    app.addLabel(i+20,quizScoreElements[i],i+2,2)
    app.addLabel(i+100,usernameElements[i],i+2,1)
    app.addLabel(i+1000,dateElements[i],i+2,4)
#when the user wants to sort the list differently they press the button and
#an SQL statement returns the fields in that order
def orderByQuizASC(self):
    cursor.execute("SELECT Username,quizScore,GameHits,date FROM studentScores ORDER BY quizScore asc")
    leaderboardListQuizASC = cursor.fetchall()
    #these functions call the order function
    #they send in a new lsit fo tuples that's in teh specific order
    order(leaderboardListQuizASC)
#this is the function that will change the order of the LB, it takes a new list as argument
def order(leaderboardList):
    #it will do the same function for the initial list with new values
    gameScoreElements = list(map(operator.itemgetter(2), leaderboardList))
    quizScoreElements = list(map(operator.itemgetter(1), leaderboardList))
    usernameElements = list(map(operator.itemgetter(0), leaderboardList))
    dateElements = list(map(operator.itemgetter(3),leaderboardList))
    #this is the local variable for length, appJar doesn't let me send 2 args in
    length = len(gameScoreElements)
    #same FOR loop structure but new variables
    for i in range (length):
        str(gameScoreElements[i])
        app.setLabel(i+1,gameScoreElements[i])
        app.setLabel(i+20,quizScoreElements[i])
        app.setLabel(i+100,usernameElements[i])
        app.setLabel(i+1000,dateElements[i])
#all the orders they can choose
def orderByQuizDESC(self):
    cursor.execute("SELECT Username,quizScore,GameHits,date FROM studentScores ORDER BY quizScore desc")
    leaderboardListQuizdesc = cursor.fetchall()
    order(leaderboardListQuizdesc)
def orderByGameScoreASC(self):
    cursor.execute("SELECT Username,quizScore,GameHits,date FROM studentScores ORDER BY GameHits ASC")
    leaderboardListGameScore = cursor.fetchall()
    order(leaderboardListGameScore)
def orderByGameScoreDESC(self):
    cursor.execute("SELECT Username,quizScore,GameHits,date FROM studentScores ORDER BY GameHits DESC")
    leaderboardListGameScore = cursor.fetchall()
    order(leaderboardListGameScore)
#these are the buttons the user can choose to sort the LB in different orders
app.addButton('orderByquizScoreASC',orderByQuizASC,length+2,1)
app.addButton('orderbyquizScoreDESC',orderByQuizDESC,length+2,2)
app.addButton('orderByGameScoreASC',orderByGameScoreASC,length+3,1)
app.addButton('orderbyGameScoreDESC',orderByGameScoreDESC,length+3,2)
app.go()
