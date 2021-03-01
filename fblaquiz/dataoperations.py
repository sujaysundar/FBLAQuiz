#By Sujay Sundar
import mysql.connector as mysql
from reportlab import *
import tkinter.messagebox as MessageBox #to display messages in the application indicating that actions on the db are successful

#Create functions to perform different data operations and execute the user stories/business requirements identified for the FBLA Quiz project

#Insert new student record into the database
def insertStudent(student_id,name,grade):
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")

		#Check to see all required fields are completed before inserting student into the db
		if(student_id=="" or name=="" or grade==""):
			MessageBox.showinfo("Insert student", "Please ensure all the mandatory fields are entered")
		else:
			#cursor to execute SQL query
			cursor=con.cursor()
			#insert Student id, Name and Grade in the db
			cursor.execute("insert into student values('"+student_id+"','"+name+"','"+grade+"')")
			#commit the student record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Insert student", "Student record entered successfully")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of insert student function")

#Delete student record from the database
def deleteStudent(student_id,student_name):
	#Check to see all required fields are completed before deleting student from the db
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")

		if(student_id==""):
			MessageBox.showinfo("Delete student", "Please ensure the Student ID field is entered")
		elif(len(student_id.strip())!=0 and (student_name.strip())==0):
			#cursor to execute SQL query
			cursor=con.cursor()
			#delete Student from the db
			cursor.execute("delete from student where student_id='"+student_id+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete student", "Student record deleted successfully")
		elif(len(student_id.strip())!=0 and (student_name.strip())!=0):
			#Create db connection using the mysql connector
			con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
			#cursor to execute SQL query
			cursor=con.cursor()
			#delete Student from the db
			cursor.execute("delete from student where student_id='"+student_id+"' and student_name='"+student_name+"'")
			#commit the delete in the db
			cursor.execute("commit");
			MessageBox.showinfo("Delete student", "Student record deleted successfully")

	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of delete student function")

#Update an existing student record
def updateStudent(student_id,name,grade):

	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		
		#Check to see all required fields are completed before inserting record into the db
		if(student_id==""):
			MessageBox.showinfo("Update student", "Please ensure the Student ID field is entered")
		else:
			#cursor to execute SQL query
			cursor=con.cursor()
			#Update student record in the db
			cursor.execute("Update student Set student_grade='"+str(grade)+"' Where student_id='"+student_id+"'")
			#commit the record in the db
			cursor.execute("commit");
			MessageBox.showinfo("Update student", "Student record updated successfully")
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of update student function")

#create function to get all Student IDs from the database to populate the combo box in the FBLA Quiz GUI
def getAllStudentIDs():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get Student ID from the db
		cursor.execute("select student_id from student")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records)

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get all student IDs function")

#create function to get all the students from the database
def getAllStudents():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get Students from the db
		cursor.execute("select * from student")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records)

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get students function")

#Create function to get one random quiz question from the database. This function will return a question that expects a text response from the user.
def getTextQuestion():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get question from the db
		cursor.execute("SELECT * from question where question_type='TEXT' order by rand() limit 1;")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records) 

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get question function")

#Create function to get one random quiz question from the database. This function will return a question that expects the user to select multiple correct answers from checkboxes.
def getMultipleChoiceQuestion():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get question from the db
		cursor.execute("SELECT * from question where question_type='MULTIPLE' order by rand() limit 1;")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records) 

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get question function")

#Create function to get one random quiz question from the database. This function will return a question that expects the user to select one correct response from radio buttons.
def getSingleChoiceQuestion():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get question from the db
		cursor.execute("SELECT * from question where question_type='SINGLE' order by rand() limit 1;")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records) 
		
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get question function")

#Create function to get one random quiz question from the database. This function will return a question that expects a boolean (True/False) response from radio buttons.
def getBinaryQuestion():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get question from the db
		cursor.execute("SELECT * from question where question_type='BINARY' order by rand() limit 1;")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records) 

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get question function")

#Create function to get one random quiz question from the database. This function will return a question that expects the user to select a response from a dropdown.
def getListQuestion():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get question from the db
		cursor.execute("SELECT * from question where question_type='LIST' order by rand() limit 1;")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records) 

		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get question function")

#This function returns the possible answers for a question from the database (except the question that expects a Text response from the user).
def getAnswerList(question_id):
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()
		#Get options from the db
		cursor.execute("select * from answer where question_id="+str(question_id)+";")
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records)
		
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get answer list function")

