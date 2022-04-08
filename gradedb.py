from sqlalchemy import * # package providing unified access to various databases
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import pandas as pd      # for better table visualisation

class GradeDB:
    def __init__(self,filename):
        addr = "sqlite:///" + fileName
        self._engine = create_engine(addr,echo=False)
        self._sessionMaker = sessionmaker(bind=engine)

    def newSession(self):
        return self._sessionMaker()

    def addStudent(self,universityid,name,email):
        with self.newSession() as st:
            a = Students(Universityid=universityid,Name=name,Email=email)
            st.add(a)
            st.commit()

    def addQuestion(self,title,text):
        with self.newSession() as st:
            a = Question(Title=title,Text=text)
            st.add(a)
            st.commit()

    def addTask(self,title,text,taskid,questionidlist):
        '''teacher should give the taskid and corresponsed questionid list/array'''
        with self.newSession() as st:
            a = Task(Taskid=taskid,Title=title,Text=text)
            st.add(a)
            st.commit()
        with self.newSession() as st:
            for id in questionidlist:
                b = Question_Task(Questionid=id,Taskid=taskid)
                st.add(b)
            st.commit()


    def addAssignment(self,taskid,universityid):
        '''after this method, student_notification change into 1'''
        with self.newSession() as st:
            a = Assignment(Taskid=taskid,Universityid=universityid)
            st.add(a)
            st.commit()

    def getTaskid(self,universityid):
        '''find taskid from corresponsed row'''
        with self.newSession() as st:
            return st.query(Assignment).where(Assignment.Universityid == universityid).one().Taskid

    def newSubmission(self,universityid):
        '''no submission id yet'''
        taskid=self.getTaskid(universityid)
        with self.newSession() as st:
            a = Submission(Universityid=universityid)
            a.Taskid=taskid
            st.add(a)
            st.commit()

    def getQuestionid(self,universityid,Qid_st):
        '''find Qid_st corresponsed row and the corresponsed Questionid in db'''
        taskid=self.getTaskid(universityid)
        with self.newSession() as st:
            l=[id.Questionid for id in st.query(Question_Task).where(Question_Task.Taskid == taskid).one()]
            return(l[Qid_st])

    def getSubmissionid(self,universityid,taskid):
        '''find submissionid'''
        with self.newSession() as st:
            return st.query(Submission).where(Submission.Universityid == universityid and Submission.Taskid==taskid).one().Submissionid

    def addAnswer(self,universityid,Qid_st,text):
        '''can not find corresponsed universityid'''
        submissionid=self.getSubmissionid(universityid,Qid_st)
        with self.newSession() as st:
            a = Answer(Submissionid=submissionid,Text=text)
            st.add(a)
            st.commit()

    def commitSubmission(self,universityid):
        ''''''
        with self.newSession() as st:
            a = Assignment(Universityid=universityid)
            st.add(a)
            st.commit()

    def newEvaluation(self,evalution):
        ''''''
        with self.newSession() as st:
            a = Submission(Evalution=evalution,EvalutionFinishedid=1)
            st.add(a)
            st.commit()

    def addScore(self,evalutionid,answerid,value):
        '''teacher has to give evalutionid and answerid'''
        with self.newSession() as st:
            a = Score(Evalutionid=evalutionid,Answerid=answerid,Value=value,Datetime=pd.datetime.now())
            st.add(a)
            st.commit()


