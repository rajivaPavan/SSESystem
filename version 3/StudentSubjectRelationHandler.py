from StudentSubjectRelation import*

from StudentDataCenter import getStudentId,getStudentById
from StudentDataHandler import isValidStudentId
from SubjectDataCenter import getSubjectId,getSubjectById
from SubjectDataHandler import isValidSubjectId

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
        return True
    return False

def isStudentNotExisting(studentId):
    "return True if student does not exists"
    if getStudentById(studentId)==None:
        print("Student with student name, "+studentId+" does not exist")
        return True
    return False

def isSubjectNotExisting(subjectId):
    "return True if subject does not exists"
    if getSubjectById(subjectId)==None:
        print("Subject with, "+subjectId+" does not exist")
        return True
    return False

studentSubjectIdSeq=0 #initialze student-subject-relation-id

def addMarkHandler(studentId,subjectId,score):
    "Validates user input for addMark"
    if isValidSubjectId(subjectId) and isValidStudentId(studentId):
        global studentSubjectIdSeq
        studentSubjectIdSeq+=1
        if isStudentNotExisting(studentId):
            return
        if isSubjectNotExisting(subjectId):
            return
        if isMarkGiven(studentId,subjectId):
            print("This student has marks for this subject already")
            #a mark has already been given for the relevant student and subject
            return
        if (checkErrorInMark(score)):
            #there is an error in the mark
            return
        addStudentSubjectRelation(studentSubjectIdSeq,studentId,subjectId,score)
        print("Mark added successfully")
        return

def modifyMarkHandler(studentId,subjectId,newStudentId,newSubjectId,score):
    "Update student name, subject name and score"
    if isValidStudentId(studentId) and isValidSubjectId(subjectId) and isValidStudentId(newStudentId) and isValidSubjectId(newSubjectId):
        relationId=getRelationId(studentId,subjectId)
        if (isStudentNotExisting(studentId)):
            return
        if (isSubjectNotExisting(subjectId)):
            return
        if not(isMarkGiven(studentId,subjectId)):
            print("This student has no marks for this subject yet")
            #the given student has no marks for the given subject
            return
        if (checkErrorInMark(score)):
            #there is an error in the mark
            return
        modifyStudentSubjectRelation(relationId,newStudentId,newSubjectId,score)
        print("Mark modified successfully")
        return

def removeMarkHandler(studentId,subjectId):
    "Clear student’s score. After clearing score , user can add it again."
    if isValidSubjectId(subjectId) and isValidStudentId(studentId):
        relationId=getRelationId(studentId,subjectId)

        if isStudentNotExisting(studentId):
            return
        if isSubjectNotExisting(subjectId):
            return
        if not(isMarkGiven(studentId,subjectId)):
            print("This student has no marks for this subject yet")
            #the given student has no marks for the given subject
            return
        deleteStudentSubjectRelation(relationId)
        print("Mark removed successfully")
        return

def showMarkHandler(studentId,subjectId):
    "show all details of the score."
    relationId=getRelationId(studentId,subjectId)

    if isStudentNotExisting(studentId):
        return
    if isSubjectNotExisting(subjectId):
        return

    markRelation=getRelationshipByRelationId(relationId)
    if markRelation==None:
        print("This student has no marks for this subject")
    else:
        print("Mark = "+str(markRelation["score"]))
    return



def findWordWithMaxLength(words):
    "finds the longest word"
    lenOfWords=list(map(len,words))
    return max(lenOfWords)

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
    return

def showAllStudentsHandler(subjectId):
    "Show all student details related to the subject as a table."
    if (isSubjectNotExisting(subjectId)):
        return
    relationships=getRelationshipsBySubjectId(subjectId)
    studentIds=[relation["studentId"] for relation in relationships]
    students=[getStudentById(studentId) for studentId in studentIds]
    
    studentsDict={}
    for studentInfo in students:
        studentId=studentInfo["studentId"]
        dob=studentInfo["dob"]
        studentsDict[studentId]=dob
    tabulate(studentsDict,"Student Id","Date of Birth")
    return

def showAllMarksHandler(studentId):
    "Show all marks related to the student as a table."
    if (isStudentNotExisting(studentId)):
        return
    print("Marks of "+studentId)
    studentMarks=getRelationshipsByStudentId(studentId)
    
    studentMarksDict={}
    for relation in studentMarks:
        subjectId=relation["subjectId"]
        subject=getSubjectById(subjectId)
        subjectId=subject["subjectId"]
        subjectMark=relation["score"]
        studentMarksDict[subjectId]=subjectMark

    tabulate(studentMarksDict,"Subject Id","Mark")
    return
