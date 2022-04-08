from collections import UserList
from datetime import datetime
import decimal

from sqlalchemy import *
from sqlalchemy.orm import relationship, declarative_base, sessionmaker,Session

engine = create_engine('sqlite:///create_2.db')
Base = declarative_base() # normally present once in a script!

associate_assignment = Table('associate_assignment', Base.metadata,
  Column('Task_id', ForeignKey('Task.Taskid'), primary_key=True),
  Column('University_id', ForeignKey('Students.Universityid'), primary_key=True))

class Students(Base):
  __tablename__ = "Students"
  
  Universityid = Column(Integer,primary_key=True)
  Name = Column(String(50))
  Email = Column(String(50),unique=True)
  Tasks = relationship("Task", secondary = associate_assignment, back_populates="Students")   #backref bi-direction

  def __repr__(self):
    return "Students(Universityid='%s', Name='%s', Email='%s')" % (self.Universityid, self.Name, self.Email)

associate_questiontask = Table('associate_questiontask', Base.metadata,
  Column('Question_id', ForeignKey('Question.Questionid'), primary_key = True), 
  Column('Task_id', ForeignKey('Task.Taskid'), primary_key = True),
)

class Task(Base):
  __tablename__ = "Task"
  Taskid = Column(Integer,primary_key=True)
  Title = Column(String(60))
  Text = Column(String(300))
  Questions = relationship("Question", secondary = associate_questiontask, back_populates="Task")              # <<<< HERE
  Student = relationship("Student", secondary = associate_assignment, back_populates="Students")

  def __repr__(self):
    return "Students(Taskid='%s', Title='%s', Text='%s')" % (self.Taskid, self.Title, self.Text)

class Question(Base):
  __tablename__ = "Question"
  
  Questionid = Column(Integer, ForeignKey('Answer.Questionid'), primary_key=True)
  Title = Column(String(60))
  Text = Column(String(300))
  Tasks = relationship('Task', secondary = associate_questiontask, back_populates="Question")

  def __repr__(self):
    return "Question(Questionid='%s', Title='%s', Text='%s')" % (self.Questionid, self.Title, self.Text)

class Submission(Base):
  __tablename__ = "Submission"
  Submissionid = Column(Integer, ForeignKey("Answer.Submissonid"), primary_key=True)
  Universityid = Column(Integer, ForeignKey("Students.Universityid"))
  Time = Column(DateTime)
  Evaluationid = Column(Integer, ForeignKey("Score.Evaluationid"), nullable=True)
  Evaluation_requestid = Column(Integer,nullable=True)
  Evaluation_finishedid = Column(Integer,nullable=True)

class Answer(Base):
  __tablename__ = "Answer"
  Answerid = Column(Integer, ForeignKey("Score.Scoreid"), primary_key=True)
  Text = Column(String(300))
  def __repr__(self):
    return "Answer(Questionid= '%s', Answerid='%s', Submissionid='%s',Text='%s')" % (self.Questionid, self.Answerid, self.Submissionid,self.Text,self.Text)

class Score(Base):
  __tablename__ = "Score"
  
  Scoreid = Column(Integer,primary_key=True)
  Value = Column(DECIMAL(2,1))
  Time= Column(DateTime)

  def __repr__(self):
    return "Score(Questionid= '%s', Answerid='%s', Submissionid='%s',Text='%s')" % (self.Questionid, self.Answerid, self.Submissionid,self.Text,self.Text)

#Base.metadata.create_all(engine)