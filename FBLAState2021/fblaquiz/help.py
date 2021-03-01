#By Sujay Sundar
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import *
from PIL import Image, ImageTk

#Open Help menu screen in a new window, so user is able to refer to Help Contents as the user continues to use the FBLA Quiz application
def openhelp():
	#Creating the Help GUI window
	root = Tk()
	root.title("Help Contents")
	root.geometry("1300x700")
	root.images=[]

	#ScrolledText object to hold the Help contents
	help_text = ScrolledText(root,wrap=WORD,font=("Courier",12, "bold"),width=140,height=40)
	help_text.grid(column=0, columnspan=3)

	#Populating the Help contents into the ScrolledText widget
	help_text.insert(END, "FBLA Quiz:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot1 = PhotoImage(file='../img/Leaderboard.png',master=root)
	root.images.append(screenshot1)
	help_text.image_create(INSERT, image=screenshot1)
	help_text.image=screenshot1

	#Adding screenshots from the application for the Help screen
	screenshot11 = PhotoImage(file='../img/GetStudentScore.png',master=root)
	root.images.append(screenshot11)
	help_text.image_create(INSERT, image=screenshot11)
	help_text.image=screenshot11

	#Adding screenshots from the application for the Help screen
	screenshot9 = PhotoImage(file='../img/FBLAQuiz.png',master=root)
	root.images.append(screenshot9)
	help_text.image_create(INSERT, image=screenshot9)
	help_text.image=screenshot9

	help_text.insert(END, "\n\nAccess The Quiz\n\nTo access the quiz, go to File >> FBLA Quiz, select Student ID and answer all five questions. Click on the Submit Quiz button to submit the quiz and record your score. The application will shutdown in order to allow you to reaccess the application and get a different set of questions to answer.\n\nGet Student Score\n\nTo retrieve a student's quiz score, select the Student ID from the drop down and click on the Get Student Score button.\n\nLeaderboard\n\nTo get the quiz scores of all students (ordered by top score), click on the Leaderboard button.\n\n")
	help_text.insert(END, "Manage Students:\n\n")
	
	#Adding screenshots from the application for the Help screen
	screenshot2 = PhotoImage(file='../img/ManageStudents.png',master=root)
	root.images.append(screenshot2)
	help_text.image_create(END, image=screenshot2)
	help_text.image=screenshot2

	#Adding screenshots from the application for the Help screen
	screenshot10 = PhotoImage(file='../img/GetAllStudents.png',master=root)
	root.images.append(screenshot10)
	help_text.image_create(END, image=screenshot10)
	help_text.image=screenshot10

	help_text.insert(END, "\n\nAdd New Student\n\nTo add a new student, go to File >> Manage Students, enter Student ID, Student Name, Student Grade. Click on the Add Student button.\n\nUpdate Student\n\nTo update student information, go to File >> Manage Students and enter Student ID and Student Grade. Click on the Update Student button.\n\nGet All Student Records\n\nTo view all student records, go to File >> Manage Students and click on the Get All Student Records button.\n\n")
	
	help_text.insert(END, "Reports:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot4 = PhotoImage(file='../img/DownloadMenu.png',master=root)
	root.images.append(screenshot4)
	help_text.image_create(END, image=screenshot4)
	help_text.image=screenshot4

	#Adding screenshots from the application for the Help screen
	screenshot8 = PhotoImage(file='../img/ReportGenerated.png',master=root)
	root.images.append(screenshot8)
	help_text.image_create(END, image=screenshot8)
	help_text.image=screenshot8

	help_text.insert(END, "\n\nStudent Quiz Score Report\n\nTo generate a student's Quiz Score report, go to File >> FBLA Quiz, select Student ID and click on the Quiz Score Report button. A PDF version of the report will be downloaded.\n\nAll Students' Scores Report\n\nTo generate the Quiz Scores of all students, go to Download >> Download Report - All Student Scores. A PDF version of the report will be downloaded.\n\nGenerate Student Report\n\nTo generate a report of all student information, go to Download >> Download Report - All Students and a PDF version of the report will be downloaded.\n\nQuiz Question and Answers Report\n\nTo generate a report of all the FBLA Quiz questions and answers, go to Download >> Download Report - Quiz Question & Answers and a PDF version of the report will be downloaded.\n\n")

	help_text.insert(END, "Help:")

	help_text.insert(END, "\n\nApplication Help\n\nFor help on how to use this application, go to Help >> Help Contents\n\n")
	help_text.insert(END, "About the application:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot6 = PhotoImage(file='../img/About.png',master=root)
	root.images.append(screenshot6)
	help_text.image_create(END, image=screenshot6)
	help_text.image=screenshot6

	help_text.insert(END, "\n\nAbout\n\nTo know more about the application, go to Help >> About\n\n")
	help_text.insert(END, "Exit:\n\n")

	#Adding screenshots from the application for the Help screen
	screenshot7 = PhotoImage(file='../img/FileMenu.png',master=root)
	root.images.append(screenshot7)
	help_text.image_create(END, image=screenshot7)
	help_text.image=screenshot7

	help_text.insert(END, "\n\nTo exit the application, go to File >> Exit.\n\n")

	#Disabling the ScrolledText widget so user cannot modify content
	help_text.configure(state=DISABLED)

	#Exit button to quit from Help screen
	exit = Button(root, text="Exit Help", command=root.destroy)
	exit.grid(row=1,column=0)