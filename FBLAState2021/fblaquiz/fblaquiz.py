#By Sujay Sundar
#Import the relevant packages/libraries to be used in the program for creating GUI, connecting to database, displaying messages to the user, etc.

from tkinter import *
import tkinter.messagebox as MessageBox #To display messages in the application (for example, indicating that actions on the database are successful)
from tkinter import ttk #For the dropdown/combo box menu
from dataoperations import * #Import functions from dataoperations.py to get and update records from/into the FBLA quiz database
from pdfgenerator import * #Import functions from pdfgenerator.py to get records from the FBLA quiz database and create PDF to view or print
from help import*
from about import*
import time

#Create the GUI

root = Tk() #create GUI window
root.geometry('1300x500') #Set the dimensions height/width of the GUI window (root)
root.title("FBLA Quiz") #Set the title of the GUI window (root)
root.configure(background="light blue")
root.resizable(0,0) #Disable the maximize window option to prevent distortion of GUI

fbla_quiz_frame=Frame(root,relief='raised', borderwidth=5) #Defining the frame within the parent GUI window for FBLA Quiz screen
student_record_frame=Frame(root,relief='raised', borderwidth=5) #Defining the frame within the parent GUI window for Student Record screen

def loadStudentPage():
	#Ensure the other pages/frames are closed/hidden and only the Student page is displayed
	fbla_quiz_frame.grid_forget()

	#Student page is displayed
	student_record_frame.grid(row=0,column=0,padx=280,pady=20)

def loadFBLAQuizPage():
	#Ensure the other pages/frames are closed/hidden and only the FBLA Quiz page is displayed
	student_record_frame.grid_forget()

	#FBLA Quiz page is displayed
	fbla_quiz_frame.grid(row=0,column=0,padx=50,pady=20)

#Get a Student's Quiz score to display in the Treeview (TV) object on the GUI
def getStudentScoreForTV(student_id):
	#Debug statement to check if student id is received in this function
	#print("Student ID is: "+student_id)

	#Clear the contents of the Treeview object before populating it with the result from the database
	for i in fbla_quiz_tree.get_children():
		fbla_quiz_tree.delete(i)

	results=getStudentScore(student_id)
	
	#Debug statement to check results from the database
	#print (results)

	if results:
		for record in results:
			#Insert record (student's score) retrieved from the db to display in the Treeview
			fbla_quiz_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Get All Student Scores (Leaderboard) to display in the Treeview (TV) object on the GUI
def getAllStudentScoreForTV():
	
	#Clear the contents of the Treeview object before populating it with the result from the db
	for i in fbla_quiz_tree.get_children():
		fbla_quiz_tree.delete(i)

	results=getAllStudentScore()
	
	#Debug statement to check results from the database
	#print (results)
	if results:
		for record in results:
			#Insert records (all students scores) retrieved from the db to display in the Treeview
			fbla_quiz_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Get All Students to display in the Treeview (TV) object on the GUI
def getAllStudentsForTV():
	
	for i in student_record_tree.get_children():
		student_record_tree.delete(i)

	results=getAllStudents()
	
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			student_record_tree.insert('',0,text=record[0],values=(record[1],record[2]))

#Populate the Student dropdown in the GUI to allow user to select Student ID
def getAllStudentIDsInCB():
	results=getAllStudentIDs()
	
	students=[]
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			students.append(record[0])
	return students

#Get possible answers for a question (Not applicable for questions that expect a text response from the user)
def getAnswerChoices(question_id):
	results=getAnswerList(question_id)
	listoptions=[]
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			listoptions.append(record[2])
	return listoptions

#Get a question that expects a text response and present it on the GUI as a label
def getTextQuestionForLabel():
	results=getTextQuestion()
	
	#Debug statement to check results from the database
	#print (results)
	#Array to hold the question id and question text
	question=[]

	if results:
		for record in results:
			question.append(record[0])
			question.append(record[1])
	return question

