# FBLAQuiz
Sujay Sundar - NYS FBLA 2021

# NYS-FBLA-FBLAQuiz
**FBLA Quiz For Chapter Students**

**Prerequisites, setup and installation:**

*Windows 10 environment setup for python and installing Mysql connector, reportlab and other dependent packages/libraries:*

1) To install Python on a Windows computer, go to, https://www.python.org/downloads/windows/ and  download the latest stable release.
For Python 3.8.1, go to, https://www.python.org/downloads/release/python-381/ and select the 32 or 64 bit installer, whichever is applicable for your computer.
2) Download the installer and run it to install Python (follow the installation instructions and leave most defaults as-is). Please ensure you select the "Install launcher for all users" and "Add Python 3.8.1 to PATH" checkboxes and select "Install Now".
3) Select the "Disable PATH length limit" option.
4) To verify Python was installed successfully on a Windows machine, open the Start menu and type cmd to open the command prompt (command line). Type in python -v and it should display the version of Python installed.
5) If the Python version isn't displayed above, you can navigate to the folder where Python is installed (for example, Python381) in the command prompt for the same python command to function.
6) If the option to add Python to PATH wasn't available during install, do this manually by opening the Start menu and starting the run app. Type sysdm.cpl and click OK.
In the System Properties window, go to the Advanced tab and select Environment Variables. Under, System Variables, select the PATH variable and click Edit. In the Variable Value field, add the path to the python.exe file preceded with a semicolon (;). For example, C:\Python381
7) To verify if Pip is installed, open the Start menu and type in cmd to open the command prompt. Type in pip -V to view the display message indicating if pip was installed successfully along with the Python installation.
8) If pip isn’t already available, please download get-pip.py from  https://bootstrap.pypa.io/get-pip.py
Open a command prompt (type cmd from the Start menu on Windows) and navigate to the folder where get-pip.py was downloaded. Run the following command:
python get-pip.py

9) Now, run the command python -V to verify that pip was installed.

10) In order to connect to a MySQL database from a python program, please install/run the following:
pip install mysql-connector-python

11) To be able to create pdf reports, please install/run the following:
pip install reportlab

12) To be able to embed and add images into Python/Tkinter GUI, please install/run the following:
pip install PIL and 
pip install Pillow

13) To be able to create an executable (exe) from a python program, please install/run the following:
pip install pyinstaller

14) To download all source code for the FBLA Quiz application, please go to https://github.com/sujaysundar/FBLAQuiz and download the content to your computer under say, C:\FBLAState2021
The folder structure in your computer should resemble close to the following:

<img src="/img/WindowsExplorer.jpg" alt="Screenshot"/>
 
15) You can again verify if your python environment is correctly setup by running the following command after navigating to the “tests” folder in the cmd window:
python testenvironment.py
The following message should be displayed:
“Python environment is successfully setup”
 
*MySQL database (v8.0.19) installation and setup on Windows 10 computer:*

1) Download and install MySQL Community edition for Windows from,  https://dev.mysql.com/downloads/installer/ (You can skip logging in by clicking on “No thanks, just start my download.”). Choose the “Developer Default” option to install MySQL.
2) In the subsequent screens, please choose the default options, including, choose Standalone MySQL Server option, Strong password encryption for authentication. Choose the root password (say, @dm!n2020), add user (say, admin) and set user password (say, @dm!n2020).
Note: It is important to use these same usernames and passwords as the python program connects to the database using these values.
3) After installation and configuration, open the MySQL Workbench from the Start menu to access the MySQL GUI. Connect to the database “Mysql@localhost:3306”
4) Open a New Query Tab from the File menu and create a new schema by executing the following SQL command:
CREATE SCHEMA `fblaquiz`;
5) Go to File >> Run SQL Script and execute the DDL_CREATE.sql script located under the “data” folder. This will create all the tables required for the FBLA Quiz application.
6) Go to File >> Run SQL Script and execute the DML_UPDATE.sql script located under the “data” folder. This will load all the initial student and Quiz data for the FBLA Quiz application.
7) At any time, if you would like to clean up data and recreate the initial data setup, go to File >> Run SQL Script and execute the DDL_DELETE.sql script located under the “data” folder. This will delete all data from the tables. To drop the tables, Go to File >> Run SQL Script and execute the DDL_DROP.sql script located under the “data” folder.
8) After cleanup, to recreate the tables and reload the initial data, please run the DDL_CREATE.sql and DML_UPDATE.sql scripts again.

**Requirements:**

To enable an iterative/agile mode of development, the requirements were documented as the following user stories/epics:

1) As an admin user, I want to add a new student, so that the new student’s information is captured.
2) As an admin user, I want to update a student’s information, if a student is graduating from one grade to another.
3) As a user/student, I want to access the FBLA Quiz and submit answers to five randomly selected questions.
4) As a user/student, I want to know the correctly answered questions for my Quiz and my Quiz score (maximum score of 100).
5) As a user/admin, I want to view the Leaderboard (Quiz scores of all students, ordered by top score).
6) As a user/student, I want to view my Quiz score.
7) As a user/student, I want to download a report of my Quiz score so that it can be viewed and printed.
8) As an admin user, I want to view all chapter student data (Student ID, Name, Grade).
9) As a user/admin, I want to download a report of all students Quiz scores so that it can be viewed and printed.
10) As an admin user, I want to download a report of all chapter student data (Student ID, Name, Grade) so that it can be viewed and printed.
11) As an admin user, I want to generate a pdf report of all Quiz questions and Answers so that it can be viewed and printed.
12) As a user, I want to be able to view help content in a separate window, so that I can use it as a resource in case I need help using the application.
13) As a user, I want to be able to view information about the desktop application, so that I know the version of the application.
14) As a user, I want to cleanly exit the application.

