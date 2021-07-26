from SubjectDataCenter import*
from TeacherDataCenter import isATeacherDoingASubject
###########################################################################

def isValidSubjectId(subjectId):
    if subjectId[:2]!="SB" or not(subjectId[2:].isdigit()):
        print("Subject Id is invalid")
        return False
    return True

def isValidSubjectName(subjectName):
    for letter in subjectName:
        if letter.isdigit():
            print("Subject name should not have numbers included")
            return False
        if letter.isspace():
            print("Subject name should not have white spaces")
            return False
    return True

def isValidStream(stream):
    if stream!= "A/L" and stream!= "O/L" :
        print("Stream should be either A/L or O/L")
        return False
    return True
        
###########################################################################

def addSubjectHandler(subjectName,stream):
    if (isValidStream(stream))and(isValidSubjectName(subjectName)):
        addSubject(subjectName,stream)
    return

def modifySubjectHandler(subjectId,newName,stream):
    if isValidStream(stream)and(isValidSubjectName(newName)) and isValidSubjectId(subjectId):
        if getSubjectById(subjectId) == None:
            print("Subject with", subjectId, "does not exist")
        else:
            if getSubjectId(newName) != None:
                print("Two subjects can not have same name")
            else:
                isSubjectModified = modifySubject(subjectId, newName, dob)
                if isSubjectModified:
                    print("Subject modified correctly")
    return
        

def removeSubjectHandler(subjectId):
    if isValidSubjectId(subjectId):
        if getSubjectById(subjectId)==None:
            print("Subject with",subjectId,"does not exist")
            return
    isOkToDelete=isATeacherDoingASubject(subjectId)
    if isOkToDelete:
        isDeleted=deleteSubject(subjectId)
        if isDeleted:
            print("Subject deleted successfully")
    else:
        print("Can not be deleted. Subject has scores stored in the system")
    return


def helpSubjectHandler(subjectId):
    if isValidSubjectId(subjectId):
        if getSubjectById(subjectId)==None:
            print("Subject with",subjectId,"does not exist")
        else:
            showSubject(subjectId)
    return


    