#Get a question that expects the user to select response from a dropdown and present it on the GUI as a label
def getListQuestionForLabel():
	results=getListQuestion()

	#Array to hold the question id and question text
	question=[]
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			question.append(record[0])
			question.append(record[1])
	return question

#Get a question that expects the user to select multiple responses from checkboxes and present it on the GUI as a label
def getMultipleChoiceQuestionForLabel():
	results=getMultipleChoiceQuestion()
	
	#Array to hold the question id and question text
	question=[]
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			question.append(record[0])
			question.append(record[1])
	return question

#Get a question that expects the user to select a binary response from radioboxes and present it on the GUI as a label
def getBinaryQuestionForLabel():
	results=getBinaryQuestion()
	
	#Array to hold the question id and question text
	question=[]
	if results:
		for record in results:
			#Debug statement to check results from the database inside the for loop
			#print (results)
			question.append(record[0])
			question.append(record[1])
	return question

#Get a question that expects the user to select a single response from radioboxes and present it on the GUI as a label
def getSingleChoiceQuestionForLabel():
	results=getSingleChoiceQuestion()
	
	#Debug statement to check results from the database
	#print (results)
	#Array to hold the question id and question text
	question=[]
	if results:
		for record in results:
			question.append(record[0])
			question.append(record[1])
	return question

#Function to validate user entered data, add/concatenate user selected checkbox values and then submit the user's quiz response to check answers against the db and insert quiz score into db.
def addCheckboxValuesAndSubmit():
	#Perform field validation to ensure all mandatory fields are entered by the user. Also check that the text response doesn't contain any special characters and all extra spaces are removed.
	#Remove any extra spaces in the user's text response to question 1 using answer1.get().strip()
	if(sid.get()=="" or answer1=="" or answer1.get().strip()=="" or answer2.get()=="" or selectedanswer4.get()=="" or selectedanswer5.get()==""):
		MessageBox.showinfo("Submit Quiz Answers", "Please ensure your Student ID is selected and all Quiz questions are answered.")
	elif (checkbox1.get()=="False" and checkbox2.get()=="False" and checkbox3.get()=="False" and checkbox4.get()=="False"):
		MessageBox.showinfo("Submit Quiz Answers", "Please ensure all Quiz questions are answered.")
	elif (not answer1.get().strip().isalnum()):
		MessageBox.showinfo("Submit Quiz Answers", "Please remove any special characters like [@_!#$%^&*()<>?/\|}{~:]' and extra spaces from your response.")
	else:
		#Capture the user selections for Answer 3 (in checkboxes) into a variable. Concatenate the checkbox values into a variable.
		checkedanswers=""

		if(checkbox1.get()==True):
			checkedanswers=str(answer3[0])
		if(checkbox2.get()==True):
			checkedanswers=checkedanswers+" "+str(answer3[1])
		if(checkbox3.get()==True):
			checkedanswers=checkedanswers+" "+str(answer3[2])
		if(checkbox4.get()==True):
			checkedanswers=checkedanswers+" "+str(answer3[3])

		#Call the function to check the student answers and then submit score to the db
		checkStudentAnswers(sid.get(),text_questions[0],answer1.get(),list_questions[0],answer2.get(),checkbox_questions[0],checkedanswers,binary_questions[0], selectedanswer4.get(), radiobutton_questions[0], selectedanswer5.get())

		#Close the application after submitting the quiz to allow user to reload the application and get a new screen with a different set of quiz questions to answer.
		root.destroy()

#FBLA Quiz Screen GUI starts here

#Main title of the screen
id = Label(fbla_quiz_frame,justify=LEFT,text='FBLA Quiz',font=('bold',20))
id.grid(row=0,column=1) #positioning the label accordingly in the GUI

#Creating labels for the form fields. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the application.

