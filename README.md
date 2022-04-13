# Essentials for Data Science Assignment (Group 4)
 <a href='https://github.com/hansq358/EfDS_assignment_DBSQL-4'><img src='Leiden.png' align="right" height="139" /></a>

## Authors
_Songqiao Han_ (s2889803), _Dun Dai_ (s2777607), _Chao Fu_ (s2918668), _Chentao Liu_ (s3083853), _Zijin Gu_ (s2797658), _Xintong Jiang_ (s2898144).<br/>
We hereby declare that all group members contributed equally to the assignment.<br/>
## Introduction
In this assignment, we aim to create a database using **[SQLAlchemy](https://www.sqlalchemy.org/)** and implement functions of adding, querying and summary in order to _**MAINTAIN**_ questions, answers, evaluations and grades. <br/>
**(1)** The first step is to create a [schema.pdf](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.pdf) to show all the requiring database relationships, then based on these relationships, there is a [schema.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.py) in the python to show the schema. <br/>
**(2)** The second step is about [gradedb.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/gradedb.py) which includes all the methods we want, including **addStudent()**, **addQuestion()**, **addTask()**, **addAssignment()**, **newSubmission()**, **addAnswer()**, **commitSubmission()**, **newEvaluation()**, **addScore()**, **commitEvaluation()**. These methods can help us to add students data to the database. <br/>
**(3)** Third, after building the database, we generate a [random_init.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/random_init.ipynb) file to generate random data and then add them into our created database.<br />
**(4)** At last, there are summaries for students themselves and for teachers. Files including: [student_summary.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/student_summary.ipynb), [student_detail.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/student_details.ipynb), [teacher_summary.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/teacher_summary.ipynb).<br/>

## Project Files
### Database content/access specification
- A github markdown file shortly describing the project (contributed by _Songqiao Han_, _Dun Dai_, _Zijin Gu_): [readme.md](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/README.md)
- A pure Python.py file containing definitions of the main project class **GradeDB** providing
access methods to the database (contibuted by _Dun Dai_, _Songqiao Han_, _Chentao Liu_): [gradedb.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/gradedb.py)
- A pdf displaying the schema of the database relationships. (contributed by all group members): [schema.pdf](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.pdf)
- A pure Python file with **[SQLAlchemy](https://www.sqlalchemy.org/)** description of the database tables (contributed by _Xintong Jiang_, _Chentao Liu_): [schema.py](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/schema.py)
- A notebook which initializes the database with some random generating content (contributed by _Chentao Liu_, _Dun Dai_, _Zijin Gu_, _Xintong Jiang_): [random_init.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/random_init.ipynb)

### Database summary tables
- A notebook shows a general summary to students which mainly including total grades for evaluated reports (contributed by _Songqiao Han_, _Chao Fu_): [student_summary.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/student_summary.ipynb)
- A notebook shows all details of students which mainly including scores for each evaluated question (contributed by _Songqiao Han_, _Chao Fu_): [student_details.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/student_details.ipynb)
- A notebook shows when grouped tasks, the totals numbers of: students assigned to the task, already submitted solutions, already evaluated solutions and pending for evaluation. (contributed by _Songqiao Han_, _Chao Fu_): [teacher_summary.ipynb](https://github.com/hansq358/EfDS_assignment_DBSQL-4/blob/main/teacher_summary.ipynb)

## Usage
### Packages 
- **os**
- **enum**
- **venv**
- **pandas**
- **numpy**
- **random**
- **email**
- **pickle**
- **tkinter**
- **sqlalchemy**
- **matplotlib**
