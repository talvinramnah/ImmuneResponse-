from appJar import gui
import sqlite3
import operator
app = gui('mini leaderboard','300x400')
connect = sqlite3.connect('leaderboardTest.db')
cursor = connect.cursor()
app.setFont('20')

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
def quit(self):
    app.stop()
app.addButton('quit',quit,6,0)
app.go()
cursor.close()
connect.close()
