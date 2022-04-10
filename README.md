# Essentials for Data Science
 <a href='https://github.com/hansq358/EfDS_assignment_DBSQL-4'><img src='Leiden.png' align="right" height="139" /></a>

# Assignment: Group 4
Members: Songqiao Han (s2889803), Dun Dai (s2777607), Chao Fu (s2918668), Chentao Liu (s3083853), Zijin Gu (s2797658), Xintong Jiang (s2898144).

## Introduction
In this assignment, we will try to create a database and manage it through what we have learned in order to _MAINTAIN_ questions, answers, evaluations and grades. 
We will try to first create a [schema.pdf](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/Schema.pdf) to show all the database relationships, then based on these relationships, we will create a [schema.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.py) in the python. After that, we will create a [gradedb.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/gradedb.py) to show all the methods we want, including **addStudent()**, **addQuestion()**, **addTask()**, **addAssignment()**, **newSubmission()**, **addAnswer()**, **commitSubmission()**, **newEvaluation()**, **addScore()**, **commitEvaluation()**.

## Project Files
### Database content
- A github markdown file shortly describing the project: [readme.md](readme.md)
- A Python.py file containing definitions of the main project class GradeDB providing
access methods to the database: [gradedb.py](gradedb.py)
- A pdf displaying the schema of the database: [schema.pdf](schema.pdf)
- A text file with SQL code creating the database tables: [create.sql](create.sql)
- A  Python file with SQLAlchemy description of the database tables: [schema.py](schema.py)
- A notebook which initializes the database with some random content: [random_init.ipynb](random_init.ipynb)

### Database summary
- A report shows a general summary important to students: [student_summary.ipynb](student_summary.ipynb)
- A report shows all details of students from the database: [student_details.ipynb](student_details.ipynb)
- A report shows process of students' task:   [teacher_summary.ipynb](teacher_summary.ipynb)