#Function to check the student's quiz answers before inserting score into the database
def checkStudentAnswers(student_id,question1,answer1,question2,answer2,question3,answer3,question4,answer4,question5,answer5):
	
	score=0 #Variable to hold the student's score
	correctanswers="" #Variable to hold the list of questions the student got correct

	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")

		#cursor to execute SQL query
		cursor=con.cursor()

		#Get the correct answers for the five questions from the database
		cursor.execute("select answer_text from answer where question_id='"+str(question1)+"' AND correct='Y';")
		records=cursor.fetchall()

		correctanswer1=[] #Variable to hold the correct answer for the first question
		if records:
			for record in records:
				#Debug statement to check results from the database inside the for loop
				#print (records)
				correctanswer1.append(record[0])

		if(answer1==correctanswer1[0]):
			correctanswers=correctanswers+"1" #Add 1 to the list of questions the user got correct
			score += 20 #Increment the score by 20 points for every correct answer

		cursor.execute("select answer_text from answer where question_id='"+str(question2)+"' AND correct='Y';")
		records=cursor.fetchall()

		correctanswer2=[] #Variable to hold the correct answer for the second question
		if records:
			for record in records:
				#Debug statement to check results from the database inside the for loop
				#print (records)
				correctanswer2.append(record[0])

		if(answer2==correctanswer2[0]):
			correctanswers=correctanswers+", 2" #Add 2 to the list of questions the user got correct
			score += 20 #Increment the score by 20 points for every correct answer

		cursor.execute("select answer_text from answer where question_id='"+str(question3)+"' AND correct='Y';")
		records=cursor.fetchall()

		correctanswer3="" #Variable to hold the correct answer for the third question
		if records:
			for record in records:
				#Debug statement to check results from the database inside the for loop
				#print (record)
				correctanswer3=correctanswer3+" "+record[0]
		
		if(answer3.strip()==correctanswer3.strip()):
			correctanswers=correctanswers+", 3" #Add 3 to the list of questions the user got correct
			score += 20 #Increment the score by 20 points for every correct answer

		cursor.execute("select answer_text from answer where question_id='"+str(question4)+"' AND correct='Y';")
		records=cursor.fetchall()

		correctanswer4=[] #Variable to hold the correct answer for the fourth question
		if records:
			for record in records:
				#Debug statement to check results from the database inside the for loop
				#print (records)
				correctanswer4.append(record[0])

		if(answer4==correctanswer4[0]):
			correctanswers=correctanswers+", 4" #Add 4 to the list of questions the user got correct
			score += 20 #Increment the score by 20 points for every correct answer

		cursor.execute("select answer_text from answer where question_id='"+str(question5)+"' AND correct='Y';")
		records=cursor.fetchall()

		correctanswer5=[] #Variable to hold the correct answer for the fifth question
		if records:
			for record in records:
				#Debug statement to check results from the database inside the for loop
				#print (records)
				correctanswer5.append(record[0])

		if(answer5==correctanswer5[0]):
			correctanswers=correctanswers+", 5" #Add 5 to the list of questions the user got correct
			score += 20 #Increment the score by 20 points for every correct answer

		#Call function to insert Student's score into the database
		insertStudentScore(student_id, score)

		#Display confirmation message to the user in the GUI
		if(score==0):
			MessageBox.showinfo("Submit Quiz","You got no answer correct. Your score is "+str(score))
		else:
			MessageBox.showinfo("Submit Quiz","You got question "+correctanswers+" correct. Your score is "+str(score))
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of check answers function")

#Function to insert student's quiz score into the database
def insertStudentScore(student_id,score):

	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")

		#cursor to execute SQL query
		cursor=con.cursor()

		#Query the database to see if the student had already given the quiz before
		cursor.execute("select student_id from Student_Score where student_id='"+str(student_id)+"';")
		records=cursor.fetchall()
		
		if records:
			#If student had already given the quiz before, update student record with the latest quiz score
			cursor.execute("Update Student_Score Set score='"+str(score)+"', quiz_date=NOW() Where student_id='"+student_id+"'")
		else:
			#If this is the first time student is taking the quiz, create a record for the student with the score
			cursor.execute("insert into Student_Score (student_id, score, quiz_date) values('"+student_id+"', '"+str(score)+"', NOW())")

		#commit the record in the db
		cursor.execute("commit");
		
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of insert record function")

#Function to get a single student's quiz score
def getStudentScore(student_id):
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")

		#Check to see if the Student Id is selected in the GUI before displaying the student's quiz score
		if(student_id==""):
			MessageBox.showinfo("Select Student ID", "Please select a Student ID to view Quiz score.")
		else:
			#cursor to execute SQL query
			cursor=con.cursor()
			#Get record from the db
			cursor.execute("select * from Student_Score where student_id="+str(student_id)+";")
			
			records=cursor.fetchall()
			
			#Print data retrieved from the database to test/debug
			#print (records)
		
			return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get student score function")

#Function to get all students quiz scores
def getAllStudentScore():
	try:
		#Create db connection using the mysql connector
		con=mysql.connect(host="localhost",user="root",password="@dm!n2020",database="FBLAQuiz")
		#cursor to execute SQL query
		cursor=con.cursor()

		#Get records from the db
		cursor.execute("select * from Student_Score Order By score;")
			
		records=cursor.fetchall()

		#Print data retrieved from the database to test/debug
		#print (records)
		
		return records
	except Exception as e:
		#print any exceptions encountered in executing above block of code
		print(e)
	finally:
		#Free up resources like open DB connections, etc.
		con.close();
		#print("End of get all student score function")