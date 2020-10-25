from appJar import gui
app= gui('add a question','600x600')
TextFile =  open('mcq.txt','w')
#writing questions to textfile in the format of question on one line the next four lines
#have each option, the last line has the answer a total of 6 lines per question
TextFile.write('Question: Which of the following bonds are broken during DNA replication?\n')
TextFile.write('option A: Ionic bonds\n')
TextFile.write('option B: Hydrogen bonds\n')
TextFile.write('option C: covalent bonds \n')
TextFile.write('option D: phosphodiester bonds \n')
TextFile.write('option B hydrogen bonds \n')
TextFile.write('Question: Where does sucrose go from and to in a plant\n')
TextFile.write('option A: source to sink \n')
TextFile.write('option B: leaf to root \n')
TextFile.write('option C: root to leaf \n')
TextFile.write('option D: sink to source \n')
TextFile.write('option A source to sink \n')
TextFile.write('Question: What is the enzyme that allows carbonic acid to form \n')
TextFile.write('option A: amylase \n')
TextFile.write('option B: lactase \n')
TextFile.write('option C: carbonic anhydrase\n')
TextFile.write('option D: catalase\n')
TextFile.write('option C carbonic anhydrase \n')
TextFile.write('Question: what cell is responsible for manufacturing antibodies \n')
TextFile.write('option A: plasma cells \n')
TextFile.write('option B: T killer cells \n')
TextFile.write('option C: B lymphocytes \n')
TextFile.write('option D: opsonins \n')
TextFile.write('optionA plasma cells \n')
TextFile.write('Questions: what is the process of grouping pathogens together \n')
TextFile.write('option A: agglutination \n')
TextFile.write('option B: opsonination\n')
TextFile.write('optionC: anti toxination \n')
TextFile.write('option D: inhibition \n')
TextFile.write('option A agglutination \n')

TextFile.close()

questionsAdded = 0
#this opens the mcq file up in append mode so you can add text
TextFile = open('mcq.txt','a+')
#when the user entered text must be exported this function is called
def addingAQuestion(self):
    #these functions will fetch text from each box and return to variable
    question = app.getTextArea('questionTextArea')
    optionA = app.getTextArea('optionATextArea')
    optionB = app.getTextArea('optionBTextArea')
    optionC = app.getTextArea('optionCTextArea')
    optionD = app.getTextArea('optionDTextArea')
    answer = app.getTextArea('answerTextArea')
    answer = answer[7:]
    #these write the variables to the file on sepeate lines
    #this allows same formatting as pre-loaded questions
    TextFile.write(question+'\n')
    TextFile.write(optionA+'\n')
    TextFile.write(optionB+'\n')
    TextFile.write(optionC+'\n')
    TextFile.write(optionD+'\n')
    TextFile.write(answer+'\n')

    
    #these clear the text boxes so user can enter next question
    app.clearTextArea('questionTextArea', False)
    app.setTextArea('questionTextArea','question:')
    app.clearTextArea('optionATextArea', False)
    app.setTextArea('optionATextArea','option A:')
    app.clearTextArea('optionBTextArea', False)
    app.setTextArea('optionBTextArea','option B:')
    app.clearTextArea('optionCTextArea', False)
    app.setTextArea('optionCTextArea','option C:')
    app.clearTextArea('optionDTextArea', False)
    app.setTextArea('optionDTextArea','option D:')
    app.clearTextArea('answerTextArea', False)
    app.setTextArea('answerTextArea','answer:')
    



#when they press this button teh addingAQuestion function is called
app.addButton('add this question',addingAQuestion,0,5)



#these text areas are inserted empty
app.addLabel('questionLabel','write the question here',0,0)
app.addTextArea('questionTextArea',1,0,0)
app.addLabel('ALabel','write option A here',2,0)
app.addTextArea('optionATextArea',3,0)
app.addLabel('BLabel','write option B here',4,0)
app.addTextArea('optionBTextArea',5,0)
app.addLabel('CLabel','write option C here',6,0)
app.addTextArea('optionCTextArea',7,0)
app.addLabel('DLabel','write option D here',8,0)
app.addTextArea('optionDTextArea',9,0)
app.addLabel('answerLabel','write the answer here',10,0)
app.addTextArea('answerTextArea',11,0)




#the text entered in the boxes is in the same format as the preloaded MCQ's so
#can export it without any string manipulation making it more robust
app.setTextArea('questionTextArea', 'Question:')
app.setTextArea('optionATextArea','option A:')
app.setTextArea('optionBTextArea','option B:')
app.setTextArea('optionCTextArea','option C:')
app.setTextArea('optionDTextArea','option D:')
app.setTextArea('answerTextArea','answer:')









app.go()
TextFile.close()
