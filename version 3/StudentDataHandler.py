from StudentDataCenter import*
from StudentSubjectRelation import getRelationshipsByStudentId   
###########################################################################

def isValidStudentId(studentId):
    if studentId[:2]!="ST" or not(studentId[2:].isdigit()):
        print("Student Id is invalid")
        return False
    return True

def isValidStudentName(studentName):
    for letter in studentName:
        if letter.isdigit():
            print("Student name should not have numbers included")
            return False
        if letter.isspace():
            print("Student name should not have white spaces")
            return False
    return True
    
    
def isValidDOB(date):
    """when a date is given in DD/MM/YYYY format as a string, checks whether the date is valid."""
    "If date is valid return True. Else False"
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


        
###########################################################################

def addStudentHandler(studentName,dob):
    if (isValidDOB(dob))and(isValidStudentName(studentName)):
        addStudent(studentName,dob)
    return

def modifyStudentHandler(studentId,newName,dob):
    if (isValidDOB(dob)) and (isValidStudentName(newName)) and (isValidStudentId(studentId)):
        if getStudentById(studentId)==None:
            print("Student with",studentId,"does not exist")
        else:
            if getStudentId(newName)!=None:
                print("Two students can not have same name")
            else:
                isStudentModified=modifyStudent(studentId,newName,dob)
                if isStudentModified:
                    print("Student modified correctly")       
    return

def removeStudentHandler(studentId):
    if isValidStudentId(studentId):
        if getStudentById(studentId)==None:
            print("Student with",studentId,"does not exist")
            return
    relations=getRelationshipsByStudentId(studentId)
    if relations==[]:
        isDeleted=deleteStudent(studentId)
        if isDeleted:
            print("Student deleted successfully")
    else:
        print("Can not be deleted. Student has scores stored in the system")
    return


def helpStudentHandler(studentId):
    if isValidStudentId(studentId):
        if getStudentById(studentId)==None:
            print("Student with",studentId,"does not exist")
        else:
            showStudent(studentId)
    return