#Label for Student ID
id = Label(fbla_quiz_frame,justify=LEFT,text='Student ID',font=('bold',12))
id.grid(row=1,column=0) #positioning the label accordingly in the GUI

#Label/Text for Question 1
text_questions=getTextQuestionForLabel()
question1=Label(fbla_quiz_frame,justify=LEFT,text=text_questions[1],font=('bold',12))
question1.grid(row=2,column=0) #positioning the label accordingly in the GUI by setting margins

#Label/Text for Question 2
list_questions=getListQuestionForLabel()
question2=Label(fbla_quiz_frame,justify=LEFT,text=list_questions[1],font=('bold',12))
question2.grid(row=3,column=0) #positioning the label accordingly in the GUI

#Label/Text for Question 3
checkbox_questions=getMultipleChoiceQuestionForLabel()
question3=Label(fbla_quiz_frame,justify=LEFT,text=checkbox_questions[1],font=('bold',12))
question3.grid(row=4,column=0) #positioning the label accordingly in the GUI

#Label/Text for Question 4
binary_questions=getBinaryQuestionForLabel()
question4=Label(fbla_quiz_frame,justify=LEFT,text=binary_questions[1],font=('bold',12))
question4.grid(row=5,column=0) #positioning the label accordingly in the GUI

#Label/Text for Question 5
radiobutton_questions=getSingleChoiceQuestionForLabel()
question5=Label(fbla_quiz_frame,justify=LEFT,text=radiobutton_questions[1],font=('bold',12))
question5.grid(row=6,column=0) #positioning the label accordingly in the GUI

#Dropdown box for list of Students, the user can select their Student ID so the quiz is recorded in their name.
sid=StringVar()
sid=ttk.Combobox(fbla_quiz_frame,justify=LEFT,textvariable=sid,width=17)
sid['values']=getAllStudentIDsInCB() #Get all the Student IDs into the combo box/drop down
sid.grid(row=1,column=1)

#Creating text box for user to enter answer for question 1
answer1=StringVar()
answer1=Entry(fbla_quiz_frame,justify=LEFT,textvariable=answer1)
answer1.grid(row=2,column=1)

#Prompt message label to inform user about acceptable data form for the text response field
promptmessage = Label(fbla_quiz_frame,justify=LEFT,text='(Please use numbers for numerical values and avoid using any special characters or extra spaces.)',font=('bold',10))
promptmessage.grid(row=2,column=2,columnspan=10) #positioning the label accordingly in the GUI

#Dropdown box for user to select answer for question 2
answer2=StringVar()
answer2=ttk.Combobox(fbla_quiz_frame,justify=LEFT,textvariable=answer2,width=50)
answer2['values']=getAnswerChoices(list_questions[0]) #Get all options into the combo box/drop down
answer2.grid(row=3,column=1,columnspan=3)

#Creating checkboxes for user to select options for question 3
checkbox1=BooleanVar()
checkbox2=BooleanVar()
checkbox3=BooleanVar()
checkbox4=BooleanVar()
answer3=getAnswerChoices(checkbox_questions[0])

ttk.Checkbutton(fbla_quiz_frame, text=answer3[0], variable=checkbox1).grid(row=4,column=1)
ttk.Checkbutton(fbla_quiz_frame, text=answer3[1], variable=checkbox2).grid(row=4,column=2)
ttk.Checkbutton(fbla_quiz_frame, text=answer3[2], variable=checkbox3).grid(row=4,column=3)
ttk.Checkbutton(fbla_quiz_frame, text=answer3[3], variable=checkbox4).grid(row=4,column=4)

#Creating radio buttons for user to select for question 4
selectedanswer4=StringVar()
answer4=getAnswerChoices(binary_questions[0])
ttk.Radiobutton(fbla_quiz_frame,text=answer4[0], variable=selectedanswer4, value=answer4[0]).grid(row=5,column=1)
ttk.Radiobutton(fbla_quiz_frame,text=answer4[1], variable=selectedanswer4, value=answer4[1]).grid(row=5,column=2)

