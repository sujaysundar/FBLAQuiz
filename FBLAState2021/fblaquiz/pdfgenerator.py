import mysql.connector as mysql
from reportlab.lib import colors, styles
from reportlab.lib.styles import (ParagraphStyle, getSampleStyleSheet)
from reportlab import *
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import letter
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful

def getAllScoresIntoPdf(): #Function to retrieve all student score records from the database into a pdf file
	try:
		pdf = SimpleDocTemplate('../reports/All Student Scores Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get all student score records from the db
		cursor.execute("select * from Student_Score")

		records=cursor.fetchall()
		data = [["Student ID","Quiz Score","Date of Quiz"]]
		for record in records:
			#Print data retrieved from the database to test/debug
			#print (record) 
			data.append(record) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1),12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get all scores function")

def getStudentScoreIntoPdf(student_id): #Function to retrieve a single student's quiz score from the database into a pdf file
	try:
		pdf = SimpleDocTemplate('../reports/Student Quiz Score Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		
		#Check to see if the Student Id is selected in the GUI before generating the report
		if(student_id==""):
			MessageBox.showinfo("Select Student ID", "Please select a Student ID to generate the report.")
		else:

			#cursor to execute SQL query
			cursor=con.cursor()
			#Get student score record from the db
			cursor.execute("select * from Student_Score where student_id='"+str(student_id)+"'")

			records=cursor.fetchall()
			data = [["Student ID","Quiz Score","Date of Quiz"]]
			for record in records:
				#Print data retrieved from the database to test/debug
				#print (record) 
				data.append(record) #Append the data from the db to the list object created for the pdf file
		
			table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

			#Apply some styling on the table that will be displayed in the pdf
			ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1), 12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
			table.setStyle(ts)
			data_obj=[]
			data_obj.append(table)
			pdf.build(data_obj)
			MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get student score function")

def getAllStudentsIntoPdf(): #Function to retrieve all student records from the database into a pdf file
	try:
		pdf = SimpleDocTemplate('../reports/All Students Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get all students from the db
		cursor.execute("select * from student")

		students=cursor.fetchall()
		data = [["Student ID","Name","Grade"]]
		for student in students:
			#Print data retrieved from the database to test/debug
			#print (student) 
			data.append(student) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=140, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1), 12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get all students function")

def getAllAnswersIntoPdf(): #Function to retrieve all quiz answers from the database into a pdf file
	try:
		pdf = SimpleDocTemplate('../reports/Quiz Question and Answers Report.pdf',pagesize=letter)
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get all quiz answers from the db
		cursor.execute("SELECT question.question_text AS Question,answer.answer_text AS Answer FROM question JOIN answer ON question.question_id=answer.question_Id WHERE answer.correct = 'Y';")

		records=cursor.fetchall()
		data = [["Question","Answer"]]
		for record in records:
			#Print data retrieved from the database to test/debug
			#print (record) 
			data.append(record) #Append the data from the db to the list object created for the pdf file
		
		table=Table(data, colWidths=280, rowHeights=30, repeatRows=1)

		#Apply some styling on the table that will be displayed in the pdf
		ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.lightskyblue),("BACKGROUND",(0,0),(3,0),colors.lightskyblue), ('FONTSIZE', (0, 0), (-1, -1),12),("BACKGROUND",(0,1),(-1,0),colors.whitesmoke)])
		table.setStyle(ts)
		data_obj=[]
		data_obj.append(table)
		pdf.build(data_obj)
		MessageBox.showinfo("Report", "PDF Report is generated and saved to your computer successfully!")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get all answers function")