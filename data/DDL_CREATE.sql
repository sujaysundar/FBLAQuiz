CREATE DATABASE FBLAQuiz;

CREATE TABLE Student (
  student_id INT(16) PRIMARY KEY,
  student_name VARCHAR(255) NOT NULL,
student_grade INT(16) NOT NULL
);
  
CREATE TABLE Question (
  question_id INT(16) PRIMARY KEY AUTO_INCREMENT,
  question_text TEXT NOT NULL,
  question_type VARCHAR(50) NOT NULL,
  question_score INT(6) NOT NULL DEFAULT 0
  );

CREATE TABLE Answer (
  answer_id INT(16) PRIMARY KEY AUTO_INCREMENT,
  question_Id INT(16) NOT NULL,
  answer_text TEXT NOT NULL,
  correct CHAR(1) 
  );
 
CREATE TABLE Student_Score (
  student_id INT(16) NOT NULL,
  score INT(16) NOT NULL,
  quiz_date datetime default now(),
Foreign Key (student_id) REFERENCES Student(student_id)
);