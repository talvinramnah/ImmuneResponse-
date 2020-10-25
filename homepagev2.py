from appJar import gui
import sqlite3
import os

def gameFunc(score): 
    import mergerWithLoginv2
    

    

    
def registerFunc(self):
    from appJar import gui
    import sqlite3
    import random
    app = gui('register','500x500')
    app.setFont(20)

    #this allows the program to enter the information into this database
    connect = sqlite3.connect('leaderboardTest.db')
    cursor = connect.cursor()
    #this is here but only ran once as the first time i run it the table is made and won't be overwritten if ran again
    def create_table():
        cursor.execute("CREATE TABLE IF NOT EXISTS studentInformationTable4(StudentID INTEGER, Username TEXT, Password TEXT,Name TEXT, YearGroup INTEGER)")
    create_table()


    #this is the function(s) called when the info boxes are pressed, the render a help window that can be closed,
    #by pressing OK, the text displayed says the minimum requirments for the username/password
    def usernameInfoFunc(self):
        app.infoBox('usernameInfoBox', 'your username must be at least 8 characters long')
    def passwordInfoFunc(self):
        app.infoBox('passwordInfoBox','your password must have at least one capital letter and one number(s) and 8 character long and no more than 20 characters')


    #this function is called when the user wants to submit their information
    def validationChecker(self):
        loop = 0
        hashValue = 0
        #fetched entry in username textbox
        username = app.getEntry('username')
        #gets rando integer from 0-1000 to concatonate to end of username
        numericAddOn = random.randint(0,1000)
        #selects all usernames from database
        cursor.execute("SELECT Username FROM studentInformationTable4")
        #puts it in a list of tuples
        nonUniqueUsernameList = cursor.fetchall()
        print(nonUniqueUsernameList)
        #goes through each tuple in list
        for i in nonUniqueUsernameList:
            #checks if username in the list of tuples
            if username in i:
                #if yes concatonates random number
                username = username + str(numericAddOn)
                print(username)
            else:
                #checks if the username meets length requirment
                if len(username)>=8:
                    #highlights box in green is valid
                    app.setEntryValid('username')
                    #renders window saying accepted and gives the username that may have been changed
                    app.infoBox('acceptUsername', 'you username was accepted it is:'+username)
                    #if accepted the username is inserted into the database using the cursor
                    #this saves the data perisistently to the database
                    connect.commit()
                    #retrieves password entry and stores in a variable 
                    password = app.getEntry('password')
                    confirmedPassword = app.getEntry('confirm password')
                    #this is the verification check for the password
                    if password == confirmedPassword:
                        #highlights entry box green
                        app.setEntryValid('confirm password')
                        #length checking password for validation
                        if len(password)>=8:
                            #checking if there is a number in the password
                            #i cycles through numbers 1-9
                            for i in range (0,20):
                                #uses substring function to check if present in string
                                if password[i].isdigit and loop == 0:
                                    loop +=1
                                    #if all conditions met entry field highlighted in green
                                    app.setEntryValid('password')
                                    #notification pops up to say it was accepted
                                    app.infoBox('passwordAccepted','you password was accepted')
                                    #hashing the password
                                    for i in password:
                                        hashValue += ord(str(i))
                                        print(hashValue)
                                    #the password is saved to the database in SQL
                                    #name and year group entered in boxes are fetched and entered into database too
                                    name = app.getEntry('name')
                                    yearGroup = app.getOptionBox('yearGroup')
                                    cursor.execute("INSERT INTO studentInformationTable4(Username,Password,Name,YearGroup) VALUES (?,?,?,?)",(username,hashValue,name,yearGroup,))
                                    #.commit will make sure it's stored persistently
                                    connect.commit()
                            #checks to reject password, and infobox pops up with apporpirate errors
                        if len(password)<8:
                            app.infoBox('passwordDeclined','password needs to be 8 characters long')
                    if password != confirmedPassword:
                        app.infoBox('passwordDeclined2','your confirmed password did match')
                if len(username)<8:
                    app.setEntryInvalid('username')
                    app.infoBox('declineUsername','your username was not accepted, check information box on right')
                    app.clearEntry('username')
                    app.setFocus('username')
                        

            


            
    #this adds a title for the window
    app.addLabel('title','Sign Up Here!',0,0,2)
    app.setLabelBg('title','blue')
    #these are the different types of entry fields
    app.addValidationEntry('username',1,0)
    app.setEntryDefault('username','enter your username here')
    app.addValidationEntry('password', 2,0,True)
    app.setEntryDefault('password','enter your password here')
    app.addValidationEntry('confirm password',3,0,True)
    app.setEntryDefault('confirm password','confirm you password here')
    #these buttons are here for when the user needs to know requirments
    #when they are pressed the functions are called 
    app.addButton('password info',passwordInfoFunc,2,1)
    app.addButton('username info',usernameInfoFunc,1,1)
    app.addLabelEntry('name',4,0)
    app.setEntryMaxLength('password', 20)
    app.setEntryMaxLength('confirm password', 20)


    #this is a option entry field, it doesn't allow anything but given options
    #be entered and this increases robustness and data integrity
    app.addLabelOptionBox('yearGroup',['-KS4-','10','11','-KS5-','12','13'])
    #once the user submits information the validation checker is called,
    #if it deems the data entered to meet requirments it puts in the in the database
    app.addButton('submit user info',validationChecker)
    app.go()
    cursor.close()
    connect.close()
    
    
