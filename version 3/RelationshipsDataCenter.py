from StudentDataCenter import*
import pickle

# newClassroom={"classroomId":id,"teacherId":teacherId , "students":[list of ids of students]}
# relationships[list of classrooms(dictionaries)]

#load data from text file
with open("RelationshipsData.txt", "rb") as f:
    try:
        relationships = pickle.load(f)
    except EOFError:
        relationships = []


def addClassTeacher(teacherId, classroomId):
    """adds a relationship to the system. return True if operation is successful"""
    # add the new TeacherClassRelation
    newTeacherClassRelation = {}
    newTeacherClassRelation["teacherId"] = teacherId
    newTeacherClassRelation["classroomId"] = classroomId
    newTeacherClassRelation["students"] = []
    relationships.append(newTeacherClassRelation)
    print(f"Teacher {teacherId} assigned to classroom {classroomId}")
    return True


def addStudentClass(studentId, classroomId):
    """adds a relationship to the system. return True if operation is successful"""
    # add the new TeacherClassRelation
    for classroom in relationships:
        if classroom["classroomId"] == classroomId:
            student=getStudentById(studentId)
            if student["classroomId"] is not None:
                assignedClassroom=student["classroomId"]
                print(f"Student {studentId} has a already been assigned to classroom {assignedClassroom}")
                return False
            classStudents = classroom["students"]
            classStudents.append(studentId)  #updating studentList in relationship in RelationshipsDataCenter
            for student in studentEntities:  #updating classroomId in studentEntity in studentDataCenter
                if student["studentId"]==studentId:
                    student["classroomId"]=classroomId
                    break
            print(f"Student {studentId} assigned to classroom {classroomId}")
            return True

    print(f"Class room {classroomId} does not have a class teacher yet. Assign a class teacher first.")
    return False

def removeStudentFromClassroom(studentId,classroomId):
    """removing student from studentList in relationship in RelationshipsDataCenter"""
    for classroom in relationships:
        if classroom["classroomId"] == classroomId:
            classroom["students"].remove(studentId)
            break
    return

def getRelationshipByTeacherId(teacherId):
    """ returns a copy of relationships,if it exists, when teacherId is given, else return None """
    for relationship in relationships:
        if relationship["teacherId"] == teacherId:
            return relationship.copy()
    return None


def getRelationshipByClassroomId(classroomId):
    """ returns a copy of relationships,if it exists, when classroomId is given, else return None """
    for relationship in relationships:
        if relationship["classroomId"] == classroomId:
            return relationship.copy()
    return None


def showClassStudents(classroomId):
    """print list of students in classroom"""
    classroom = getRelationshipByClassroomId(classroomId)
    print(f"List of Students of {classroomId} :")
    print("Id".ljust(5, " ") + " " + "Name")
    print("--".ljust(5, " ") + " " + "----")
    for studentId in classroom["students"]:
        student = getStudentById(studentId)
        print(studentId + " " + student["studentName"])
    return


def showTeacherStudents(teacherId):
    """print list of students of teacher"""
    classroom = getRelationshipByTeacherId(teacherId)
    print(f"List of Students of {teacherId} :")
    print("Id".ljust(5," ")+" "+"Name")
    print("--".ljust(5," ")+" "+"----")
    for studentId in classroom["students"]:
        student=getStudentById(studentId)
        print(studentId+" "+student["studentName"])
    return


def saveRelationshipDaTa():
    """saves relationship data in text file in write binary mode"""
    with open("RelationshipsData.txt", "wb") as f:
        pickle.dump(relationships, f)

