from ClassRoomDataCenter import*
from RelationshipsDataCenter import*

def isValidClassroomName(classroomName):
    """checks whether classroom name is valid or not. returns True or False respectively."""
    classroomName=classroomName.split("-",1)
    if classroomName[0].isdigit():
        if int(classroomName[0])<=0 or int(classroomName[0])>13:
            print("CLass grade should be between 1 and 13")
            return False
    else:
        print("CLass grade should be between 1 and 13")
        return False

    if not(classroomName[1].isupper()):
        print("CLass should be between A and Z")
        return False

    return True

def isValidCapacity(capacity):
    """checks whether capacity is valid or not. returns True or False respectively."""
    if not(capacity.isdigit()) or capacity=='0':
        print("Classroom capacity is not valid")
        return False
    return True

def isValidClassroomId(classroomId):
    """checks whether classroom Id is valid or not. returns True or False respectively."""
    if classroomId[:2]!="CR" or not(classroomId[2:].isdigit()):
        print("Classroom Id is invalid")
        return False
    return True

###########################################################################

def addClassroomHandler(classroomName, capacity, location):
    if isValidClassroomName(classroomName) and isValidCapacity(capacity):
        addClassroom(classroomName, capacity, location)
    return

def modifyClassroomHandler(classroomId, newName, capacity, location):
    if isValidClassroomId(classroomId) and isValidClassroomName(newName) and isValidCapacity(capacity):
        if getClassroomById(classroomId) == None:
            print(f"Classroom with {classroomId} does not exist")
        else:
            if getClassroomId(newName) != None:
                print("Two classrooms can not have same name")
            else:
                isClassroomModified = modifyClassroom(classroomId, newName, capacity,location)
                if isClassroomModified:
                    print("Classroom modified correctly")
    return


def removeClassroomHandler(classroomId):
    if isValidClassroomId(classroomId):
        if getClassroomById(classroomId) == None:
            print(f"Classroom with {classroomId} does not exist")
            return
        relations = getRelationshipByClassroomId(classroomId)
        if relations == []:
            isDeleted = deleteClassroom(classroomId)
            if isDeleted:
                print("Classroom deleted successfully")
        else:
            print("Can not be deleted. Classroom has information stored in the system")
    return

def helpClassroomHandler(classroomId):
    if isValidClassroomId(classroomId):
        if getClassroomById(classroomId) == None:
            print(f"Classroom with {classroomId} does not exist")
            return
        else:
            helpClassroom(classroomId)
    return
