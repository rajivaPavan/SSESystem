import pickle

with open("TeacherData.txt","rb") as f:
    try:
        teacherEntities=pickle.load(f)
    except EOFError:
        teacherEntities=[]

def getTeacherId(teacherName):
    # return classroom id when classroom name is given (this function is for the system usage)
    for teacher in teacherEntities:
        if teacher["teacherName"] == teacherName:
            return teacher["id"]
    return None

def getTeacherById(teacherId):
    """return the teacher that has given id. Otherwise return None"""
    for teacher in teacherEntities:
        if teacher["teacherId"] == teacherId:
            return teacher.copy()
    return None

def addTeacher(teacherName,subjectIdList,teacherDOB,teacherStream):
    for teacher in teacherEntities:
        if teacher["teacherName"] == teacherName:
            print("Two teachers can not have same name")
            return False
    if teacherEntities==[]:
        lastSavedIdNumber="0"
    else:
        lastSavedId=teacherEntities[-1]["teacherId"] #update teacherId as first element in teacherEntities list
        lastSavedIdNumber=lastSavedId[2:]
    numberOfDigitsInID = 3
    if lastSavedIdNumber == "9" * len(lastSavedIdNumber):
        numberOfDigitsInID = len(lastSavedIdNumber) + 1
    teacherId="TC"+str(int(lastSavedIdNumber)+1).rjust(numberOfDigitsInID,"0")

    # add the new teacher
    newTeacher={}
    newTeacher["teacherId"]=teacherId
    newTeacher["teacherName"]=teacherName
    newTeacher["subjectIdList"]=subjectIdList
    newTeacher["TeacherDOB"]=teacherDOB
    newTeacher["TeacherStream"]=teacherStream
    teacherEntities.append(newTeacher)
    print(f"Teacher is added into the system, Teacher id is {teacherId}.")
    return True



def modifyTeacher(teacherId,teacherNewName,newSubjectIdList,TeacherNewDOB,teacherNewStream):
    for teacher in teacherEntities:
        if teacher["teacherId"]==teacherId:
            selectedTeacher=teacher
            selectedTeacher["teacherName"]=teacherNewName
            selectedTeacher["subjectIdList"]=newSubjectIdList
            selectedTeacher["TeacherDOB"]=TeacherNewDOB
            selectedTeacher["TeacherStream"]=teacherNewStream
            return True
    return False

def deleteTeacher(teacherId):
    for teacher in teacherEntities:
        if teacher["teacherId"]==teacherId:
            selectedTeacher=teacher
            teacherEntities.remove(selectedTeacher)
            return True
    return False

def helpTeacher(teacherId):
    selectedTeacher = getTeacherById(teacherId)
    print("Your teachers details are - ")
    print("Teacher Id - "+selectedTeacher["teacherId"])
    print("Teacher Name - "+selectedTeacher["teacherName"])
    print("Subject Id List - "+",".join(selectedTeacher["subjectIdList"]))
    print("Teacher DOB - "+selectedTeacher["TeacherDOB"])
    print("Teacher Stream - "+selectedTeacher["TeacherStream"])
    return True


def isATeacherDoingASubject(subjectId):
    for teacher in teacherEntities:
        if subjectId in teacher["subjectIdList"]:
            return True
    return False


def saveTeachersData():
    """saves teacherEntitites in the TeacherData file"""
    with open("TeacherData.txt","wb") as teacherData:
        pickle.dump(teacherEntities,teacherData)
