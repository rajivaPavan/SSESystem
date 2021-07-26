import pickle

with open("ClassRoomData.txt","rb") as f:
    try:
        classroomEntities=pickle.load(f)
    except EOFError:
        classroomEntities=[]
    
def getClassroomId(name):
    # return classroom id when classroom name is given (this function is for the system usage)
    for classroom in classroomEntities:
        if classroom["classroomName"] == name:
            return classroom["classroomId"]
    return None

def getClassroomById(classroomId):
    """return the classroom that has given classroomId. Otherwise return None"""
    for classroom in classroomEntities:
        if classroom["classroomId"] == classroomId:
            return classroom.copy()
    return None

def addClassroom(classroomName, capacity,location):
    """store the classroom inside the classroom data list. return True if operation is successful"""
    for classroom in classroomEntities:
        if classroom["classroomName"] == classroomName:
            print("Two classrooms can not have same name")
            return False

    if classroomEntities==[]:
        lastSavedIdNumber = "0"
    else:
        lastSavedId=classroomEntities[-1]["classroomId"] #update classroomId as first element in classroomEntities list
        lastSavedIdNumber=lastSavedId[2:]
    numberOfDigitsInID = 3
    if lastSavedIdNumber == "9" * len(lastSavedIdNumber):
        numberOfDigitsInID = len(lastSavedIdNumber) + 1
    classroomId="CR"+str(int(lastSavedIdNumber)+1).rjust(numberOfDigitsInID,"0")

    # add the new Classroom
    newClassroom = {}
    newClassroom["classroomId"] = classroomId
    newClassroom["classroomName"] = classroomName
    newClassroom["capacity"] = capacity
    newClassroom["location"] = location
    classroomEntities.append(newClassroom)
    print(f"Class Room is added into the system, Class Room id is {classroomId}.")
    return True


def modifyClassroom(classroomId, classroomName, capacity,location):
    """modify content of a already stored classroom. return True if operation is successful"""
    for classroom in classroomEntities:
        if classroom["classroomId"] == classroomId:
            selectedClassroom = classroom
            selectedClassroom["classroomName"] = classroomName
            selectedClassroom["capacity"] = capacity
            selectedClassroom["location"] = location
            return True
    return False


def deleteClassroom(classroomId):
    """delete a classroom from the system. return True if operation is successful"""
    for classroom in classroomEntities:
        if classroom["classroomId"] == classroomId:
            selectedClassroom = classroom
            classroomEntities.remove(selectedClassroom)
            return True
    return False


def helpClassroom(classroomId):
    """prints dictionary with classroom details"""
    selectedClassroomCopy = getClassroomById(classroomId)
    print("Class Id: " + selectedClassroomCopy["classroomId"])
    print("Name: " + selectedClassroomCopy["classroomName"])
    print("Capacity: " + selectedClassroomCopy["capacity"])
    print("Location: " + selectedClassroomCopy["location"])
    return True


def showAllClassrooms():
    print(classroomEntities)

def saveClassroomData():
    """saves classroomEntities in the ClassRoomData file"""
    with open("ClassRoomData.txt","wb") as classroomData:
        pickle.dump(classroomEntities,classroomData)