#Creating radio buttons for user to select for question 5
selectedanswer5=StringVar()
answer5=getAnswerChoices(radiobutton_questions[0])
ttk.Radiobutton(fbla_quiz_frame,text=answer5[0], variable=selectedanswer5, value=answer5[0]).grid(row=6,column=1)
ttk.Radiobutton(fbla_quiz_frame,text=answer5[1], variable=selectedanswer5, value=answer5[1]).grid(row=6,column=2)
ttk.Radiobutton(fbla_quiz_frame,text=answer5[2], variable=selectedanswer5, value=answer5[2]).grid(row=6,column=3)
ttk.Radiobutton(fbla_quiz_frame,text=answer5[3], variable=selectedanswer5, value=answer5[3]).grid(row=6,column=4)

#Create button to submit quiz responses and insert results/score into the db
insertbutton=Button(fbla_quiz_frame,text="Submit Quiz",font=("bold",12),bg="white",command=lambda:addCheckboxValuesAndSubmit())
insertbutton.grid(row=7,column=0)

#Create button to fetch single record (single student's score) from the db
get=Button(fbla_quiz_frame,text="Get Student Score",font=("bold",12),bg="white",command=lambda:getStudentScoreForTV(sid.get()))
get.grid(row=7,column=1)

#Create button to fetch all student scores
get_all_student_records=Button(fbla_quiz_frame,text="Leaderboard",font=("bold",12),bg="white",command=lambda:getAllStudentScoreForTV())
get_all_student_records.grid(row=7,column=2)

#Create button to view/download student's score report
get_all_student_records=Button(fbla_quiz_frame,text="Quiz Score Report",font=("bold",12),bg="white",command=lambda:getStudentScoreIntoPdf(sid.get()))
get_all_student_records.grid(row=7,column=3)

#Create Treeview to display a student's score when the get student score button is clicked
fbla_quiz_tree=ttk.Treeview(fbla_quiz_frame,columns=("QuizScore","QuizDate"))

#Set a vertical scroll bar so user can scroll the results to see all students' quiz scores in the tree view
sb = ttk.Scrollbar(root, orient="vertical", command=fbla_quiz_tree.yview)
fbla_quiz_tree.configure(yscrollcommand=sb.set)
fbla_quiz_tree.grid(column=0, row=0, sticky='nsew')
sb.grid(column=1, row=0, sticky='ns')

fbla_quiz_tree.grid(row=8,column=0,columnspan=10)
fbla_quiz_tree.heading('#0', text='Student ID')
fbla_quiz_tree.heading("QuizScore", text='Quiz Score')
fbla_quiz_tree.heading("QuizDate", text='Quiz Date')

#FBLA Quiz GUI Screen ends here

#Student Record GUI Screen starts here

#Main title of the screen
id = Label(student_record_frame,text='Manage Students',font=('bold',20))
id.grid(row=0,column=1) #positioning the label accordingly in the GUI	

#Creating labels for the form fields. The labels are created in compliance with ADA standards ensuring differently enabled users are able to use the application.

id = Label(student_record_frame,text='Student ID',font=('bold',12))
id.grid(row=1,column=0) #positioning the label accordingly in the GUI 

name=Label(student_record_frame,text='Student Name',font=('bold',12))
name.grid(row=2,column=0) #positioning the label accordingly in the GUI 

grade=Label(student_record_frame,text='Student Grade',font=('bold',12))
grade.grid(row=3,column=0) #positioning the label accordingly in the GUI 

#Creating text boxes for user to enter data
e_id=Entry(student_record_frame)
e_id.grid(row=1,column=1) #positioning the text box accordingly in the GUI 

#Creating text boxes for user to enter data
e_name=Entry(student_record_frame)
e_name.grid(row=2,column=1)