def questionEngineCall(self):
    import addQuestionv1
    os.system('addQuestionv1.py')

def loginFunc(self):
    import mergerWithLoginv2
##    import sqlite3
##    from appJar import gui
##
##
##    app = gui('login','500x500')
##    app.setFont(20)
##
##    connect = sqlite3.connect('leaderboardTest.db')
##    cursor = connect.cursor()
##
##
##    #this adds a title for the window
##    app.addLabel('title','Sign Up Here!',0,0,2)
##    app.setLabelBg('title','blue')
##
##    app.addValidationEntry('username',1,0)
##    app.setEntryDefault('username','enter your username here')
##    app.addValidationEntry('password', 2,0,True)
##    app.setEntryDefault('password','enter your password here')
##
##    cursor.execute("SELECT Username FROM studentInformationTable4")
##    usernameList = cursor.fetchall()
##    cursor.execute("SELECT Password FROM studentInformationTable4")
##    passwordList = cursor.fetchall()
##
##
##    def LoginChecker(self):
##        index = -1
##        hashValue = 0
##        username = app.getEntry('username')
##        password = app.getEntry('password')
##        for i in usernameList:
##            index +=1
##            if username in i:
##                print(index)
##                print(usernameList[index])
##                for everyLetter in password:
##                    hashValue += ord(str(everyLetter))
##                    print(hashValue)
##                    print(passwordList[index])
##                    passwordTuple = passwordList[index]
##                    print(passwordTuple[0])
##                    if int(hashValue)==  int(passwordTuple[0]):
##                        app.infoBox('huzzah','your username and password were correct, press OK to begin')
##                        app.setEntryValid('username')
##                        app.setEntryValid('password')
##                        app.addButton('press me to go to game',gameFunc,3,1)
##
##                        if int(hashValue)!= int(passwordTuple[0]):
##                            app.infoBox('error','your password did not match, try again')
##                if username not in i:
##                    app.infoBox('error','your username was not found, go back and register first!')
                
                        




##
##    app.addButton('press',LoginChecker,3,0)
##
##    app.go()
##
##    cursor.close()
##    connect.close()
def leaderboard(self):
    import leaderboardv2
    
app = gui('picture test','900x700')
app.setFont(30)
app.startLabelFrame("Simple", 0,0,4,3)
app.addImage("simple", "background2.png")
app.stopLabelFrame()
app.addButton('game',gameFunc,2,1)
app.addButton('tutorial',gameFunc,1,0)
app.addButton('leaderboard',leaderboard,2,2)
app.addButton('add a question',questionEngineCall,1,3)
app.addLabel('mess','welcome to immune response',0,1,2)
app.addLabel('label','choose an option',1,1,2)

app.addButton('login',loginFunc,0,0)
app.addButton('register',registerFunc,0,3)
app.setLabelBg('mess','green')
app.setLabelFg('mess','blue')
app.setLabelBg('label','green')
app.setLabelFg('label','blue')
app.setButtonBg('game','purple')
app.setButtonBg('tutorial','blue')
app.setButtonBg('leaderboard','orange')
app.setButtonBg('add a question','red')

app.go()
