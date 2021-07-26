from ClassRoomDataHandler import isValidClassroomId
from TeacherDataHandler import isValidTeacherId
from StudentDataHandler import isValidStudentId
from TeacherDataCenter import getTeacherById
from ClassRoomDataCenter import getClassroomById
from StudentDataCenter import getStudentById
from RelationshipsDataCenter import*


def addTeacherClassRelationHandler(teacherId,classroomId):
    if isValidTeacherId(teacherId) and isValidClassroomId(classroomId):
        if getTeacherById(teacherId)==None:
            print(f"Teacher with {teacherId} does not exist")
            return
        if getClassroomById(classroomId)==None:
            print(f"Classroom with {classroomId} does not exist")
            return
        if getRelationshipByTeacherId(teacherId)==None:
            addClassTeacher(teacherId,classroomId)

        else:
            print("One Teacher can own only one classroom")
    return


def addStudentClassRelationHandler(studentId,classroomId):
    if isValidStudentId(studentId) and isValidClassroomId(classroomId):
        if getStudentById(studentId)==None:
            print(f"Student with {studentId} does not exist")
            return
        if getClassroomById(classroomId)==None:
            print(f"Classroom with {classroomId} does not exist")
            return
        addStudentClass(studentId,classroomId)
    return

def showClassStudentsHandler(classroomId):
    if isValidClassroomId(classroomId):
        if getClassroomById(classroomId)!=None:
            if getRelationshipByClassroomId(classroomId)!=None:
                showClassStudents(classroomId)
            else:
                print(f"A teacher has not yet been assigned to classroom {classroomId}.Therefore students have not been assigned")
        else:
            print(f"Classroom {classroomId} does not exist")
    return

def showTeacherStudentsHandler(teacherId):
    if isValidTeacherId(teacherId):
        if getTeacherById(teacherId)!=None:
            if getRelationshipByTeacherId(teacherId)!=None:
                showTeacherStudents(teacherId)
            else:
                print(f"Teacher {teacherId} has not yet been assigned to a classroom .Therefore teacher does not have students")
        else:
            print(f"Teacher {teacherId} does not exist")
    return