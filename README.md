# Essentials for Data Science
 <a href='https://github.com/hansq358/EfDS_assignment_DBSQL-4'><img src='Leiden.png' align="right" height="139" /></a>

# Assignment: Group 4
Members: Songqiao Han (s2889803), Dun Dai (s2777607), Chao Fu (s2918668), Chentao Liu (s3083853), Zijin Gu (s2797658), Xintong Jiang (s2898144).

## Introduction
In this assignment, we try to create a database and manage it through what we have learned in order to _**MAINTAIN**_ questions, answers, evaluations and grades. <br />
**(1)** The first step is to create a [schema.pdf](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/Schema.pdf) to show all the requiring database relationships, then based on these relationships, there is a [schema.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.py) in the python to show the schema. <br />
**(2)** The second step is about [gradedb.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/gradedb.py) which includes all the methods we want, including **addStudent()**, **addQuestion()**, **addTask()**, **addAssignment()**, **newSubmission()**, **addAnswer()**, **commitSubmission()**, **newEvaluation()**, **addScore()**, **commitEvaluation()**. These methods can help us to add students data to the database. <br />
**(3)** Third, after building the database, we generate a [random_init.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/random_init.ipynb) file to generate random data and then add them into our created database.<br />
**(4)** At last, there are summaries for students themselves and for teachers. Files including: [student_summary.ipynb](), [student_detail.ipynb](), [teacher_summary.ipynb]().<br />

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

