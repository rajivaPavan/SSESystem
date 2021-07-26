
studentEntities=[]

def getStudentId(name):
    #return student id when student name is given (this function is for the system usage)
    for student in studentEntities:
        if(student["studentName"]==name):
            return student["id"];

def addStudent(id, studentName, dob):
    "store the student inside the student data list. return True if operation is successful"
    for student in studentEntities:
        if student["id"]==id:
            return False;
        if student["studentName"]==studentName :
            print("Two students can not have same name")
            return False;

    #add the new Student
    newStudent={}
    newStudent["id"]=id
    newStudent["studentName"]=studentName
    newStudent["dob"]=dob
    studentEntities.append(newStudent)
    return True;

def modifyStudent(id, studentName, dob):
    "modify content of a already stored student. return True if operation is successful"
    for student in studentEntities:
        if(student["id"]==id):
            selectedStudent=student
            selectedStudent["studentName"]=studentName
            selectedStudent["dob"]=dob
            return True;
    return False;

def deleteStudent(id):
    "delete a student from the system. return True if operation is successful"
    for student in studentEntities:
        if(student["id"]==id):
            selectedStudent=student
            studentEntities.remove(selectedStudent)
            return True;
    return False;
    

def showStudent(studentName):
    "prints dictionary with student details"
    for student in studentEntities:
        if(student["studentName"]==studentName):
            selectedStudentCopy=student.copy()
            break
    del selectedStudentCopy["id"]
    print("Name: "+selectedStudentCopy["studentName"])
    print("Date of Birth: "+selectedStudentCopy["dob"])
    return;

def getStudentById(id):
    "return the student that has given id. Otherwise return None"

    for student in studentEntities:
        if(student["id"]==id):
            return student.copy(); 
    return None;
    

def getStudentByStudentName(studentName):
    "return the student that has given id. Otherwise return None"

    studentEntityList=[]
     
    for student in studentEntities:
        if(student["studentName"]==studentName):
            studentEntityList.append(student.copy()) # give a copy of the dictionary as returned value.
    return studentEntityList;
    
