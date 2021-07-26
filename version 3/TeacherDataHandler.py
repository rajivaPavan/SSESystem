from TeacherDataCenter import *
from RelationshipsDataCenter import*
from SubjectDataHandler import isValidSubjectId
from SubjectDataCenter import getSubjectById
##############################################

def isValidTeacherId(teacherId):
    if teacherId[:2]!="TC" or not(teacherId[2:].isdigit()):
        print("Teacher Id is invalid")
        return False
    return True

def isValidTeacherName(teacherName):
    for letter in teacherName:
        if letter.isdigit():
            print("Teacher's name should not have numbers included")
            return False
        if letter.isspace():
            print("Teacher's name have should have no white spaces")
            return False
    return True

def isValidStream(teacherStream):
    if str(teacherStream) == "A/L" or str(teacherStream) == "O/L" :
        return True
    else:
        print("Stream should be either A/L or O/L")
        return False

def isValidDOB(date):
    """when a date is given in DD/MM/YYYY format as a string, checks whether the date is valid.
    If valid return True. Else False"""
    import datetime
    if len(date)!=len("DD/MM/YYYY"):
        print("DOB should match with DD/MM/YYYY format")
        return False
    date=date.strip().split("/",2)
    for i in date:
        if not(i.isdigit()):
            print("DOB should match with DD/MM/YYYY format")
            return False
    year=int(date[2])
    month=int(date[1])
    day=int(date[0])
    try:
        datetime.datetime(year,month,day)
        return True
    except ValueError:
        print("DOB should match with DD/MM/YYYY format")
        return False


def isValidSubjectIdList(subjectIdList):
    teachersSubjectIds=subjectIdList.split(",")
    for subjectId in teachersSubjectIds:
        isValid=isValidSubjectId(subjectId)
        if isValid==False:
            return False
    return True

##############################################

def addTeacherHandler(teacherName,subjectIdList,TeacherDOB,teacherStream):
    if(isValidTeacherName(teacherName) and isValidSubjectIdList(subjectIdList) and isValidDOB(TeacherDOB) and isValidStream(teacherStream)):
        subjectIdList=subjectIdList.split(",")
        for subjectId in subjectIdList:
            if getSubjectById(subjectId)==None:
                print("Subject",subjectId,"does not exist")
                return
        addTeacher(teacherName,subjectIdList,TeacherDOB,teacherStream)
        return

def modifyTeacherHandler(teacherId,teacherNewName,newSubjectIdList,TeacherNewDOB,teacherNewStream):
    if (isValidTeacherId(teacherId) and isValidTeacherName(teacherNewName) and isValidSubjectIdList(newSubjectIdList) and isValidDOB(TeacherNewDOB) and isValidStream(teacherNewStream)):
        if getTeacherById(teacherId) == None:
            print(f"Teacher with {teacherId} does not exist")
        else:
            if getTeacherId(teacherNewName) != None:
                print("Two classrooms can not have same name")
            else:
                isTeacherModified=modifyTeacher(teacherId,teacherNewName,newSubjectIdList,TeacherNewDOB,teacherNewStream)
                if isTeacherModified:
                    print("Teacher modified correctly")

def removeTeacherHandler(teacherId):
    if isValidTeacherId(teacherId):
        if getTeacherById(teacherId) == None:
            print(f"Teacher with {teacherId} does not exist")
            return
        relations = getRelationshipByTeacherId(teacherId)
        if relations == []:
            isTeacherDeleted = deleteTeacher(teacherId)
            if isTeacherDeleted:
                print("Teacher deleted successfully")
        else:
            print("Can not be deleted. Teacher has information stored in the system")
    return

def helpTeacherHandler(teacherId):
    if isValidTeacherId(teacherId):
        if getTeacherById(teacherId) == None:
            print(f"Teacher with {teacherId} does not exist")
            return
        else:
            helpTeacher(teacherId)
    return



        
