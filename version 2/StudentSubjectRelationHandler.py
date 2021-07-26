from StudentSubjectRelation import*

from StudentDataCenter import getStudentId,getStudentById
from SubjectDataCenter import getSubjectId,getSubjectById

def checkErrorInMark(mark):
    #display the relevant errors in the mark. Return True if error occurs else return False
    if (mark[1:].find("-")>0 or not(mark.isdigit())): #condition1-checks whether number is negative #condition2-checks whether mark is a number
        print("Student mark should be a number")
        return True
    if int(mark)<0:
        print("Student mark should be greater than zero")
        return True
    elif int(mark)>100:
        print("Student mark should be less or equal to 100")
        return True;
    return False;

def isStudentNotExisting(studentId,studentName):
    "return True if student does not exists"
    if (getStudentById(studentId)==None):
        print("Student with student name, "+studentName+" does not exist")
        #Student with <student_name> does not exist
        return True;
    return False

def isSubjectNotExisting(subjectId,subjectName):
    "return True if subject does not exists"
    if (getSubjectById(subjectId)==None):
        print("Subject with subject name, "+subjectName+" does not exist")
        #Subject with <subject_name> does not exist
        return True;
    return False;

studentSubjectIdSeq=0 #initialze student-subject-relation-id

def addMarkHandler(studentName,subjectName,score):
    "Validates user input for addMark"
    global studentSubjectIdSeq
    studentSubjectIdSeq+=1
    studentId=getStudentId(studentName)
    subjectId=getSubjectId(subjectName)

    if (isStudentNotExisting(studentId,studentName)):
        return;
    if (isSubjectNotExisting(subjectId,subjectName)):
        return;
    if isMarkGiven(studentId,subjectId):
        print("This student has marks for this subject already")
        #a mark has already been given for the relevant student and subject
        return;
    if (checkErrorInMark(score)):
        #there is an error in the mark
        return;
    addStudentSubjectRelation(studentSubjectIdSeq,studentId,subjectId,score)
    print("Mark added successfully")
    return;

def modifyMarkHandler(oldStudentName,oldSubjectName,newStudentName,newSubjectName,score):
    "Update student name, subject name and score"
    global studentSubjectIdSeq
    
    studentId=getStudentId(oldStudentName)
    subjectId=getSubjectId(oldSubjectName)
    relationId=getRelationId(studentId,subjectId)
    
    if (isStudentNotExisting(studentId,oldStudentName)):
        return;
    if (isSubjectNotExisting(subjectId,oldSubjectName)):
        return;
    if not(isMarkGiven(studentId,subjectId)):
        print("This student has no marks for this subject yet")
        #the given student has no marks for the given subject 
        return;
    if (checkErrorInMark(score)):
        #there is an error in the mark
        return;
    modifyStudentSubjectRelation(relationId,studentId,subjectId,score)
    print("Mark modified successfully")
    return;

def removeMarkHandler(studentName,subjectName):
    "Clear student’s score. After clearing score , user can add it again."
    global studentSubjectIdSeq
    
    studentId=getStudentId(studentName)
    subjectId=getSubjectId(subjectName)
    relationId=getRelationId(studentId,subjectId)
    
    if (isStudentNotExisting(studentId,studentName)):
        return;
    if (isSubjectNotExisting(subjectId,subjectName)):
        return;
    if not(isMarkGiven(studentId,subjectId)):
        print("This student has no marks for this subject yet")
        #the given student has no marks for the given subject 
        return;
    deleteStudentSubjectRelation(relationId)
    print("Mark removed successfully")
    return;

def showMarkHandler(studentName,subjectName):
    "show all details of the score."
    studentId=getStudentId(studentName)
    subjectId=getSubjectId(subjectName)
    relationId=getRelationId(studentId,subjectId)

    if (isStudentNotExisting(studentId,studentName)):
        return;
    if (isSubjectNotExisting(subjectId,subjectName)):
        return

    markRelation=getRelationshipByRelationId(relationId)
    if markRelation==None:
        print("This student has no marks for this subject")
    else:
        print("Mark = "+str(markRelation["score"]))
    return;



def findWordWithMaxLength(words):
    "finds the longest word"
    lenOfWords=list(map(len,words))
    return max(lenOfWords);

def tabulate(infoDict,Column1,Column2):
    "prints a two column table when a dictionary is given"
    "key of dictionary goes to the first column and the value goes to the second column"
    lengthOne=len(Column1)
    lengthTwo=len(Column2)
    Column1Data=list(infoDict.keys())
    Column2Data=[infoDict[key] for key in Column1Data]
    if len(infoDict)>0:
        Column1Length=findWordWithMaxLength(Column1Data)
        Column2Length=findWordWithMaxLength(Column2Data)
        if Column1Length>lengthOne:
            lengthOne=Column1Length
        if Column2Length>lengthTwo:
            lengthTwo=Column2Length
        
    totalLength=lengthOne+7+lengthTwo
    print("="*totalLength)
    print("| "+Column1.center(lengthOne," ")+" | "+Column2.center(lengthTwo," ")+" |")
    print("="*totalLength)
    for key in infoDict:
        value=infoDict[key]
        if value==None:
            value=""
        print("|"+key.center(lengthOne+2," ")+"|"+value.center(lengthTwo+2," ")+"|")
    return;

def showAllStudentsHandler(subjectName):
    "Show all student details related to the subject as a table."
    subjectId=getSubjectId(subjectName)
    if (isSubjectNotExisting(subjectId,subjectName)):
        return;
    relationships=getRelationshipsBySubjectId(subjectId)
    studentIds=[relation["studentId"] for relation in relationships]
    students=[getStudentById(studentId) for studentId in studentIds]
    
    studentsDict={}
    for studentInfo in students:
        studentName=studentInfo["studentName"]
        dob=studentInfo["dob"]
        studentsDict[studentName]=dob
    tabulate(studentsDict,"Name","Date of Birth")
    return;

def showAllMarksHandler(studentName):
    "Show all marks related to the student as a table."
    studentId=getStudentId(studentName)
    if (isStudentNotExisting(studentId,studentName)):
        return;
    print("Marks of "+studentName)
    studentMarks=getRelationshipsByStudentId(studentId)
    
    studentMarksDict={}
    for relation in studentMarks:
        subjectId=relation["subjectId"]
        subject=getSubjectById(subjectId)
        subjectName=subject["subjectName"]
        subjectMark=relation["score"]
        studentMarksDict[subjectName]=subjectMark

    tabulate(studentMarksDict,"Subject","Mark") 
    return;