**Design/Architecture:**

This application follows a standard 3-tier architecture where the front-end GUI is developed in Python/Tkinter, middle layer processing is via application logic written in Python and backend database is MySQL server.

**Few Considerations:**

1) ADA compliant - This application tries to follow the spirit of the Americans with Disabilities Act (ADA) Standards for Accessible Design. In particular, the colors  and font sizes chosen enable differently abled people to also use the application.

2) Modular development - Component based development where code is separated logically into it's own program files/modules like GUI, data/business logic, etc. This will also enable reusability of the components/code.

3) Iterative development - Agile mode of development with regular testing, debugging and feedback sessions.

4) Logging - Log critical program output into the console for debug and future reference.

5) Exception Handling - Exceptions in program execution are handled, particularly with respect to database operations, to trap unexpected errors.

6) Data privacy and Security - Personally identifiable information (PII) isn't captured or stored to the extent possible and data leaks are prevented by having strong password encryption on the MySQL database end. All versions of software/libraries used are the most recent and they generally contain security hotfixes, patches, etc. to address known issues.

7) Best practices - All best practices for software development lifecycle have been followed during design, development and testing.

8) Testing - Unit and Integration testing were performed to test the individual modules of the application integrated with the backend database. User testing was also performed with mock users.

9) Database Design - The relational database tables are normalized to avoid redundant data and integrity constraints like primary key are included.
 
**Using FBLA Quiz Desktop application:**

*To use the FBLA Quiz application, please follow any one of the following approaches:*

1) To launch the application from a command line interface - open the cmd window, navigate to the “fblaquiz” folder (say, cd C:\FBLAState2021\fblaquiz) and run the following command:
python fblaquiz.py
2) To launch the application using the exe provided - navigate to the “dist” folder and double click on oconsole.exe
Note: The exe was created by running the following command in the cmd window (after navigating to the folder above “fblaquiz” say, FBLAState2021):
pyinstaller -F -noconsole fblaquiz/fblaquiz.py

**Please review the below detailed  instructions on navigating through the FBLA Quiz application.**

*FBLA Quiz:*

<img src="/img/FBLAQuiz.png" alt="Screenshot"/>

Access The Quiz

To access the quiz, go to File >> FBLA Quiz, select Student ID and answer all five questions. Click on the Submit Quiz button to submit the quiz and record your score. The application will shutdown in order to allow you to reaccess the application and get a different set of questions to answer.

Get Student Score

To retrieve a student's quiz score, select the Student ID from the drop down and click on the Get Student Score button.

Leaderboard

To get the quiz scores of all students (ordered by top score), click on the Leaderboard button.

*Manage Students:*

<img src="/img/ManageStudents.png" alt="Screenshot"/>

Add New Student

To add a new student, go to File >> Manage Students and enter Student ID, Student Name, Student Grade. Click on the Add Student button.

Update Student

To update student information, go to File >> Manage Students and enter Student ID, Student Grade. Click on the Update Student button.

Get All Student Records

To view all student records, go to File >> Manage Students and click on the Get All Student Records button.

*Reports:*

<img src="/img/DownloadMenu.png" alt="Screenshot"/>
<img src="/img/ReportGenerated.png" alt="Screenshot"/>

Student Quiz Score Report

To generate a student's Quiz Score report, go to File >> FBLA Quiz, select Student ID and click on the Quiz Score Report button. A PDF version of the report will be downloaded.

Generate Student Report

To generate a report of all student information, go to Download >> Download Report - All Students and a PDF version of the report will be downloaded.

All Students' Scores Report

To generate the Quiz Scores of all students, go to Download >> Download Report - All Student Scores. A PDF version of the report will be downloaded.

Quiz Question and Answers Report

To generate a report of all the FBLA Quiz questions and answers, go to Download >> Download Report - Quiz Question & Answers and a PDF version of the report will be downloaded.

*Help:*

<img src="/img/Help.png" alt="Screenshot"/>

For help on how to use this application, go to Help >> Help Contents

*About:*

<img src="/img/About.png" alt="Screenshot"/>

To know more about the application, go to Help >> About

*Exit:*

<img src="/img/FileMenu.png" alt="Screenshot"/>

To exit the application, go to File >> Exit.

**Contributing to FBLA Quiz Application:**

Please reach out to me if you have any comments or feedback on this application.

**Contributors:**

Sujay Sundar (10th Grade)

Thanks to my advisers and testers for their feedback and encouragement.

**Contact:**

You can contact me at sujay.sundar@jerichoapps.org

**License:**

This project uses the following license: https://github.com/sujaysundar/NYS-FBLA-FBLAQuiz/blob/master/LICENSE
