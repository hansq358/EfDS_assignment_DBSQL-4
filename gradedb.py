from sqlalchemy import *
from sqlalchemy.orm import *
import pandas as pd
from schema import *
import random
import numpy as np
import os
from sqlalchemy.event import *


class GradeDB:
    
    def __init__(self, fileName):
        global engine
        addr = "sqlite:///" + fileName
        #if(os.path.isfile(fileName)): 
            #os.remove(fileName)
        engine = create_engine(addr,echo=False)
        self.sessionMaker = sessionmaker(bind=engine)
    
    def newSession(self):
        return self.sessionMaker()
    
    def Create(self):
        #%run schema.py
        Base.metadata.create_all(engine)

    def addStudent(self,universityid,name,email):
        with self.newSession() as st:
            a = Students(Universityid=universityid,Name=name,Email=email)
            st.add(a)
            st.commit()

    def addQuestion(self,qid,title,text):
        with self.newSession() as st:
            a = Question(Questionid=qid,Title=title,Text=text)
            st.add(a)
            st.commit()
            
    def addTask(self,title,text,taskid,qid_list):
        '''teacher should give the taskid and corresponsed questionid list/array'''
        l=[]
        with self.newSession() as s1:
            for id in qid_list:
                l.append(s1.query(Question).where(Question.Questionid == id).one())
        with self.newSession() as s2:
            a=Task(Taskid=taskid,Title=title,Text=text)
            a.Question=l
            s2.add(a)
            s2.commit()

    def addAssignment(self,taskid,universityid):
        '''after this method, student_notification change into 1'''
        def new_ass(session):
            print("NEW ASSIGNMENT!")

        with self.newSession() as st: 
           
            a = Assignment(Taskid=taskid,Universityid=universityid)
            listen(st, "append", new_ass)
            st.add(a)
            st.commit()
            
    def getAssignmentid(self,universityid):
        '''find taskid from corresponsed row'''
        with self.newSession() as st:
            return st.query(Assignment).where(Assignment.Universityid == universityid).one().Assignmentid

    def newSubmission(self,universityid):
        '''no submission id yet'''
        assignmentid=self.getAssignmentid(universityid)
        with self.newSession() as st:
            a = Submission(Evaluation_request=False,Time=pd.datetime.now())
            a.Assignmentid=assignmentid
            st.add(a)
            st.commit()

    def getTaskid(self,universityid):
        with self.newSession() as st:
            return st.query(Assignment).filter(Assignment.Universityid == universityid).one().Taskid
    
    def getQuestionid(self,taskid):
        with self.newSession() as st:
            return [id.Questionid for id in st.query(Question).filter(Question.Task.any(Taskid=taskid)).all()]
    
    def getSubmissionid(self,assignmentid):
        '''find newest submissionid of one specific student'''
        with self.newSession() as st:
            return(st.query(Submission).filter(Submission.Assignmentid == assignmentid).order_by(desc(Submission.Time)).first().Submissionid)
                   
    def addAnswer(self,universityid,Q_id,text):
        '''Q_id is the question id of a specific student's task'''
        assignmentid=self.getAssignmentid(universityid)
        submissionid=self.getSubmissionid(assignmentid)
        taskid=self.getTaskid(universityid)
        questionid=self.getQuestionid(taskid)
        with self.newSession() as st:
            for i in range(len(Q_id)):
                a=Answer(Submissionid=submissionid,Questionid=questionid[i],Text=text)
                st.add(a)
                st.commit()        
      
    def getAnswerid(self,submissionid):
        with self.newSession() as st:
            return [id.Answerid for id in st.query(Answer).filter(Answer.Submissionid == submissionid)]
        
    def addScore(self,universityid,value):
        '''teacher has to give universityid of one student'''
        '''value: score list of one student's all answer'''
        assignmentid=self.getAssignmentid(universityid)
        submissionid=self.getSubmissionid(assignmentid)
        answeridlist=self.getAnswerid(submissionid)
        with self.newSession() as st:
            for i in range(len(answeridlist)):
                a = Score(Submissionid=submissionid,Answerid=answeridlist[i],Value=value[i],Time=pd.datetime.now())
                st.add(a)
                st.commit()

    def addAssignment(self,taskid,universityid):
        '''after this method, student_notification change into 1'''
        with self.newSession() as st:
            a = Assignment(Taskid=taskid,Universityid=universityid)
            st.add(a)
            st.commit()
    
    def commitSubmission(self,universityid):
        ''''''
        Ass_ID=self.getAssignmentid(universityid)
        
        def new_sub(session):
            print("NEW SUBMISSION!")
        
        with self.newSession() as st:
            
            a_result= st.query(Submission).filter(Submission.Assignmentid == Ass_ID).one()
            a_result.Evaluation_request = True
            st.commit()
            listen(st, "after_commit", new_sub)
         
    def newEvaluation(self,universityid,evalution):
        '''teacher uses this method to get the assignment 
        waiting for evalution corresponseding student university id '''
        assignmentid=self.getAssignmentid(universityid)
        with self.newSession() as st:
            a_result= st.query(Submission).filter(Submission.Assignmentid == assignmentid).one()
            a_result.Evaluation=evalution
            st.commit()
            
    def commitEvaluation(self,universityid):
        '''Teacher inputs university IDs to access the "submission table" and add evaluations of corresponding university IDs.'''
        Ass_ID=self.getAssignmentid(universityid)
        
        def eva_fin(session):
            print("EVALUATION FINISHED!")
            
        with self.newSession() as st:
            if(st.query(Submission).filter(Submission.Assignmentid == Ass_ID).one().Evaluation_finished==True):
                print('Evaluation is finished. Any further change will be rejected!')
                
            else:
                with self.newSession() as st:
            
                    a_result= st.query(Submission).filter(Submission.Assignmentid == Ass_ID).one()
                    a_result.Evaluation_finished = True
                    st.commit()
                    listen(st, "after_commit", eva_fin)