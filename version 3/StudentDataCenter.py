import RelationshipsDataCenter as rdc
import pickle

with open("StudentData.txt", "rb") as f:
    try:
        studentEntities = pickle.load(f)
    except EOFError:
        studentEntities = []


def getStudentId(name):
    """return student id when student name is given (this function is for the system usage)"""
    for student in studentEntities:
        if student["studentName"] == name:
            return student["id"]


def getStudentById(studentId):
    """return the student that has given id. Otherwise return None"""
    for student in studentEntities:
        if student["studentId"] == studentId:
            return student.copy()
    return None


def addStudent(studentName, dob):
    """store the student inside the student data list. return True if operation is successful"""
    for student in studentEntities:
        if student["studentName"] == studentName:
            print("Two students can not have same name")
            return False

    #generating ID
    if studentEntities == []:
        lastSavedIdNumber = "0"
    else:
        lastSavedId = studentEntities[-1]["studentId"]  # update studentId as first element in teacherEntities list
        lastSavedIdNumber = lastSavedId[2:]
    numberOfDigitsInID = 3
    if lastSavedIdNumber == "9" * len(lastSavedIdNumber):
        numberOfDigitsInID = len(lastSavedIdNumber) + 1
    studentId = "ST" + str(int(lastSavedIdNumber) + 1).rjust(numberOfDigitsInID, "0")

    # add the new Student
    newStudent = {}
    newStudent["studentId"] = studentId
    newStudent["studentName"] = studentName
    newStudent["dob"] = dob
    newStudent["classroomId"] = None
    studentEntities.append(newStudent)
    print(f"Student is added into the system, Student Id is {studentId}.")
    return True


def modifyStudent(studentId, studentName, dob):
    """modify content of a already stored student. return True if operation is successful"""
    for student in studentEntities:
        if student["studentId"] == studentId:
            selectedStudent = student
            selectedStudent["studentName"] = studentName
            selectedStudent["dob"] = dob
            return True
    return False


def deleteStudent(studentId):
    """delete a student from the system. return True if operation is successful"""
    for student in studentEntities:
        if student["studentId"] == studentId:
            selectedStudent = student
            classroomId = selectedStudent["classroomId"]
            if classroomId is not None:
                rdc.removeStudentFromClassroom(studentId, classroomId)
            studentEntities.remove(selectedStudent)
            return True
    return False


def showStudent(studentId):
    """prints dictionary with student details"""
    selectedStudentCopy = getStudentById(studentId)
    print("Student Id: " + studentId)
    print("Name: " + selectedStudentCopy["studentName"])
    print("Date of Birth: " + selectedStudentCopy["dob"])
    print("Class: " + selectedStudentCopy["classroomId"])
    return


def saveStudentsData():
    """saves student data in text file in write binary mode"""
    with open("StudentData.txt", "wb") as studentData:
        pickle.dump(studentEntities, studentData)