#Creating radio buttons for user to enter student grade
e_grade=StringVar(value="9"); #Setting a variable to hold the selected radio button value, defaulted to Grade 9
e_grade9=Radiobutton(student_record_frame,text="9", variable=e_grade, value="9")
e_grade10=Radiobutton(student_record_frame,text="10", variable=e_grade, value="10")
e_grade11=Radiobutton(student_record_frame,text="11", variable=e_grade, value="11")
e_grade12=Radiobutton(student_record_frame,text="12", variable=e_grade, value="12")

#Display the radio buttons one below the other
e_grade9.grid(row=3,column=1)
e_grade10.grid(row=4,column=1)
e_grade11.grid(row=5,column=1)
e_grade12.grid(row=6,column=1)

#Create button to insert student information into the db
insertbutton=Button(student_record_frame,text="Add Student",font=("bold",12),bg="white",command=lambda:insertStudent(e_id.get(),e_name.get(),e_grade.get()))
insertbutton.grid(row=7,column=0)

#Create button to update student information in the db
updatebutton=Button(student_record_frame,text="Update Student",font=("bold",12),bg="white",command=lambda:updateStudent(e_id.get(),e_name.get(),e_grade.get()))
updatebutton.grid(row=7,column=1)

#Create button to delete student record from the db. This button is temporarily disabled to prevent students from being deleted and losing their past quiz data.
#deletebutton=Button(student_record_frame,text="Delete Student",font=("bold",12),bg="white",command=lambda:deleteStudent(e_id.get(),e_name.get()))
#deletebutton.grid(row=7,column=2)

#Create button to fetch student records from the db
get=Button(student_record_frame,text="Get All Student Records",font=("bold",12),bg="white",command=lambda:getAllStudentsForTV())
get.grid(row=7,column=2)

#Create Treeview to display all student records when the get students button is clicked
student_record_tree=ttk.Treeview(student_record_frame,columns=("StudentName", "Grade"),height=6)

#Set a vertical scroll bar so user can scroll the results to see all student records in the tree view
s_sb = ttk.Scrollbar(root, orient="vertical", command=student_record_tree.yview)
student_record_tree.configure(yscrollcommand=s_sb.set)
student_record_tree.grid(column=0, row=0, sticky='nsew')
s_sb.grid(column=1, row=0, sticky='ns')

student_record_tree.grid(row=8,column=0,columnspan=3)
student_record_tree.heading('#0', text='Student ID')
student_record_tree.heading("StudentName", text='Student Name')
student_record_tree.heading("Grade", text='Grade')

#Student Record GUI Screen ends here

root.option_add('*tearOff', FALSE) #Remove the Tear line that appears in the Menu

#Create Menu for the GUI window 'root'
menu=Menu(root)
root.config(menu=menu)

#File menu
file=Menu(menu)
file.add_command(label='FBLA Quiz',command=lambda:loadFBLAQuizPage())
file.add_command(label='Manage Students',command=lambda:loadStudentPage())
file.add_command(label='Exit',command=root.destroy) #We can also use root.exit() command
menu.add_cascade(label='File',menu=file)

#Download menu
download=Menu(menu)
download.add_command(label='Download Report - All Student Scores',command=lambda:getAllScoresIntoPdf())
download.add_command(label='Download Report - All Students',command=lambda:getAllStudentsIntoPdf())
download.add_command(label='Download Report - Quiz Question & Answers',command=lambda:getAllAnswersIntoPdf())
menu.add_cascade(label='Download',menu=download)

#Help menu
help=Menu(menu)
help.add_command(label='Help Contents',command=lambda:openhelp())
help.add_command(label='About',command=lambda:openabout())
menu.add_cascade(label='Help',menu=help)

#Initialize the application and load the FBLA Quiz page on startup
loadFBLAQuizPage()

#Call the function to load the Student IDs in the drop down
getAllStudentIDsInCB()

#Run/activate the mainloop event
root.mainloop()