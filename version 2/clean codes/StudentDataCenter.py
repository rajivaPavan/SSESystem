#here stores all the students
studentEntities=[]

def getStudentId(name):
    #return student id when student name is given (this function is for the system usage)
    for student in studentEntities:
        if(student["name"]==name):
            return student["id"]

def addStudent(id, name, dob):
    "store the student inside the student data list. return True if operation is successful"
    #todo- check the a Student with this id already exist in system. If so, return false
    #todo- check the a Student with this Student name already exist in system. If so, return false
    #todo- check the DOB is correct. If not, return false
    #return False;

    #add the new Student
    newStudent={}
    newStudent["id"]=id
    newStudent["name"]=name
    newStudent["dob"]=dob
    studentEntities.append(newStudent)
    return True;

def modifyStudent(id, name, dob):
    "modify content of a already stored Student. return True if operation is successful"
    #todo- check the a Student with this id already exist in system. If not, return false
    #return False;

    #choose the Student
    for student in studentEntities:
        if(student["id"]==id):
            selectedStudent=student

    selectedStudent["name"]=name
    selectedStudent["dob"]=dob
    return True;

def deleteStudent(id):
    "delete a Student from the system. return True if operation is successful"
    #todo- check the a Student with this id already exist in system. If not, return false
    #return False;

    #choose the Student
    for student in studentEntities:
        if(student["id"]==id):
            selectedStudent=student
    studentEntities.remove(selectedStudent)
    return True;

def getStudentById(id):
    "return the student that has given id. Otherwise return None"

    #choose the Student
    for student in studentEntities:
        if(student["id"]==id):
            return student.copy(); # give a copy of the dictionary as returned value.
    return None;
    #we can check this using if statement 'if ret_value is not None'

def getStudentByName(name):
    "return the student that has given name. Otherwise return None"

    studentEntityList=[]
    #choose the Student
    for student in studentEntities:
        if(student["name"]==name):
            studentEntityList.append(student.copy())# give a copy of the dictionary as returned value.
    return studentEntityList;
    #we can check this using if statement 'if ret_value is not None'


    
