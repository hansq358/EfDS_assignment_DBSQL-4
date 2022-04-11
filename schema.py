from email.policy import default
from enum import unique
from pickle import FALSE
from tkinter import CASCADE
from venv import create
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData,Table,ForeignKeyConstraint
from sqlalchemy.orm import relationship, declarative_base, sessionmaker,Session
import sqlalchemy
from gradedb import *
import os

adress='create.db'
if(os.path.isfile(adress)): 
      os.remove(adress)
engine = create_engine('sqlite:///'+adress,echo=False)

Base = declarative_base() # normally present once in a script!

class Students(Base):
  __tablename__ = "Students"
  
  Universityid = Column(String(8),primary_key=True)
  Name = Column(String(50),nullable=FALSE)
  Email = Column(String(50),nullable=True,unique=True)
  Assignment = relationship("Assignment",backref="Students", cascade="all, delete",passive_deletes=True)               # <<<< HERE
  #sqlalchemy.Constraint('len(Universityid)==8')
  def __repr__(self):
    return "Students(Universityid='%s', Name='%s', Email='%s')" % (self.Universityid, self.Name, self.Email)


Question_Task=Table("Question_Task", Base.metadata,
  Column('Questionid',ForeignKey('Question.Questionid'), primary_key=True),
  Column('Taskid',ForeignKey('Task.Taskid'), primary_key=True)
  )#AlbumId = Column(ForeignKey('albums.AlbumId'), nullable=True) # <<<< HERE
class Task(Base):
  __tablename__ = "Task"
  
  Taskid = Column(Integer,primary_key=True, autoincrement=True)
  Title= Column(String(60),nullable=FALSE)
  Text = Column(String(300),nullable=FALSE)
  Assignment = relationship("Assignment", backref="Task", cascade="all, delete",passive_deletes=True)               # <<<< HERE
  Question = relationship("Question", secondary=Question_Task, back_populates='Task',cascade="all,delete")   
  def __repr__(self):
    return "Students(Taskid='%s', Title='%s', Text='%s')" % (self.Taskid, self.Title, self.Text)

class Question(Base):
  __tablename__ = "Question"
  
  Questionid = Column(Integer,primary_key=True, autoincrement=True)
  Title= Column(String(60),nullable=FALSE)
  Text = Column(String(300),nullable=FALSE)
  Answer = relationship("Answer", backref="Question",cascade="all, delete",passive_deletes=True) 
  Task = relationship("Task", secondary=Question_Task,back_populates='Question', cascade="all,delete")              # <<<< HERE

  def __repr__(self):
    return "Question(Questionid='%s', Title='%s', Text='%s')" % (self.Questionid, self.Title, self.Text)

class Assignment(Base):
  __tablename__ = "Assignment"
  #__table_args__ = (
  # this can be db.PrimaryKeyConstraint if you want it to be a primary key
  #sqlalchemy.UniqueConstraint('Universityid', 'Taskid'),
  #)
  sqlalchemy.UniqueConstraint('Universityid', 'Taskid')
  Universityid = Column(Integer,ForeignKey('Students.Universityid', ondelete="CASCADE"))
  Taskid = Column(Integer,ForeignKey('Task.Taskid', ondelete="CASCADE"))
  #AlbumId = Column(ForeignKey('albums.AlbumId'), nullable=True) # <<<< HERE
  Assignmentid=Column(Integer,primary_key=True,nullable=FALSE, autoincrement=True)
  Submission = relationship("Submission", backref="Assignment",cascade="all, delete",passive_deletes=True)


  def __repr__(self):
    return "Assignment(Universityid='%s', Taskid='%s',Assignmentid='%s')" % (self.Universityid, self.Taskid,self.Assignmentid)

class Submission(Base):
  __tablename__ = "Submission"
  
  Submissionid = Column(Integer,primary_key=True, autoincrement=True)
  #Universityid = Column(Integer,nullable=FALSE)
  #Taskid = Column(Integer,nullable=FALSE)
  Time= Column(sqlalchemy.DateTime,nullable=FALSE)
  Evaluation = Column(String(300),nullable=True)
  Evaluation_request = Column(sqlalchemy.types.Boolean,default=False)
  Evaluation_finished = Column(sqlalchemy.types.Boolean,default=False)
  #Assignment = relationship("Assignment", backref="Students")               # <<<< HERE
  #sqlalchemy.ForeignKeyConstraint(['Taskid', 'Universityid'], ['Assignment.Taskid', 'Assignment.Universityid'])
  Assignmentid=Column(Integer,ForeignKey('Assignment.Assignmentid',ondelete=CASCADE),unique=True,nullable=FALSE)
  Answer = relationship("Answer", backref="Submission",cascade="all, delete",passive_deletes=True)   
  Score= relationship("Score", backref="Submission",cascade="all, delete",passive_deletes=True) 
  def __repr__(self):
    return "Submission(Submissionid='%s', Assignmentid='%s',Time='%s', Evaluation='%s',  Evaluation_request='%s',Evaluation_finished='%s')" % (self.Submissionid, self.Assignmentid,self.Time, self.Evaluation,  self.Evaluation_request,self.Evaluation_finished)

class Answer(Base):
  __tablename__ = "Answer"
  
  Answerid = Column(Integer,primary_key=True, autoincrement=True)
  Questionid = Column(ForeignKey('Question.Questionid',ondelete=CASCADE),nullable=FALSE)
  Submissionid = Column(ForeignKey('Submission.Submissionid',ondelete=CASCADE),nullable=True)
  Text = Column(String(300),nullable=FALSE)
  Score= relationship("Score", backref="Answer",cascade="all, delete",passive_deletes=True) 
  def __repr__(self):
    return "Answer(Questionid= '%s', Answerid='%s', Submissionid='%s',Text='%s')" % (self.Questionid, self.Answerid, self.Submissionid,self.Text,self.Text)

class Score(Base):
  __tablename__ = "Score"
  
  Scoreid = Column(Integer,primary_key=True, autoincrement=True)
  Answerid = Column(ForeignKey('Answer.Answerid',ondelete=CASCADE),nullable=FALSE)
  Submissionid = Column(ForeignKey('Submission.Submissionid',ondelete=CASCADE),nullable=FALSE)
  Value = Column(sqlalchemy.types.DECIMAL(3,1),nullable=FALSE)
  Time= Column(sqlalchemy.DateTime,nullable=FALSE)
  #Answer= relationship("Answer", backref="Score")
  #Assignment = relationship("Assignment", backref="Students")               # <<<< HERE

  def __repr__(self):
    return "Score(Scoreid= '%s', Answerid='%s', Submissionid='%s',Value='%s',Time='%s')" % (self.Scoreid, self.Answerid, self.Submissionid,self.Value,self.Time)
sqlalchemy.CheckConstraint(Score.Value>=0)
sqlalchemy.CheckConstraint(Score.Value<=10)
Base.metadata.create_all(engine)